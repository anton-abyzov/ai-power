const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 TESTING FIXED DIAGRAM DEPLOYMENT\n');

  // Test the specific URL the user mentioned
  const testUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/#the-opportunity-100-120';
  console.log(`Testing: ${testUrl}\n`);

  await page.goto(testUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  // Check SVG images
  const imgElements = await page.$$eval('img[src*="frames"]', elements =>
    elements.map(img => ({
      src: img.src.split('/').pop(),
      alt: img.alt,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      complete: img.complete,
      displayWidth: img.offsetWidth,
      displayHeight: img.offsetHeight
    }))
  );

  console.log('📊 Frame SVG Analysis:\n');

  if (imgElements.length === 0) {
    console.log('❌ No frame SVGs found!');
  } else {
    let allLoaded = true;
    imgElements.forEach((img, index) => {
      console.log(`Frame ${index + 1}: ${img.alt}`);
      console.log(`  File: ${img.src}`);
      console.log(`  Natural size: ${img.naturalWidth}x${img.naturalHeight}px`);
      console.log(`  Display size: ${img.displayWidth}x${img.displayHeight}px`);

      if (img.naturalWidth === 0 || img.naturalHeight === 0) {
        console.log('  ❌ Image not loaded properly!');
        allLoaded = false;
      } else {
        console.log('  ✅ Loaded correctly');
      }
      console.log('');
    });

    if (allLoaded) {
      console.log('✅ ALL DIAGRAMS LOADING CORRECTLY!\n');
    } else {
      console.log('⚠️  Some diagrams failed to load\n');
    }
  }

  // Check network requests for SVG file sizes
  const svgResponses = [];
  page.on('response', response => {
    if (response.url().includes('/frames/') && response.url().endsWith('.svg')) {
      svgResponses.push({
        url: response.url().split('/').pop(),
        status: response.status(),
        size: response.headers()['content-length']
      });
    }
  });

  // Reload to capture network requests
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  if (svgResponses.length > 0) {
    console.log('📁 SVG File Sizes:');
    svgResponses.forEach(resp => {
      const sizeKB = resp.size ? (parseInt(resp.size) / 1024).toFixed(1) : 'Unknown';
      console.log(`  ${resp.url}: ${sizeKB} KB (Status: ${resp.status})`);
    });
    console.log('');
  }

  // Take screenshots
  console.log('📸 Taking screenshots...\n');

  // Full page screenshot
  await page.screenshot({ path: 'test-fixed-full-page.png', fullPage: false });
  console.log('Saved: test-fixed-full-page.png');

  // Scroll to and capture "The Opportunity" section specifically
  const opportunitySection = await page.$('h2:has-text("The Opportunity")');
  if (opportunitySection) {
    await opportunitySection.scrollIntoViewIfNeeded();
    await page.waitForTimeout(500);
    await page.screenshot({ path: 'test-fixed-opportunity.png', fullPage: false });
    console.log('Saved: test-fixed-opportunity.png (focused on The Opportunity section)');
  }

  console.log('\n✅ TEST COMPLETE!');
  console.log('\nDirect link to test:');
  console.log(`🔗 ${testUrl}\n`);

  await browser.close();
})();