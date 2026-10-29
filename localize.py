"""把原站 index.html 翻成繁中：python3 localize.py 原檔 輸出檔
對照表 zh-tw.json 沒有的日文字串保持原樣，列在 missing.txt。"""
import json, os, re, sys

ORIGIN = 'https://ai-pose-gallery.pages.dev/'
JA = re.compile(r'[぀-ヿ㐀-鿿＀-￯　-〿]+'
                r'(?:[ A-Za-z0-9・ー\-/:()（）]*[぀-ヿ㐀-鿿＀-￯　-〿]+)*')
# JS 裡當欄位名用的日文，不能翻
IDENT = re.compile(r'(?<=[.{,])(?:系統|ポーズ番号|ポーズ名|分類|アングル|サムネ|原寸|番号|名)(?=[^぀-鿿])')
NOTE = ('<div style="background:#1a1e24;border-bottom:1px solid #343a44;color:#a3abb8;font-size:13px;'
        'padding:8px 16px;text-align:center">繁體中文翻譯版。原站：<a style="color:#8fb4ff" href="' + ORIGIN +
        '">' + ORIGIN + '</a>（作者 ギア）。介面與姿勢名稱翻成繁中，圖片一律從原站載入。'
        '<a style="color:#8fb4ff" href="https://github.com/yazelin/ai-pose-gallery-zh-tw">說明</a></div>')


def localize(s, tr):
    missing = set()

    def t(x):
        if x in tr:
            return tr[x]
        missing.add(x)
        return x

    i = s.index('[{"id"')
    j = s.index('}]', i) + 2
    data = json.loads(s[i:j])
    for d in data:
        for k in ('系統', '分類', 'ポーズ名', 'アングル'):
            if d.get(k):
                d[k] = t(d[k])
        for k in ('サムネ', '原寸'):  # ponytail: 條款禁止轉載圖片，只連回原站
            d[k] = ORIGIN + d[k]
    rest = s[:i] + '\0' + s[j:]
    # 欄位名先換成佔位符，翻完再換回來
    idents = []
    rest = IDENT.sub(lambda m: idents.append(m[0]) or f'\1{len(idents) - 1}\1', rest)
    rest = JA.sub(lambda m: t(m[0]), rest)
    rest = re.sub('\x01(\\d+)\x01', lambda m: idents[int(m[1])], rest)
    out = rest.replace('\0', json.dumps(data, ensure_ascii=False))
    out = out.replace('<html lang="ja">', '<html lang="zh-Hant">')
    out = out.replace("img-src 'self' data:", "img-src 'self' data: " + ORIGIN.rstrip('/'))
    out = re.sub(r"<script defer src='https://static\.cloudflareinsights\.com.*?</script>", '', out, flags=re.S)
    out = re.sub(r'(<body[^>]*>)', lambda m: m[1] + NOTE, out, count=1)
    return out, missing, data


if __name__ == '__main__':
    tr = json.load(open('zh-tw.json', encoding='utf-8'))
    out, missing, data = localize(open(sys.argv[1], encoding='utf-8').read(), tr)
    open(sys.argv[2], 'w', encoding='utf-8').write(out)
    # 給 AI 用的資料檔，放在輸出頁旁邊
    keys = {'id': 'id', '系統': 'series', 'ポーズ番号': 'pose_no', '分類': 'category', 'ポーズ名': 'name',
            'アングル': 'angle', 'サムネ': 'thumb', '原寸': 'image'}
    json.dump([{keys[k]: v for k, v in d.items()} for d in data], open(os.path.join(os.path.dirname(sys.argv[2]), 'poses.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=0)
    open('missing.txt', 'w', encoding='utf-8').write(''.join(m + '\n' for m in sorted(missing)))
    print(f'未翻 {len(missing)} 條')
