"""Zamenjuje goste dva stola u raspored-sedenja.md, pa pokreće sync.py.
Pokretanje iz korena repoa:  python3 alati/zameni.py 5 17
"""
import re, os, sys, subprocess
koren = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(koren)
a, b = (f'Sto {int(x)}' for x in sys.argv[1:3])
p = 'raspored-sedenja.md'
s = open(p, encoding='utf-8').read()
head, body = s.split('\n---\n', 1)
row = re.compile(r'^(<!--\s*)?\|\s*[\dx]+\s*\|\s*([^|]+?)\s*\|(?:\s*[^|]*?\s*\|)?\s*(-->)?\s*$')
parts = re.split(r'(^## .*$)', body, flags=re.M)
idx, rows = {}, {}
for i in range(1, len(parts), 2):
    h = parts[i][3:].strip(); idx[h] = i + 1
    rows[h] = [l for l in parts[i + 1].split('\n') if row.match(l)]
for t in (a, b):
    if t not in idx: sys.exit(f'Nema stola "{t}" u {p}')
for dst, src in ((a, b), (b, a)):
    lines = parts[idx[dst]].split('\n'); keep = [l for l in lines if not row.match(l)]
    k = next(i for i, l in enumerate(keep) if l.startswith('|---:|'))
    parts[idx[dst]] = '\n'.join(keep[:k + 1] + rows[src] + keep[k + 1:])
open(p, 'w', encoding='utf-8').write(head + '\n---\n' + ''.join(parts))
print(f'Zamenjeno: {a} <-> {b}')
subprocess.run([sys.executable, os.path.join('alati', 'sync.py')], check=True)
