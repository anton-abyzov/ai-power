const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const urls = [
    'https://anton-abyzov.github.io/ai-power/',
    'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/',
    'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/',
  ];

  for (const url of urls) {
    console.log(`\nTesting: ${url}`);
    await page.goto(url);
    await page.waitForTimeout(2000);

    // Get page title
    const title = await page.title();
    console.log(`Title: ${title}`);

    // Check for SVG elements
    const svgCount = await page.$$eval('svg', elements => elements.length);
    console.log(`SVG elements: ${svgCount}`);

    // Check for specific headers
    const headers = await page.$$eval('h1, h2', elements => elements.slice(0, 5).map(el => el.textContent));
    console.log(`Headers: ${headers.join(', ')}`);

    // Check for navigation links
    const navLinks = await page.$$eval('nav a', elements => elements.slice(0, 5).map(el => el.href));
    console.log(`Nav links: ${navLinks.slice(0, 3).join(', ')}`);
  }

  await browser.close();
})();