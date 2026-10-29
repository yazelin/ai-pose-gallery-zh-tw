# ai-pose-gallery-zh-tw

AI 繪圖用姿勢參考圖庫「ポーズ集 POSE-DB-01」的繁體中文翻譯版。

- 原站：https://ai-pose-gallery.pages.dev/
- 原作者：ギア（https://x.com/giaaibusi）
- 翻譯版：https://yazelin.github.io/ai-pose-gallery-zh-tw/

## 我們改了什麼

GitHub Actions 每天台灣時間 03:37 抓一次原站的 `index.html`，經 `localize.py` 處理後部署到 GitHub Pages：

1. 介面文字、系列、分類、姿勢名稱、角度從日文翻成繁體中文，對照表在 `zh-tw.json`。
2. 圖片沒有複製進來。縮圖、原尺寸圖、下載連結都指回原站，CSP 的 `img-src` 加上原站網域讓圖片載得到。原站注意事項禁止圖片本身的再散布與轉載，所以這個 repo 和 Pages 都不放任何圖片。
3. 移除原站的 Cloudflare Web Analytics beacon，避免把翻譯版的流量算進原作者的統計。
4. 頁首加一行說明，註明原站與作者，並連到這個 repo。

`html lang` 改成 `zh-Hant`。除此之外，版面、程式與功能都和原站相同。

## 原站新增姿勢時

對照表沒有的日文字串會保持日文顯示，並列在當次 Actions 執行的 Summary。補進 `zh-tw.json` 後 push，就會重新部署。

本機試跑：

```
curl -fsSL https://ai-pose-gallery.pages.dev/ -o orig.html
python3 localize.py orig.html out.html   # 未翻譯的字串寫在 missing.txt
```

## 使用規範（摘譯自原站注意事項）

圖片可免費使用，作品製作中的商業使用、編輯與參考都可以。禁止圖片本身（含原尺寸與加工後）的再散布、轉載與轉售。不得用於表現真實人物或未成年人，也不得用於違反公序良俗的用途。版權歸原作者所有。
