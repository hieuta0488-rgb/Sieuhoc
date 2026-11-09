import json,os,re,sys
D='/tmp/claude-0/vocab'
ipa=json.load(open(f'{D}/ipa.json'))
words=[]
for i in range(6):
    for x in json.load(open(f'{D}/out_{i}.json')):
        base=re.sub(r'\s+\d+$','',x['w'])
        x['ipa']=x.get('ipa') or ipa.get(x['w']) or ipa.get(base) or ''
        x['toeic']=int(x.get('toeic',0))
        words.append(x)
seen={w['w'].lower() for w in words}
if os.path.exists(f'{D}/toeic_extra.json'):
    for x in json.load(open(f'{D}/toeic_extra.json')):
        if x['w'].lower() not in seen: x['toeic']=1; words.append(x); seen.add(x['w'].lower())
def ld(n,dflt):
    p=f'{D}/{n}'; return json.load(open(p)) if os.path.exists(p) else dflt
import glob
school=[]
for f in sorted(glob.glob('/tmp/claude-0/school/en_g*.json'), key=lambda f:int(re.search(r'en_g(\d+)',f).group(1))):
    school+=json.load(open(f))
for u in school: u.setdefault('subject','en')
bank=[]
# SUBJ: các môn khác (toan_*, van_*, ...) dạng {units,bank}
for f in sorted(glob.glob('/tmp/claude-0/school/*_g*.json')):
    if os.path.basename(f).startswith(('en_','bank_')): continue
    d=json.load(open(f)); school+=d.get('units',[]); bank+=d.get('bank',[])
for f in sorted(glob.glob('/tmp/claude-0/school/bank_g*.json')):
    bank+=json.load(open(f))
keep=['w','pos','vi','lv','t','toeic','ex','exvi','ipa']
data={'school':school,'bank':bank,'words':[{k:w.get(k,'') for k in keep} for w in words],'grammar':ld('grammar.json',[]),'part5':ld('part5.json',[]),
      'part6':ld('part6.json',[]),'part7':ld('part7.json',[]),'listening':ld('listening.json',{'p1':[],'p2':[],'p3':[],'p4':[]})}
js='const DATA='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';'
tpl=open('/home/user/TOEIC_APP/template.html',encoding='utf-8').read()
out=tpl.replace('/*__DATA__*/',js.replace('</','<\\/'))
open('/home/user/TOEIC_APP/SieuHocTOEIC.html','w',encoding='utf-8').write(out)
L=data['listening']
print('school units',len(school),'bank',len(bank),'words',len(data['words']),'grammar',len(data['grammar']),'p5',len(data['part5']),'p6',len(data['part6']),'p7',len(data['part7']),'listen',{k:len(v) for k,v in L.items()},'size KB',len(out.encode())//1024)
from collections import Counter
print(Counter(w['lv'] for w in data['words'])); print(Counter(w['pos'] for w in data['words']).most_common(14))
print('no ipa:',sum(1 for w in data['words'] if not w['ipa']))

import re as _re
frag=out
frag=_re.sub(r'<!DOCTYPE html>\s*<html[^>]*>\s*<head>\s*<meta charset="UTF-8">\s*<meta name="viewport"[^>]*>\s*','',frag,1)
frag=frag.replace('</head>\n<body>\n','',1).replace('</body>\n</html>\n','')
open('/tmp/claude-0/-home-user/fb90b537-cf29-58ff-afc4-11d4086a0b75/scratchpad/sieu_toeic.html','w',encoding='utf-8').write(frag)
print('artifact frag KB',len(frag.encode())//1024, frag[:60].replace('\n',' '))
