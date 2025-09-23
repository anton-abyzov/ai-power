const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const pages = [
    { url: 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction/', name: 'Introduction' },
    { url: 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/01-obsidian-setup/', name: 'Obsidian Setup' },
    { url: 'https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/02-ai-tools-landscape/', name: 'AI Tools' },
  ];

  console.log('🔍 VERIFYING DIAGRAMS ON ALL PAGES\n');

  for (const pageInfo of pages) {
    await page.goto(pageInfo.url);
    await page.waitForTimeout(2000);

    const images = await page.$$eval('img[src*="frames"]', elements => elements.map(el => ({
      src: el.src.split('/').pop(),
      visible: el.getBoundingClientRect().width > 0,
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight
    })));

    console.log(`📄 ${pageInfo.name}:`);
    if (images.length === 0) {
      console.log(`   No frame diagrams on this page`);
    } else {
      images.forEach(img => {
        const status = img.visible && img.naturalWidth > 0 ? '✅' : '❌';
        console.log(`   ${status} ${img.src} (${img.naturalWidth}x${img.naturalHeight})`);
      });
    }
  }

  console.log('\n✅ VERIFICATION COMPLETE');
  await browser.close();
})();