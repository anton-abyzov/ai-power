const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 FINAL TEST - AI TOOLS DIAGRAM WITH ICONS\n');

  // Navigate to the AI Tools Landscape page
  const testUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/02-ai-tools-landscape/';
  console.log(`Testing: ${testUrl}\n`);

  await page.goto(testUrl, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(2000);

  // Check for the cost-comparison SVG
  const svgImages = await page.$$eval('img[src*="cost-comparison"]', elements =>
    elements.map(img => ({
      src: img.src,
      alt: img.alt,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      complete: img.complete,
      offsetWidth: img.offsetWidth,
      offsetHeight: img.offsetHeight
    }))
  );

  if (svgImages.length > 0) {
    console.log('✅ Found AI Tools Landscape diagram!\n');

    const img = svgImages[0];
    console.log('📊 Diagram Details:');
    console.log(`   Alt text: ${img.alt}`);
    console.log(`   Natural size: ${img.naturalWidth}x${img.naturalHeight}px`);
    console.log(`   Display size: ${img.offsetWidth}x${img.offsetHeight}px`);
    console.log(`   Loaded: ${img.complete ? 'Yes ✅' : 'No ❌'}\n`);

    // Check the actual file size
    const response = await page.goto(img.src, { waitUntil: 'networkidle' });
    const contentLength = response.headers()['content-length'];

    if (contentLength) {
      const sizeKB = (parseInt(contentLength) / 1024).toFixed(1);
      console.log(`📁 SVG File Details:`);
      console.log(`   File size: ${sizeKB} KB`);

      if (parseInt(contentLength) > 100000) { // More than 100KB
        console.log(`   ✅ Icons are embedded! (Large file size indicates embedded images)`);
      } else {
        console.log(`   ⚠️  File seems small for embedded icons`);
      }
    }

    // Go back to the content page
    await page.goto(testUrl);
    await page.waitForTimeout(1000);

    // Take a screenshot of the diagram
    const diagramImg = await page.$('img[src*="cost-comparison"]');
    if (diagramImg) {
      await diagramImg.scrollIntoViewIfNeeded();
      await page.waitForTimeout(500);

      // Take a full viewport screenshot
      await page.screenshot({
        path: 'test-final-ai-tools-diagram.png',
        fullPage: false
      });
      console.log('\n📸 Screenshot saved: test-final-ai-tools-diagram.png');

      // Also take a close-up of just the diagram
      const box = await diagramImg.boundingBox();
      if (box) {
        await page.screenshot({
          path: 'test-final-ai-tools-closeup.png',
          clip: {
            x: box.x,
            y: box.y,
            width: box.width,
            height: box.height
          }
        });
        console.log('📸 Close-up saved: test-final-ai-tools-closeup.png');
      }
    }
  } else {
    console.log('❌ AI Tools diagram not found on the page');

    // Check what's actually on the page
    const allImages = await page.$$eval('img', imgs => imgs.length);
    console.log(`\nFound ${allImages} total images on the page`);

    const frameImages = await page.$$eval('img[src*="frames"]', imgs =>
      imgs.map(img => img.src.split('/').pop())
    );
    if (frameImages.length > 0) {
      console.log('\nFound these frame images:');
      frameImages.forEach(name => console.log(`  - ${name}`));
    }
  }

  console.log('\n✅ FINAL TEST COMPLETE!\n');
  console.log('Direct link to AI Tools page:');
  console.log(`🔗 ${testUrl}\n`);

  await browser.close();
})();