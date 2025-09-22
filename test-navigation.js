const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Testing navigation to diagrams...');

  // Go to main page
  await page.goto('https://anton-abyzov.github.io/ai-power/');
  await page.waitForTimeout(2000);

  // Try to navigate through the menu
  console.log('Looking for Episode 01 link...');

  // Click on Episode 01 if it exists
  const episode01Link = await page.$('a:has-text("Episode 01")');
  if (episode01Link) {
    console.log('Found Episode 01 link, clicking...');
    await episode01Link.click();
    await page.waitForTimeout(2000);
  }

  // Look for introduction link
  const introLink = await page.$('a:has-text("Introduction")');
  if (introLink) {
    console.log('Found Introduction link, clicking...');
    await introLink.click();
    await page.waitForTimeout(2000);
  }

  // Get current URL
  const currentUrl = page.url();
  console.log(`Current URL: ${currentUrl}`);

  // Check for SVG elements
  const svgElements = await page.$$eval('svg', elements => elements.length);
  console.log(`Found ${svgElements} SVG elements`);

  // Check for diagram containers
  const diagramContainers = await page.$$eval('div[style*="padding-bottom"]', elements => elements.length);
  console.log(`Found ${diagramContainers} diagram containers`);

  // Take screenshot
  await page.screenshot({ path: 'navigation-test.png', fullPage: false });
  console.log('Screenshot saved as navigation-test.png');

  console.log('Browser will stay open for 20 seconds for manual inspection...');
  await page.waitForTimeout(20000);

  await browser.close();
})();