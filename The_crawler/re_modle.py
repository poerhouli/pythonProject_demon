import re
html = '''
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际会浅水游</p></div>
'''
# 非贪婪
pattern = re.compile("<div><p>(.*?)</p></div>", re.S)
r_list = pattern.findall(html)
print(r_list)



