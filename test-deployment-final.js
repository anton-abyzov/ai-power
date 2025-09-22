const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('Testing deployment...');

  // Navigate to the page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');

  // Wait for content to load
  await page.waitForTimeout(3000);

  // Check for SVG elements
  const svgElements = await page.$$eval('svg', elements => elements.length);
  console.log(`Found ${svgElements} SVG elements`);

  // Check for image elements inside SVGs
  const svgImages = await page.$$eval('svg image', elements => elements.map(el => ({
    href: el.getAttribute('href'),
    displayed: el.getBoundingClientRect().width > 0
  })));
  console.log('SVG images:', JSON.stringify(svgImages, null, 2));

  // Check for the specific text that shouldn't be there
  const rawSyntax = await page.$eval('body', body => body.textContent.includes('![[episodes/'));
  console.log(`Raw Obsidian syntax present: ${rawSyntax}`);

  // Check for div containers with diagrams
  const diagramContainers = await page.$$eval('div[style*="padding-bottom"]', elements => elements.length);
  console.log(`Found ${diagramContainers} diagram containers`);

  // Take screenshot
  await page.screenshot({ path: 'deployment-final.png', fullPage: true });
  console.log('Screenshot saved as deployment-final.png');

  await browser.close();

  if (rawSyntax) {
    console.error('❌ FAILED: Raw Obsidian syntax still present!');
    process.exit(1);
  } else if (svgElements > 0 && svgImages.length > 0) {
    console.log('✅ SUCCESS: SVG diagrams are rendered!');
  } else {
    console.error('⚠️ WARNING: No SVG elements found, but no raw syntax either');
    console.log('This might be expected for some pages.');
  }
})();