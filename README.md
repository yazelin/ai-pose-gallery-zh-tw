# ai-pose-gallery-zh-tw（已搬家）

這個 repo 已改名為 [ai-reference-gallery-zh-tw](https://github.com/yazelin/ai-reference-gallery-zh-tw)，擴充成姿勢、depth 姿勢、服裝、臉部四個圖庫：<https://yazelin.github.io/ai-reference-gallery-zh-tw/>

這裡留著讓舊網址繼續能用：

- `https://yazelin.github.io/ai-pose-gallery-zh-tw/` 轉到新版的姿勢集。
- `poses.json` 每天從新版複製一份，所以舊版 `pose-reference` skill 照常可用。
- `skills/pose-reference/` 是舊版 skill，不再更新。請改裝新版的 `reference-gallery`：

```bash
git clone https://github.com/yazelin/ai-reference-gallery-zh-tw.git
ln -s "$PWD/ai-reference-gallery-zh-tw/skills/reference-gallery" ~/.claude/skills/reference-gallery
```
