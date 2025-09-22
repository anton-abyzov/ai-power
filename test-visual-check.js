const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Visual check of deployed diagrams...');

  // Navigate to the introduction page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Scroll to see all diagrams
  await page.evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight / 3);
  });
  await page.waitForTimeout(1000);

  await page.evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight * 2 / 3);
  });
  await page.waitForTimeout(1000);

  // Check SVG dimensions and visibility
  const svgInfo = await page.$$eval('svg', elements => elements.map(el => {
    const rect = el.getBoundingClientRect();
    return {
      width: rect.width,
      height: rect.height,
      visible: rect.width > 0 && rect.height > 0,
      viewBox: el.getAttribute('viewBox')
    };
  }));

  console.log('SVG information:');
  svgInfo.forEach((info, i) => {
    console.log(`  SVG ${i + 1}: ${info.visible ? '✓' : '✗'} ${info.width}x${info.height}`);
  });

  // Take full page screenshot
  await page.screenshot({ path: 'visual-check-full.png', fullPage: true });
  console.log('\nFull page screenshot saved as visual-check-full.png');

  console.log('\nBrowser will stay open for 15 seconds for visual inspection...');
  console.log('Check that diagrams are properly aligned and scaled.');
  await page.waitForTimeout(15000);

  await browser.close();

  const allVisible = svgInfo.every(info => info.visible);
  if (allVisible) {
    console.log('\n✅ All SVG diagrams are visible and properly rendered!');
  } else {
    console.log('\n⚠️ Some SVGs may not be visible.');
  }
})();