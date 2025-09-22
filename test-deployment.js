const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  console.log('Testing deployment...');

  // Navigate to the page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');

  // Wait for content to load
  await page.waitForLoadState('networkidle');

  // Check for SVG elements
  const svgElements = await page.$$eval('svg', elements => elements.length);
  console.log(`Found ${svgElements} SVG elements`);

  // Check for the specific text that shouldn't be there
  const rawSyntax = await page.$eval('body', body => body.textContent.includes('![[episodes/'));
  console.log(`Raw Obsidian syntax present: ${rawSyntax}`);

  // Get the actual HTML content
  const diagramSection = await page.$eval('h2:has-text("The New Reality") + *', el => el.outerHTML);
  console.log('Diagram HTML:', diagramSection.substring(0, 200) + '...');

  // Take screenshot
  await page.screenshot({ path: 'deployment-test.png', fullPage: false });
  console.log('Screenshot saved as deployment-test.png');

  await browser.close();

  if (rawSyntax) {
    console.error('❌ FAILED: Raw Obsidian syntax still present!');
    process.exit(1);
  } else if (svgElements > 0) {
    console.log('✅ SUCCESS: SVG diagrams are rendered!');
  } else {
    console.error('❌ FAILED: No SVG elements found!');
    process.exit(1);
  }
})();