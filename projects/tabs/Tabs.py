import requests, re
import sys
url = sys.argv[1]
s = requests.get(url).text
result = re.search(r'"content":"(.*?)"', s)
result = result.groups()[0] + '\\n'
e = re.findall(r'n.\|(.*?)\|[^-|0-9]{1}', result)
k = re.findall(r'\\n.', result)
strings = ['' for i in range(6)]
for i in range(len(e)):
    strings[i % 6] += e[i]

result1 = re.search(r'"tuning":{(.*?)}}', s)
if not result1:
    value = {1: 'E A D G B E'}
else:
    name = re.search(r'"name":"(.*?)"', result1[1])
    value = re.search(r'"value":"(.*?)"', result1[1])

e = set(re.findall(r'\\r\\n(.)\|', result[1]))
tact = 6
with open('out.tex', 'w') as file:
    file.write('\\documentclass{guitartabs}\n\
\\thispagestyle{empty}\n\
\\begin{document}\n\
\\large\n')
    str2 = f'\\begin{{tabline}}{{{tact}}}{{{4}}}{{{4}}}{{{",".join(value[1].split())}}}'
    str3 = ''
    k = 0
    f = True
    for i in range(len(strings[0])):
        if f and k != 0 and not k % (tact * 3):
            file.write(r'\end{tabline}')
        if f and not k % (tact * 3):
            file.write(str2)
            f = False
        if f and k != 0 and not k % 3:
            file.write(r'\nextbar')
            f = False

        b = False
        for j in range(6):
            if strings[j][i] != '-' and strings[j][i] != '|':
                b = True
                f = True
        #             % note 1 of 3, string 5, fret 4
        k += b
        for j in range(6):
            if strings[j][i] != '-' and strings[j][i] != '|':
                file.write(f'\\note{{{(k - 1) % 3 + 1}}}{{{3}}}{{{j + 1}}}{{{strings[j][i]}}}')

    file.write('\end{tabline}\n\
    \end{document}')
