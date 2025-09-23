const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 TESTING ICON DISPLAY IN DIAGRAMS\n');

  // Navigate to a page that should have the AI tools diagram
  const testUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/10-ai-tools-landscape/';
  console.log(`Testing: ${testUrl}\n`);

  try {
    await page.goto(testUrl, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(2000);
  } catch (e) {
    console.log('Page might not exist yet, trying main introduction page...\n');
    // Try the introduction page instead
    const altUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/';
    await page.goto(altUrl, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);
  }

  // Look for SVG images with frames
  const svgImages = await page.$$eval('img[src*="frames"]', elements =>
    elements.map(img => ({
      src: img.src.split('/').pop(),
      alt: img.alt,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      complete: img.complete
    }))
  );

  console.log(`Found ${svgImages.length} frame SVG(s) on the page\n`);

  // Check if any of them is the cost-comparison (AI tools) frame
  const aiToolsFrame = svgImages.find(img => img.src.includes('cost-comparison'));

  if (aiToolsFrame) {
    console.log('✅ Found AI Development Tools Landscape diagram (cost-comparison.svg)');
    console.log(`   Size: ${aiToolsFrame.naturalWidth}x${aiToolsFrame.naturalHeight}px`);
    console.log(`   Loaded: ${aiToolsFrame.complete ? 'Yes' : 'No'}\n`);
  } else {
    console.log('⚠️  AI tools diagram (cost-comparison.svg) not found on this page\n');
  }

  // Try to find the actual cost comparison page
  console.log('Searching for pages with the AI tools diagram...\n');

  // Check the episode overview page
  const overviewUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/';
  await page.goto(overviewUrl, { waitUntil: 'networkidle' });

  const overviewImages = await page.$$eval('img[src*="cost-comparison"]', elements =>
    elements.map(img => ({
      src: img.src,
      loaded: img.complete,
      width: img.naturalWidth,
      height: img.naturalHeight
    }))
  );

  if (overviewImages.length > 0) {
    console.log(`✅ Found cost-comparison diagram on overview page!`);
    console.log(`   URL: ${overviewUrl}`);
    const img = overviewImages[0];
    console.log(`   Image size: ${img.width}x${img.height}px`);
    console.log(`   Loaded: ${img.loaded ? 'Yes' : 'No'}\n`);

    // Check if we can detect the presence of embedded images in the SVG
    // by checking the response size
    const response = await page.goto(img.src);
    const contentLength = response.headers()['content-length'];
    const sizeKB = contentLength ? (parseInt(contentLength) / 1024).toFixed(1) : 'Unknown';
    console.log(`   SVG file size: ${sizeKB} KB`);

    if (parseInt(contentLength) > 100000) { // More than 100KB means it likely has embedded images
      console.log('   ✅ File size indicates embedded images are included!\n');
    } else {
      console.log('   ⚠️  File size seems small, images might not be embedded\n');
    }

    // Take a screenshot of the diagram
    await page.goto(overviewUrl);
    await page.waitForTimeout(1000);

    const costComparisonImg = await page.$('img[src*="cost-comparison"]');
    if (costComparisonImg) {
      await costComparisonImg.scrollIntoViewIfNeeded();
      await page.waitForTimeout(500);
      await page.screenshot({
        path: 'test-ai-tools-diagram.png',
        fullPage: false
      });
      console.log('📸 Screenshot saved: test-ai-tools-diagram.png\n');
    }
  } else {
    console.log('❌ Could not find cost-comparison diagram\n');
  }

  console.log('✅ TEST COMPLETE!\n');

  await browser.close();
})();