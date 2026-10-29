"""查姿勢參考圖（ai-pose-gallery 繁中版）：
  python3 pose.py search 關鍵字 [關鍵字...] [--angle 正面|從上方|從下方|側面|斜側] [--line 系列]
      列出符合的圖：id、系列、分類、姿勢名稱、角度、原尺寸圖網址
  python3 pose.py get <id> [<id>...] [-o 目錄]
      把原尺寸 PNG 下載到本機（預設 ./pose-refs/），給生圖工具當參考圖
圖片由原站提供，下載只供自己的作品參考，不要再散布（不要 commit 進公開 repo）。"""
import json, os, sys, urllib.request

DATA = os.environ.get('POSES_JSON', 'https://yazelin.github.io/ai-pose-gallery-zh-tw/poses.json')

# Cloudflare 會擋 Python 預設的 User-Agent
UA = 'Mozilla/5.0 (pose-reference skill; +https://github.com/yazelin/ai-pose-gallery-zh-tw)'


def poses():
    return json.load(urllib.request.urlopen(DATA, timeout=30))


def opt(args, name):
    if name in args:
        i = args.index(name)
        v = args[i + 1]
        del args[i:i + 2]
        return v


def search(args):
    angle, line = opt(args, '--angle'), opt(args, '--line')
    for d in poses():
        hay = ' '.join([d['id'], d['series'], d['category'], d['name'], d['pose_no']]).lower()
        if all(w.lower() in hay for w in args) and (not angle or d['angle'] == angle) and (not line or line in d['series']):
            print(f"{d['id']}  {d['series']}｜{d['category']}｜{d['name']}｜{d['angle']}  {d['image']}")


def get(args):
    out = opt(args, '-o') or 'pose-refs'
    os.makedirs(out, exist_ok=True)
    by = {d['id']: d for d in poses()}
    for i in args:
        if i not in by:
            sys.exit(f'找不到 id：{i}（先用 search 查）')
        path = os.path.join(out, i + '.png')
        req = urllib.request.Request(by[i]['image'], headers={'User-Agent': UA})
        open(path, 'wb').write(urllib.request.urlopen(req, timeout=60).read())
        print(path)


if __name__ == '__main__':
    cmd, rest = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ('', [])
    {'search': search, 'get': get}.get(cmd, lambda _: print(__doc__))(rest)
