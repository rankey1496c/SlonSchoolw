import csv
with open('table.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
# print(your_list)

# print(*your_list[0])

s = f'\\PeopleField{{1}}{{1}}{{2}}'
# print(s)

with open('out.tex', 'w') as f:
    f.write('\\documentclass[a4paper]{article}\n\
                \\usepackage[utf8]{inputenc}\n\
                \\usepackage[english,russian]{babel}\n\
                \\usepackage{geometry}\n\n\
                \\geometry{top=0mm,left=0mm, right=0mm, bottom=0mm}\n\n\
                \\newsavebox{\\foo}\n\
                \\newcommand{\\savedata}[1]{\\savebox{\\foo}{\\ifvoid\\foo\\else\\unhbox\\foo{} \\fi\\fbox{\#1}}}\n\
                \\newcommand{\\printdata}{\\framebox{\\parbox{4cm}{\\raggedright\\unhbox\\foo}}}\n\n\
                \\newcommand{\\PeopleField}[3]{\\framebox{\\begin{minipage}[c][53.98mm][c]{85.6mm}\n\
			    \\begin{center}\n\
				{\\LARGE\n\
					\\flushleft\n\
					{#2}\\\\}\n\
				\\vbox to 1em{}\n\
				{\\huge{#1}\\\\}\n\
				\\vbox to 1em{}\n\
				{\\LARGE\n\n\
				\\flushright{#3} \\\\}\n\
			\\end{center}\n\
	\\end{minipage}}}\n\n\
    \\setlength\parindent{0pt}\
\\begin{document}\n')
    c = 0
    print(your_list)
    for i in your_list:
        c += 1
        s = '\\PeopleField{' + i[0] + '}{' + i[1] + '}{' + i[2] + '}'
        if not c % 2:
             s += '\\\\'
        s += '\n'
        # print(s)
        f.write(s)
	# \PeopleField{Иван Иванович Иванов}{ГУГОЛ}{УБОРЩИК}
    f.write('\\end{document}')


