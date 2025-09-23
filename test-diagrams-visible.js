const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Checking if diagrams are now visible...');

  // Navigate to the introduction page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Check for img elements
  const imgElements = await page.$$eval('img[src*="all-diagrams"]', elements => elements.map(el => ({
    src: el.src,
    naturalWidth: el.naturalWidth,
    naturalHeight: el.naturalHeight,
    displayed: el.getBoundingClientRect().width > 0
  })));

  console.log('Diagram images found:');
  imgElements.forEach((img, i) => {
    console.log(`  Image ${i + 1}: ${img.displayed ? '✓' : '✗'} ${img.naturalWidth}x${img.naturalHeight} - ${img.src}`);
  });

  // Take screenshot
  await page.screenshot({ path: 'diagrams-check.png', fullPage: false });
  console.log('\nScreenshot saved as diagrams-check.png');

  console.log('\nBrowser will stay open for 10 seconds...');
  await page.waitForTimeout(10000);

  await browser.close();

  if (imgElements.length > 0 && imgElements.every(img => img.displayed)) {
    console.log('\n✅ SUCCESS: All diagrams are now visible!');
  } else if (imgElements.length > 0) {
    console.log('\n⚠️ WARNING: Some diagrams found but not all are displayed');
  } else {
    console.log('\n❌ FAILED: No diagram images found');
  }
})();