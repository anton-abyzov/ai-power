const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 TESTING FRAME SVG FILES\n');

  // List all frame SVG files
  const framesDir = path.join(__dirname, 'docs', 'episodes', '01-portfolio-no-code', 'diagrams', 'frames');
  const svgFiles = fs.readdirSync(framesDir).filter(file => file.endsWith('.svg'));

  console.log(`Found ${svgFiles.length} frame SVG files to test:\n`);

  let allValid = true;

  for (const svgFile of svgFiles) {
    const filePath = path.join(framesDir, svgFile);
    const fileUrl = `file://${filePath}`;

    // Navigate to the SVG file
    await page.goto(fileUrl);
    await page.waitForTimeout(500);

    // Check SVG content
    const svgAnalysis = await page.evaluate(() => {
      const svg = document.querySelector('svg');
      if (!svg) return { error: 'No SVG found' };

      // Count different element types
      const elements = {
        paths: svg.querySelectorAll('path').length,
        rects: svg.querySelectorAll('rect').length,
        circles: svg.querySelectorAll('circle').length,
        ellipses: svg.querySelectorAll('ellipse').length,
        texts: svg.querySelectorAll('text').length,
        lines: svg.querySelectorAll('line').length,
        images: svg.querySelectorAll('image').length
      };

      // Count visible elements (with non-zero dimensions)
      const allElements = svg.querySelectorAll('*');
      const visibleElements = Array.from(allElements).filter(el => {
        const rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
      });

      // Get SVG dimensions
      const viewBox = svg.getAttribute('viewBox');
      const width = svg.getAttribute('width');
      const height = svg.getAttribute('height');

      // Check for actual content (not just the background)
      const hasContent = Object.values(elements).some(count => count > 1); // More than just background rect

      return {
        elements,
        totalElements: allElements.length,
        visibleElements: visibleElements.length,
        viewBox,
        width,
        height,
        hasContent
      };
    });

    const frameName = svgFile.replace('.svg', '');
    if (svgAnalysis.error) {
      console.log(`❌ ${frameName}: ${svgAnalysis.error}`);
      allValid = false;
    } else if (!svgAnalysis.hasContent) {
      console.log(`⚠️  ${frameName}: No visible content (empty SVG)`);
      allValid = false;
    } else {
      const elementSummary = Object.entries(svgAnalysis.elements)
        .filter(([_, count]) => count > 0)
        .map(([type, count]) => `${count} ${type}`)
        .join(', ');

      console.log(`✅ ${frameName}`);
      console.log(`   Size: ${Math.round(svgAnalysis.width)}x${Math.round(svgAnalysis.height)}`);
      console.log(`   Content: ${elementSummary}`);
      console.log(`   Visible elements: ${svgAnalysis.visibleElements}`);
    }

    // Take a screenshot for manual verification
    await page.screenshot({
      path: path.join(__dirname, `test-screenshots`, `${frameName}.png`),
      fullPage: false
    });
  }

  console.log('\n' + '='.repeat(50));
  if (allValid) {
    console.log('✅ All frame SVGs are valid and contain visible content!');
  } else {
    console.log('⚠️  Some frame SVGs have issues. Check the details above.');
  }

  console.log('\n📸 Screenshots saved to test-screenshots/ directory');

  await browser.close();
})();