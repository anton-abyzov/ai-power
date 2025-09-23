const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('🔍 VERIFYING SVG CONTENT VISIBILITY\n');

  // Test a specific frame SVG directly
  await page.goto('file:///Users/antonabyzov/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/GitHubAIPower/episodes/01-portfolio-no-code/diagrams/frames/the-new-reality.svg');
  await page.waitForTimeout(2000);

  // Take screenshot of the SVG
  await page.screenshot({ path: 'svg-direct-view.png', fullPage: true });

  // Check SVG content
  const svgContent = await page.evaluate(() => {
    const svg = document.querySelector('svg');
    if (!svg) return { error: 'No SVG found' };

    // Count visible elements
    const allElements = svg.querySelectorAll('*');
    const visibleElements = Array.from(allElements).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });

    // Check for actual drawn content
    const paths = svg.querySelectorAll('path');
    const rects = svg.querySelectorAll('rect');
    const texts = svg.querySelectorAll('text');
    const images = svg.querySelectorAll('image');

    return {
      totalElements: allElements.length,
      visibleElements: visibleElements.length,
      paths: paths.length,
      rects: rects.length,
      texts: texts.length,
      images: images.length,
      viewBox: svg.getAttribute('viewBox'),
      width: svg.getAttribute('width'),
      height: svg.getAttribute('height')
    };
  });

  console.log('SVG CONTENT ANALYSIS:');
  console.log(svgContent);

  // Now test on the actual page
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(2000);

  const pageImages = await page.$$eval('img[src*="frames"]', elements => elements.map(el => {
    // Try to check if image appears blank
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.src = el.src;

    return {
      src: el.src.split('/').pop(),
      displayed: el.getBoundingClientRect().width > 0,
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight,
      complete: el.complete
    };
  }));

  console.log('\nIMAGES ON PAGE:');
  pageImages.forEach(img => {
    console.log(`  ${img.src}: ${img.displayed ? 'visible' : 'hidden'} (${img.naturalWidth}x${img.naturalHeight})`);
  });

  // Take screenshot of the page
  await page.screenshot({ path: 'page-with-svgs.png', fullPage: false });

  console.log('\n📸 Screenshots saved:');
  console.log('  - svg-direct-view.png (direct SVG view)');
  console.log('  - page-with-svgs.png (page with embedded SVGs)');

  console.log('\n⏰ Browser stays open for 15 seconds to inspect...');
  await page.waitForTimeout(15000);

  await browser.close();
})();