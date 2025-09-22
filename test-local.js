const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Testing local deployment...');

  // Navigate to the local page
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');

  // Wait for content to load
  await page.waitForLoadState('networkidle');

  // Check for SVG elements
  const svgElements = await page.$$eval('svg', elements => elements.length);
  console.log(`Found ${svgElements} SVG elements`);

  // Check for image elements inside SVGs
  const svgImages = await page.$$eval('svg image', elements => elements.map(el => ({
    href: el.getAttribute('href'),
    x: el.getAttribute('x'),
    y: el.getAttribute('y')
  })));
  console.log('SVG images:', svgImages);

  // Check for the specific text that shouldn't be there
  const rawSyntax = await page.$eval('body', body => body.textContent.includes('![[episodes/'));
  console.log(`Raw Obsidian syntax present: ${rawSyntax}`);

  // Get the actual HTML content where diagrams should be
  const diagramSections = await page.$$eval('h2', headers => {
    const results = [];
    headers.forEach(h2 => {
      if (h2.textContent.includes('The New Reality')) {
        const nextElement = h2.nextElementSibling;
        if (nextElement) {
          results.push({
            header: h2.textContent,
            nextHTML: nextElement.outerHTML.substring(0, 200)
          });
        }
      }
    });
    return results;
  });
  console.log('Diagram sections:', diagramSections);

  // Take screenshot
  await page.screenshot({ path: 'local-test.png', fullPage: false });
  console.log('Screenshot saved as local-test.png');

  // Keep browser open for manual inspection
  console.log('Browser will stay open for 30 seconds for manual inspection...');
  await page.waitForTimeout(30000);

  await browser.close();

  if (rawSyntax) {
    console.error('❌ FAILED: Raw Obsidian syntax still present!');
    process.exit(1);
  } else if (svgElements > 0) {
    console.log(`✅ SUCCESS: ${svgElements} SVG diagrams are rendered!`);
  } else {
    console.error('❌ FAILED: No SVG elements found!');
    process.exit(1);
  }
})();