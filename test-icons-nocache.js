const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    // Disable cache
    bypassCSP: true,
    ignoreHTTPSErrors: true,
    extraHTTPHeaders: {
      'Cache-Control': 'no-cache, no-store, must-revalidate',
      'Pragma': 'no-cache'
    }
  });
  const page = await context.newPage();

  console.log('🔍 TESTING ICONS WITH CACHE BYPASS\n');

  // Direct URL to the cost-comparison SVG with cache buster
  const timestamp = Date.now();
  const svgUrl = `https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/diagrams/frames/cost-comparison.svg?t=${timestamp}`;

  console.log(`Testing direct SVG URL: ${svgUrl}\n`);

  try {
    const response = await page.goto(svgUrl, {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    if (response) {
      const status = response.status();
      const contentLength = response.headers()['content-length'];
      const contentType = response.headers()['content-type'];

      console.log(`Response Status: ${status}`);
      console.log(`Content-Type: ${contentType}`);

      if (contentLength) {
        const sizeKB = (parseInt(contentLength) / 1024).toFixed(1);
        const sizeMB = (parseInt(contentLength) / (1024 * 1024)).toFixed(2);
        console.log(`File Size: ${sizeKB} KB (${sizeMB} MB)`);

        if (parseInt(contentLength) > 100000) {
          console.log('✅ File size indicates embedded images are included!');
        } else {
          console.log('⚠️  File size seems small, images might not be embedded');
        }
      } else {
        console.log('File Size: Unknown');
      }
    }
  } catch (error) {
    console.log(`Error loading SVG: ${error.message}`);
  }

  console.log('\n📊 Checking if SVG contains image data...\n');

  // Load the SVG content and check for embedded images
  const svgContent = await page.content();

  // Check for data URLs (base64 encoded images)
  const hasDataUrls = svgContent.includes('data:image');
  const imageCount = (svgContent.match(/<image/g) || []).length;

  console.log(`Contains data URLs: ${hasDataUrls ? 'Yes ✅' : 'No ❌'}`);
  console.log(`Number of <image> elements: ${imageCount}`);

  if (hasDataUrls) {
    // Count how many data URLs
    const dataUrlCount = (svgContent.match(/data:image/g) || []).length;
    console.log(`Number of embedded images: ${dataUrlCount}`);
  }

  // Now check the main page
  console.log('\n🌐 Testing main episode page...\n');

  const mainUrl = `https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/?t=${timestamp}`;
  await page.goto(mainUrl, { waitUntil: 'networkidle' });

  const images = await page.$$eval('img[src*="cost-comparison"]', imgs =>
    imgs.map(img => ({
      src: img.src,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      complete: img.complete
    }))
  );

  if (images.length > 0) {
    console.log(`Found ${images.length} cost-comparison image(s) on the page`);
    images.forEach((img, i) => {
      console.log(`\nImage ${i + 1}:`);
      console.log(`  URL: ${img.src}`);
      console.log(`  Dimensions: ${img.naturalWidth}x${img.naturalHeight}px`);
      console.log(`  Loaded: ${img.complete ? 'Yes' : 'No'}`);
    });

    // Take a screenshot
    const firstImg = await page.$('img[src*="cost-comparison"]');
    if (firstImg) {
      await firstImg.scrollIntoViewIfNeeded();
      await page.waitForTimeout(500);
      await page.screenshot({
        path: 'test-icons-nocache.png',
        fullPage: false
      });
      console.log('\n📸 Screenshot saved: test-icons-nocache.png');
    }
  } else {
    console.log('No cost-comparison images found on the page');
  }

  console.log('\n✅ TEST COMPLETE!\n');

  await browser.close();
})();