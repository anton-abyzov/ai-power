const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('Testing LOCAL diagrams rendering...\n');

  // Test localhost first
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(2000);

  // Check for images with frame SVGs
  const localImages = await page.$$eval('img[src*="frames"]', elements => elements.map(el => {
    const rect = el.getBoundingClientRect();
    return {
      src: el.src,
      alt: el.alt,
      displayed: rect.width > 0 && rect.height > 0,
      width: Math.round(rect.width),
      height: Math.round(rect.height),
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight,
      complete: el.complete,
      currentSrc: el.currentSrc
    };
  }));

  console.log('LOCAL IMAGES:');
  if (localImages.length === 0) {
    console.log('  ❌ No frame images found on local!');
  } else {
    localImages.forEach((img, i) => {
      console.log(`  ${i+1}. ${img.src.split('/').pop()}`);
      console.log(`     Loaded: ${img.complete ? '✓' : '✗'} | Visible: ${img.displayed ? '✓' : '✗'}`);
      console.log(`     Display: ${img.width}x${img.height} | Natural: ${img.naturalWidth}x${img.naturalHeight}`);
    });
  }

  // Check all img elements
  const allImages = await page.$$eval('img', elements => elements.map(el => ({
    src: el.src.substring(el.src.lastIndexOf('/') + 1),
    displayed: el.getBoundingClientRect().width > 0
  })));

  console.log('\n  ALL IMAGES ON PAGE:', allImages.length);
  allImages.forEach(img => {
    console.log(`    - ${img.src.substring(0, 40)} ${img.displayed ? '(visible)' : '(hidden)'}`);
  });

  // Check the actual HTML
  const htmlSnippet = await page.$eval('h2:has-text("The New Reality")', el => {
    const next = el.nextElementSibling;
    return next ? next.innerHTML.substring(0, 300) : 'No element after h2';
  });

  console.log('\n  HTML after "The New Reality" heading:');
  console.log('    ' + htmlSnippet);

  // Take screenshot
  await page.screenshot({ path: 'local-diagrams-test.png', fullPage: false });

  console.log('\n📸 Screenshot saved as local-diagrams-test.png');
  console.log('⏰ Browser stays open for 10 seconds...');

  await page.waitForTimeout(10000);
  await browser.close();
})();