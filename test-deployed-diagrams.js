const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('TESTING DEPLOYED SITE DIAGRAMS');
  console.log('URL: https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');

  // Navigate to the introduction page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Check for diagram images
  const diagrams = await page.$$eval('div[data-testid="excalidraw-diagram"] img', elements =>
    elements.map(el => ({
      frameName: el.getAttribute('data-frame-name'),
      src: el.src,
      displayed: el.getBoundingClientRect().width > 0,
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight,
      complete: el.complete
    }))
  );

  console.log('\nDIAGRAM ANALYSIS:');
  diagrams.forEach((diagram, i) => {
    console.log(`\n${i + 1}. ${diagram.frameName}`);
    console.log(`   URL: ${diagram.src}`);
    console.log(`   Displayed: ${diagram.displayed}`);
    console.log(`   Loaded: ${diagram.complete}`);
    console.log(`   Size: ${diagram.naturalWidth}x${diagram.naturalHeight}`);
    if (diagram.naturalWidth === 0) {
      console.log('   WARNING: Image not found (404)');
    }
  });

  // Try to fetch one SVG directly
  if (diagrams.length > 0) {
    console.log('\nTESTING DIRECT SVG ACCESS:');
    const response = await page.goto(diagrams[0].src);
    if (response) {
      console.log(`Status: ${response.status()}`);
    }
  }

  await browser.close();
})();
