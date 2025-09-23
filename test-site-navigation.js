const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🔍 TESTING SITE NAVIGATION AND DIAGRAMS\n');

  // Test the main episode page
  console.log('1. Testing Episode Overview Page...');
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/');
  await page.waitForTimeout(1000);

  // Check if diagrams are present on the overview page
  const overviewDiagrams = await page.$$eval('img[src*="frames"]', elements => elements.length);
  console.log(`   ✅ Found ${overviewDiagrams} diagram(s) on overview page`);

  // Check if the Start Learning Now button exists and works
  const startButton = await page.$('a[href*="content/00-introduction"]');
  if (startButton) {
    console.log('   ✅ "Start Learning Now" button found');
    await startButton.click();
    await page.waitForTimeout(1000);
    const url = page.url();
    if (url.includes('00-introduction')) {
      console.log('   ✅ Button navigation works - reached introduction page');
    } else {
      console.log('   ❌ Button navigation failed');
    }
  } else {
    console.log('   ❌ "Start Learning Now" button not found');
  }

  // Test the introduction page for diagrams
  console.log('\n2. Testing Introduction Page...');
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(1000);

  const introDiagrams = await page.$$eval('div[data-testid="excalidraw-diagram"] img', elements =>
    elements.map(el => ({
      name: el.getAttribute('data-frame-name'),
      src: el.src.split('/').pop(),
      loaded: el.complete
    }))
  );

  if (introDiagrams.length > 0) {
    console.log(`   ✅ Found ${introDiagrams.length} diagram(s):`);
    introDiagrams.forEach(d => {
      console.log(`      - ${d.name}: ${d.src} (${d.loaded ? 'loaded' : 'not loaded'})`);
    });
  } else {
    console.log('   ❌ No diagrams found on introduction page');
  }

  // Test community pages
  console.log('\n3. Testing Community Pages...');
  const communityPages = [
    { path: 'community/showcase/', name: 'Showcase' },
    { path: 'community/contributions/', name: 'Contributions' }
  ];

  for (const page_info of communityPages) {
    try {
      await page.goto(`http://127.0.0.1:8000/ai-power/${page_info.path}`);
      await page.waitForTimeout(500);
      const title = await page.title();
      console.log(`   ✅ ${page_info.name} page loads (title: ${title})`);
    } catch (error) {
      console.log(`   ❌ ${page_info.name} page failed: ${error.message}`);
    }
  }

  // Take screenshots for verification
  console.log('\n4. Taking screenshots...');
  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/');
  await page.screenshot({ path: 'test-episode-overview.png', fullPage: false });
  console.log('   📸 Episode overview: test-episode-overview.png');

  await page.goto('http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.screenshot({ path: 'test-introduction-page.png', fullPage: false });
  console.log('   📸 Introduction page: test-introduction-page.png');

  console.log('\n✅ TESTING COMPLETE');
  console.log('\nDirect links to test:');
  console.log('📍 Episode Overview: http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/');
  console.log('📍 Introduction: http://127.0.0.1:8000/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  console.log('📍 Community: http://127.0.0.1:8000/ai-power/community/showcase/');

  await browser.close();
})();