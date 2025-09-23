const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 DEBUGGING DEPLOYED SITE DIAGRAM ISSUES\n');

  // Enable console logging from the page
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log('   ❌ Console Error:', msg.text());
    }
  });

  // Monitor network requests
  const failedRequests = [];
  const successfulImages = [];

  page.on('requestfailed', request => {
    if (request.url().includes('.svg')) {
      failedRequests.push({
        url: request.url(),
        failure: request.failure().errorText
      });
    }
  });

  page.on('response', response => {
    if (response.url().includes('.svg')) {
      console.log(`   📡 SVG Request: ${response.url()}`);
      console.log(`      Status: ${response.status()} ${response.statusText()}`);
      if (response.status() === 200) {
        successfulImages.push(response.url());
      } else {
        failedRequests.push({
          url: response.url(),
          status: response.status()
        });
      }
    }
  });

  // Test the specific URL the user mentioned
  console.log('1. Testing the specific page with diagrams...');
  const testUrl = 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/#the-opportunity-100-120';
  console.log(`   URL: ${testUrl}\n`);

  await page.goto(testUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  // Get the actual HTML for img elements
  console.log('2. Analyzing IMG elements in the page...');
  const imgElements = await page.$$eval('img[src*="svg"]', elements =>
    elements.map(img => ({
      src: img.src,
      alt: img.alt,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      complete: img.complete,
      currentSrc: img.currentSrc,
      computedDisplay: window.getComputedStyle(img).display,
      computedVisibility: window.getComputedStyle(img).visibility,
      offsetWidth: img.offsetWidth,
      offsetHeight: img.offsetHeight,
      parentDisplay: img.parentElement ? window.getComputedStyle(img.parentElement).display : 'N/A'
    }))
  );

  if (imgElements.length === 0) {
    console.log('   ❌ No SVG images found in the page!');

    // Check if there are any divs with data-testid="excalidraw-diagram"
    const diagramDivs = await page.$$eval('div[data-testid="excalidraw-diagram"]', elements =>
      elements.map(div => ({
        innerHTML: div.innerHTML.substring(0, 200),
        childCount: div.children.length,
        hasImg: div.querySelector('img') !== null
      }))
    );

    if (diagramDivs.length > 0) {
      console.log(`   Found ${diagramDivs.length} diagram container(s):`);
      diagramDivs.forEach((div, i) => {
        console.log(`   Container ${i + 1}:`);
        console.log(`      Has IMG: ${div.hasImg}`);
        console.log(`      Children: ${div.childCount}`);
        console.log(`      HTML preview: ${div.innerHTML}`);
      });
    } else {
      console.log('   ❌ No diagram containers found either!');
    }
  } else {
    console.log(`   Found ${imgElements.length} SVG image(s):\n`);
    imgElements.forEach((img, index) => {
      console.log(`   Image ${index + 1}:`);
      console.log(`      Alt: ${img.alt}`);
      console.log(`      Src: ${img.src}`);
      console.log(`      Current Src: ${img.currentSrc}`);
      console.log(`      Loaded: ${img.complete}`);
      console.log(`      Natural Size: ${img.naturalWidth}x${img.naturalHeight}`);
      console.log(`      Display Size: ${img.offsetWidth}x${img.offsetHeight}`);
      console.log(`      CSS Display: ${img.computedDisplay}`);
      console.log(`      CSS Visibility: ${img.computedVisibility}`);
      console.log(`      Parent Display: ${img.parentDisplay}`);

      if (img.naturalWidth === 0 || img.naturalHeight === 0) {
        console.log(`      ⚠️  Image appears to be broken or not loaded!`);
      }
      console.log('');
    });
  }

  // Check the actual page source to see what HTML is being served
  console.log('3. Checking raw HTML source...');
  const pageContent = await page.content();

  // Look for diagram sections
  const diagramSections = ['The New Reality', 'The Opportunity', 'What You\'ll Build'];
  for (const section of diagramSections) {
    const index = pageContent.indexOf(section);
    if (index !== -1) {
      console.log(`\n   Found section: "${section}"`);
      // Extract a snippet around this section
      const snippet = pageContent.substring(Math.max(0, index - 100), Math.min(pageContent.length, index + 500));
      // Check if there's an img tag nearby
      if (snippet.includes('<img')) {
        console.log('      ✓ Has <img> tag');
        const imgMatch = snippet.match(/<img[^>]*src="([^"]*)"[^>]*>/);
        if (imgMatch) {
          console.log(`      Image src: ${imgMatch[1]}`);
        }
      } else {
        console.log('      ❌ No <img> tag found near this section');
      }
    }
  }

  // Report on failed requests
  if (failedRequests.length > 0) {
    console.log('\n4. Failed SVG Requests:');
    failedRequests.forEach(req => {
      console.log(`   ❌ ${req.url}`);
      if (req.failure) console.log(`      Error: ${req.failure}`);
      if (req.status) console.log(`      Status: ${req.status}`);
    });
  } else {
    console.log('\n4. No failed SVG requests');
  }

  // Test if we can directly access the SVG files
  console.log('\n5. Testing direct access to SVG files...');
  const svgPaths = [
    'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/diagrams/frames/the-new-reality.svg',
    'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/diagrams/frames/the-opportunity.svg',
    'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/diagrams/frames/what-youll-build.svg'
  ];

  for (const svgPath of svgPaths) {
    try {
      const response = await page.goto(svgPath);
      const filename = svgPath.split('/').pop();
      if (response && response.ok()) {
        const contentLength = response.headers()['content-length'];
        console.log(`   ✅ ${filename}: Status ${response.status()} (${contentLength || 'N/A'} bytes)`);
      } else {
        console.log(`   ❌ ${filename}: Status ${response ? response.status() : 'No response'}`);
      }
      // Go back to the main page for next test
      await page.goto(testUrl, { waitUntil: 'networkidle' });
    } catch (error) {
      console.log(`   ❌ ${svgPath.split('/').pop()}: ${error.message}`);
    }
  }

  // Take a screenshot
  console.log('\n6. Taking screenshot...');
  await page.screenshot({ path: 'debug-deployed-site.png', fullPage: false });
  console.log('   📸 Screenshot saved: debug-deployed-site.png');

  console.log('\n✅ DEBUGGING COMPLETE');

  await browser.close();
})();