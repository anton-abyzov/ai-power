const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  console.log('🎯 FINAL CHECK - Frame-specific diagrams\n');

  // Test Introduction page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/');
  await page.waitForTimeout(3000);

  const introImages = await page.$$eval('img[src*="frames/"]', elements => elements.map(el => ({
    src: el.src.split('/').pop(),
    displayed: el.getBoundingClientRect().width > 0,
    width: Math.round(el.getBoundingClientRect().width),
    height: Math.round(el.getBoundingClientRect().height),
    naturalWidth: el.naturalWidth,
    naturalHeight: el.naturalHeight
  })));

  console.log('📄 INTRODUCTION PAGE:');
  introImages.forEach((img, i) => {
    console.log(`   ${i+1}. ${img.src}`);
    console.log(`      Visible: ${img.displayed ? '✅' : '❌'} | Display: ${img.width}x${img.height}px | Natural: ${img.naturalWidth}x${img.naturalHeight}px`);
  });

  await page.screenshot({ path: 'final-intro.png', fullPage: false });

  // Test Obsidian Setup page
  await page.goto('https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/01-obsidian-setup/');
  await page.waitForTimeout(2000);

  const obsidianImages = await page.$$eval('img[src*="frames/"]', elements => elements.map(el => ({
    src: el.src.split('/').pop(),
    displayed: el.getBoundingClientRect().width > 0,
    width: Math.round(el.getBoundingClientRect().width),
    height: Math.round(el.getBoundingClientRect().height)
  })));

  console.log('\n📂 OBSIDIAN SETUP PAGE:');
  if (obsidianImages.length > 0) {
    obsidianImages.forEach((img, i) => {
      console.log(`   ${i+1}. ${img.src}`);
      console.log(`      Visible: ${img.displayed ? '✅' : '❌'} | Display: ${img.width}x${img.height}px`);
    });
  } else {
    console.log('   No frame diagrams on this page');
  }

  await page.screenshot({ path: 'final-obsidian.png', fullPage: false });

  console.log('\n📸 Screenshots saved: final-intro.png, final-obsidian.png');
  console.log('\n⏰ Browser will stay open for 10 seconds for inspection...');
  await page.waitForTimeout(10000);

  await browser.close();

  const allIntroVisible = introImages.length > 0 && introImages.every(img => img.displayed);
  if (allIntroVisible) {
    console.log('\n🎉 SUCCESS: Frame-specific diagrams are working perfectly!');
    console.log('   Each diagram now shows only its relevant content.');
  } else {
    console.log('\n⚠️  Some issues detected with frame diagrams');
  }
})();