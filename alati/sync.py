"""Usklađuje raspored-sedenja.md (brojevi, numeracija, pregled) i iz njega pravi data/raspored.js.
Pokretanje iz korena repoa:  python3 alati/sync.py

Redovi u tabelama:   | 3 | Ime Prezime | napomena |   (napomena nije obavezna, npr. "vegan")
Zakomentarisan red:  <!-- | x | Ime Prezime | -->       (ne prikazuje se i ne računa)
"""
import re, json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# grupa 1: komentar, 2: broj, 3: ime, 4: napomena (opciono)
ROW = re.compile(r'^(<!--\s*)?\|\s*([\dx]+)\s*\|\s*([^|]+?)\s*\|(?:\s*([^|]*?)\s*\|)?\s*(-->)?\s*$')

p = 'raspored-sedenja.md'
s = open(p, encoding='utf-8').read()
head, body = s.split('\n---\n', 1)
parts = re.split(r'(^## .*$)', body, flags=re.M)
secs = []; newbody = parts[0]
for i in range(1, len(parts), 2):
    h = parts[i][3:].strip(); sec = parts[i + 1]; items = []; k = 0; out = []
    for l in sec.split('\n'):
        m = ROW.match(l)
        if m:
            commented, name, note = bool(m.group(1)), m.group(3), (m.group(4) or '').strip()
            if not commented:
                k += 1
                l = f'| {k} | {name} | {note} |' if note else f'| {k} | {name} | |'
            items.append((commented, name, note))
        out.append(l)
    sec = '\n'.join(out)
    sec = re.sub(r'\*(\d+) (gostiju|gosta|gost|osoba)', lambda m: f'*{k} {m.group(2)}', sec, count=1)
    newbody += parts[i] + sec; secs.append((h, items))

mlad = [x for x in secs if x[0].startswith('Mlad')][0]
tabs = [x for x in secs if not x[0].startswith('Mlad')]
vis = lambda it: sum(1 for c, _, _ in it if not c)
tot = sum(vis(it) for _, it in tabs)
head = re.sub(r'\*\*Ukupno gostiju:\*\* \d+ · \*\*Stolova:\*\* \d+',
              f'**Ukupno gostiju:** {tot} · **Stolova:** {sum(1 for _, it in tabs if vis(it))}', head)
head = re.sub(r'\(zaseban, \d+ osoba,', f'(zaseban, {vis(mlad[1])} osoba,', head)
for h, it in tabs:
    n = re.search(r'\d+', h).group()
    head, c = re.subn(r'(\| \[Sto %s\]\(#sto-%s\) \| )\d+( \|)' % (n, n), r'\g<1>%d\g<2>' % vis(it), head)
    assert c == 1, f'U pregledu nema reda za {h}'
head, c = re.subn(r'\| \*\*Ukupno\*\* \| \*\*\d+\*\* \|', f'| **Ukupno** | **{tot}** |', head); assert c == 1
open(p, 'w', encoding='utf-8').write(head + '\n---\n' + newbody)

def entry(name, note):
    if note:
        return json.dumps({'ime': name, 'napomena': note}, ensure_ascii=False).replace('{"', '{ "').replace('"}', '" }')
    return json.dumps(name, ensure_ascii=False)

def arr(items, ind):
    v = [i for i, (c, _, _) in enumerate(items) if not c]; last = v[-1] if v else -1
    return '\n'.join(ind + ('// ' + json.dumps(n, ensure_ascii=False) if c else entry(n, note) + (',' if i < last else ''))
                     for i, (c, n, note) in enumerate(items))

js = ("// Raspored sedenja — NE MENJATI RUČNO: pravi se iz raspored-sedenja.md (python3 alati/sync.py).\n"
      "// Mladenački sto se prikazuje zasebno i ne ulazi u ukupan broj gostiju.\n"
      "// Zakomentarisana imena (//) se ne prikazuju i ne računaju.\n"
      "// Gost sa napomenom (npr. posebna ishrana): { \"ime\": \"…\", \"napomena\": \"vegan\" }\nwindow.RASPORED = {\n")
js += '  "mladenacki": [\n' + arr(mlad[1], '    ') + '\n  ],\n  "stolovi": [\n'
js += ',\n'.join('    {\n      "broj": %d,\n      "gosti": [\n%s\n      ]\n    }' % (int(re.search(r'\d+', h).group()), arr(it, '        ')) for h, it in tabs) + '\n  ]\n};\n'
open('data/raspored.js', 'w', encoding='utf-8').write(js)

slobodni = [h for h, it in tabs if not vis(it)]
napomene = sum(1 for _, it in secs for c, _, note in it if note and not c)
print(f'OK: {tot} gostiju, {len(tabs) - len(slobodni)} zauzetih stolova, slobodan: {", ".join(slobodni) or "nijedan"}, '
      f'mladenački sto {vis(mlad[1])}, napomena: {napomene}')
