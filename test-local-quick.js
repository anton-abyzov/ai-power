const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('Testing local deployment...');

  // Navigate to the local page
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');

  // Wait for content to load
  await page.waitForTimeout(2000);

  // Check for SVG elements
  const svgElements = await page.$$eval('svg', elements => elements.length);
  console.log(`Found ${svgElements} SVG elements`);

  // Check for image elements inside SVGs and their resolved URLs
  const svgImages = await page.$$eval('svg image', elements => elements.map(el => {
    const href = el.getAttribute('href');
    const resolvedHref = el.href ? el.href.baseVal : href;
    return {
      href: href,
      resolved: resolvedHref,
      displayed: el.getBoundingClientRect().width > 0
    };
  }));
  console.log('SVG images:', JSON.stringify(svgImages, null, 2));

  // Check if images are loading
  const imageLoadStatus = await Promise.all(
    svgImages.map(async (img, index) => {
      if (img.resolved && img.resolved.startsWith('http')) {
        try {
          const response = await page.request.get(img.resolved);
          return { index, status: response.status() };
        } catch (e) {
          return { index, error: e.message };
        }
      }
      return { index, note: 'Not HTTP URL' };
    })
  );
  console.log('Image load status:', imageLoadStatus);

  // Check for the specific text that shouldn't be there
  const rawSyntax = await page.$eval('body', body => body.textContent.includes('![[episodes/'));
  console.log(`Raw Obsidian syntax present: ${rawSyntax}`);

  // Take screenshot
  await page.screenshot({ path: 'local-test.png', fullPage: false });
  console.log('Screenshot saved as local-test.png');

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