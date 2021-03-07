"""
execjs模块
"""
import execjs
with open('translates.js','r') as f:
    jscode = f.read()

jsobj = execjs.compile(jscode)
sign = jsobj.eval('e("girl")')
print(sign)