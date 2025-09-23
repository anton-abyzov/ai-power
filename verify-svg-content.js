const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 VERIFYING FULL DIAGRAM SOLUTION\n');

  // Test the full diagram SVG directly
  await page.goto('file:///Users/antonabyzov/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/GitHubAIPower/docs/episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.light.svg');
  await page.waitForTimeout(2000);

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

  console.log('✅ FULL DIAGRAM SVG CONTENT:');
  console.log(`  Total elements: ${svgContent.totalElements}`);
  console.log(`  Visible elements: ${svgContent.visibleElements}`);
  console.log(`  Paths: ${svgContent.paths}`);
  console.log(`  Rectangles: ${svgContent.rects}`);
  console.log(`  Text elements: ${svgContent.texts}`);
  console.log(`  ViewBox: ${svgContent.viewBox}`);

  // Skip screenshot of the huge SVG to avoid timeout
  console.log('  (Skipping SVG screenshot - too large)');

  // Now test on the actual page with full diagram embeds
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(2000);

  // Check for our converted diagram embeds with data-testid
  const diagramDivs = await page.$$eval('div[data-testid="excalidraw-diagram"]', elements =>
    elements.map(el => {
      const img = el.querySelector('img');
      return {
        frameId: img?.getAttribute('data-frame-id'),
        frameName: img?.getAttribute('data-frame-name'),
        src: img?.src?.split('/').pop(),
        displayed: img?.getBoundingClientRect().width > 0,
        naturalWidth: img?.naturalWidth,
        naturalHeight: img?.naturalHeight,
        complete: img?.complete
      };
    })
  );

  console.log('\n📊 DIAGRAMS ON PAGE:');
  if (diagramDivs.length === 0) {
    console.log('  ❌ No diagrams found with data-testid="excalidraw-diagram"');
  } else {
    diagramDivs.forEach(diagram => {
      const status = diagram.displayed ? '✅' : '❌';
      console.log(`  ${status} ${diagram.frameName} (${diagram.frameId})`);
      console.log(`     Source: ${diagram.src}`);
      console.log(`     Size: ${diagram.naturalWidth}x${diagram.naturalHeight}`);
      console.log(`     Loaded: ${diagram.complete}`);
    });
  }

  // Take screenshot of the page (viewport only to avoid timeout)
  await page.screenshot({ path: 'page-with-full-diagrams.png', fullPage: false });

  console.log('\n📸 Screenshots saved:');
  console.log('  - page-with-full-diagrams.png (page with embedded diagrams)');

  console.log('\n✨ VERIFICATION COMPLETE');

  await browser.close();
})();