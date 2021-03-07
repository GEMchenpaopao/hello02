"""
百度翻译破解案例（js逆向解析）
"""
import requests
import execjs

class BDSpider:
    def __init__(self):
        self.post_url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.post_headers={
            '''Accept''': '''*/*''',
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''zh-CN,zh;q=0.9''',
            '''Cache-Control''': '''no-cache''',
            '''Connection''': '''keep-alive''',
            '''Content-Length''': '''135''',
            '''Content-Type''': '''application/x-www-form-urlencoded; charset=UTF-8''',
            '''Cookie''': '''BAIDUID=0494F8D75D1CD5904AF3A75D4D08C005:FG=1; BIDUPSID=0494F8D75D1CD5904AF3A75D4D08C005; PSTM=1612487124; __yjs_duid=1_c76ee7c33d5e318a634f44bad000d50a1612489451736; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1612596225; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1612609073; __yjsv5_shitong=1.0_7_60888d0e5b72f3308071f120acc7695d3466_300_1612609073737_125.119.209.119_7e639f14; ab_sr=1.0.0_OGYwZTdhZWI5NzI4MTg4ZTZhM2I5MDRhOTE3ZGI0OWVjMWEyOWU0MmZhYjBjYWJjODk3NThjNDc5ZWNiNmY4ZjJjZjU1NzNlYzMxNmVkYzRjNDYxMTNmNGU5M2ZkYmQ5''',
            '''Host''': '''fanyi.baidu.com''',
            '''Origin''': '''https://fanyi.baidu.com''',
            '''Pragma''': '''no-cache''',
            '''Referer''': '''https://fanyi.baidu.com/''',
            '''Sec-Fetch-Dest''': '''empty''',
            '''Sec-Fetch-Mode''': '''cors''',
            '''Sec-Fetch-Site''': '''same-origin''',
            '''User-Agent''': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36''',
            '''X-Requested-With''': '''XMLHttpRequest''',
            }
        self.word = input('请输入要翻译的单词')

    def get_sign(self):
        with open('translates.js','r') as f:
            jscode = f.read()
        jsobj=execjs.compile(jscode)
        sign = jsobj.eval('e("{}")'.format(self.word))
        return sign
    def attackbaidu(self):
        """逻辑函数"""
        sign = self.get_sign()
        data = {
            "from": "en",
            "to": "zh",
            "query": self.word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "b06e91cd48fde5f5d8ec37eafba52191",
            "domain": "common",
        }
        html=requests.post(url=self.post_url,
                           data=data,
                           headers=self.post_headers).json()
        return html['trans_result']['data'][0]['dst']
if __name__ == '__main__':
    baidu = BDSpider()
    print(baidu.attackbaidu())

