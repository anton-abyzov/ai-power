const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Testing DEPLOYED diagrams...\n');

  // Navigate to deployed site
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  // Check for images
  const deployedImages = await page.$$eval('img', elements => elements.map(el => {
    const rect = el.getBoundingClientRect();
    return {
      src: el.src,
      displayed: rect.width > 0 && rect.height > 0,
      width: Math.round(rect.width),
      height: Math.round(rect.height),
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight,
      complete: el.complete,
      error: el.onerror !== null
    };
  }));

  console.log('DEPLOYED IMAGES:');
  if (deployedImages.length === 0) {
    console.log('  ❌ No images found on deployed site!');
  } else {
    deployedImages.forEach((img, i) => {
      const filename = img.src.split('/').pop();
      console.log(`  ${i+1}. ${filename}`);
      console.log(`     URL: ${img.src}`);
      console.log(`     Loaded: ${img.complete ? '✓' : '✗'} | Visible: ${img.displayed ? '✓' : '✗'}`);
      console.log(`     Display: ${img.width}x${img.height} | Natural: ${img.naturalWidth}x${img.naturalHeight}`);
    });
  }

  // Check console errors
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });

  // Check network errors
  const failedRequests = [];
  page.on('requestfailed', request => {
    failedRequests.push({
      url: request.url(),
      error: request.failure().errorText
    });
  });

  // Reload to catch errors
  await page.reload();
  await page.waitForTimeout(2000);

  if (consoleErrors.length > 0) {
    console.log('\n❌ CONSOLE ERRORS:');
    consoleErrors.forEach(err => console.log(`  - ${err}`));
  }

  if (failedRequests.length > 0) {
    console.log('\n❌ FAILED REQUESTS:');
    failedRequests.forEach(req => console.log(`  - ${req.url}: ${req.error}`));
  }

  // Check actual HTML content
  const htmlContent = await page.$eval('body', body => {
    const intro = body.querySelector('h2#the-new-reality-035-100');
    if (intro) {
      const next = intro.nextElementSibling;
      return next ? next.outerHTML.substring(0, 500) : 'No next element';
    }
    return 'Section not found';
  });

  console.log('\n📄 HTML Content after "The New Reality":');
  console.log(htmlContent);

  // Take screenshot
  await page.screenshot({ path: 'deployed-diagrams-test.png', fullPage: false });
  console.log('\n📸 Screenshot saved as deployed-diagrams-test.png');

  console.log('⏰ Browser stays open for 10 seconds...');
  await page.waitForTimeout(10000);

  await browser.close();
})();