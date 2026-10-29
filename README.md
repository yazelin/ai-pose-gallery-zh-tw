# ai-pose-gallery-zh-tw

AI 繪圖用姿勢參考圖庫「ポーズ集 POSE-DB-01」的繁體中文版，附上讓 AI 直接查詢、取用的 skill。

- 原站：<https://ai-pose-gallery.pages.dev/>
- 原作者：ギア（[X @giaaibusi](https://x.com/giaaibusi)）
- 繁中版網站：<https://yazelin.github.io/ai-pose-gallery-zh-tw/>

## 這個版本多了什麼

原站是給人瀏覽的網頁。這個版本保留同一個網頁並翻成繁中，另外提供 AI 能直接使用的入口：

| 入口 | 內容 |
|---|---|
| [`skills/pose-reference/`](skills/pose-reference/) | AI agent 的 skill。`SKILL.md` 寫明何時使用、怎麼搜尋、怎麼當參考圖、使用規範；`pose.py` 負責搜尋與下載，只用 Python 標準函式庫 |
| [`poses.json`](https://yazelin.github.io/ai-pose-gallery-zh-tw/poses.json) | 全部 1,439 張圖的資料：id、系列、姿勢編號、分類、繁中名稱、角度、縮圖與原尺寸圖網址 |
| [`llms.txt`](https://yazelin.github.io/ai-pose-gallery-zh-tw/llms.txt) | 給 AI 讀的網站簡介，指向上面兩項 |

### 給 AI 用

把 skill 裝進 agent 的 skill 目錄（Claude Code 為例）：

```bash
git clone https://github.com/yazelin/ai-pose-gallery-zh-tw.git
ln -s "$PWD/ai-pose-gallery-zh-tw/skills/pose-reference" ~/.claude/skills/pose-reference
```

其他 agent 直接讀 `skills/pose-reference/SKILL.md` 照著做即可。不想安裝的話，對 AI 說「讀 https://yazelin.github.io/ai-pose-gallery-zh-tw/llms.txt，幫我找一個跪坐回頭的姿勢參考」也可以。

```bash
python3 skills/pose-reference/pose.py search 跪立 後仰 --angle 側面
python3 skills/pose-reference/pose.py get full_sexy_P031_side -o pose-refs
```

## 和原站相比改了什麼

GitHub Actions 每天台灣時間 03:37 抓一次原站的 `index.html`，經 `localize.py` 處理後部署到 GitHub Pages：

1. 介面文字、系列、分類、姿勢名稱、角度從日文翻成繁體中文，對照表在 `zh-tw.json`。
2. 圖片沒有複製進來。縮圖、原尺寸圖、下載連結都指回原站，CSP 的 `img-src` 加上原站網域讓圖片載得到。原站注意事項禁止圖片本身的再散布與轉載，所以這個 repo 和 Pages 都不放任何圖片。
3. 移除原站的 Cloudflare Web Analytics beacon，避免把繁中版的流量算進原作者的統計。
4. 頁首加一行說明，註明原站與作者，並連到這個 repo。
5. 多產出 `poses.json` 和 `llms.txt`（見上一節）。

`html lang` 改成 `zh-Hant`。除此之外，版面、程式與功能都和原站相同。

### 原站新增姿勢時

對照表沒有的日文字串會保持日文顯示，並列在當次 Actions 執行的 Summary。補進 `zh-tw.json` 後 push，就會重新部署。

```bash
curl -fsSL https://ai-pose-gallery.pages.dev/ -o orig.html
python3 localize.py orig.html out.html   # 未翻譯的字串寫在 missing.txt
```

## 使用規範（摘譯自原站注意事項）

圖片可免費使用，作品製作中的商業使用、編輯與參考都可以，不必標註出處。禁止圖片本身（含原尺寸與加工後）的再散布、轉載與轉售。不得用於表現真實人物或未成年人，也不得用於違反公序良俗的用途。版權歸原作者所有。
