import sys, re

path = '动力系统笔记/rainbow.sty'
try:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print(f"File not found: {path}")
    sys.exit(1)

envs = [
    ('Theorem', 'theorem', '定理'),
    ('Lemma', 'lemma', '引理'),
    ('Corollary', 'corollary', '推论'),
    ('Definition', 'definition', '定义'),
    ('Axiom', 'axiom', '公理'),
    ('Postulate', 'postulate', '公设'),
    ('Proposition', 'proposition', '命题'),
    ('Assumption', 'assumption', '假设'),
    ('Property', 'property', '性质'),
    ('Conjecture', 'conjecture', '猜想'),
]

new_envs = []
new_envs.append('\n%================ 无编号版本 ================')
for cap, env, name in envs:
    snip = f'''
% ---- {env}* {name}（无编号） ----
\\newtcolorbox{{{env}*}}[1][]{{%
  enhanced, breakable, blanker, colback=white,
  borderline west={{3pt}}{{-1pt}}{{rb{cap}Color!50}},
  left=.66em, right=0pt, top=.66em, bottom=.66em,
  before skip=.5em, after skip=.5em,
  fonttitle=\\heiti\\bfseries\\color{{rb{cap}Color}},
  fontupper=\\kaishu,
  attach title to upper={{\\par\\vspace{{.3em}}}},
  title={{{name}%
    \\ifx\\\\#1\\\\\\else~(#1)\\fi
  }},
}}'''
    new_envs.append(snip)

marker = '%================ 附加：proof 环境 ================'
if marker not in text:
    print('Marker not found')
    sys.exit(1)
text = text.replace(marker, '\n'.join(new_envs) + '\n\n' + marker)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated 动力系统笔记/rainbow.sty')
