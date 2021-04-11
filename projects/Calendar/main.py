import csv

def csv_reader(path):
    global d
    reader = csv.reader(path)
    for row in reader:
        row = row[0]
        row = row.split(";")
        if row[-1] == '':
            row = row[:-1]
        if int(row[0]) in d.keys():
            d[int(row[0])] += "\\\\" + " ".join(row[:])
            
        else:
            d[int(row[0])] = " ".join(row[:])
            


d = {}
clines = ["1-6", "1 - 6", "2-7", "2-7"]
clis = 0
path = "table.csv"
with open(path, 'r') as csv_path:
    csv_reader(csv_path)
    csv_path.close()
pathtex = "out.tex"
with open(pathtex, 'wb') as tex_path:
    tex_path.write("""\\documentclass[a4paper, landscape]{article}

\\usepackage[utf8]{inputenc}
\\usepackage[english,russian]{babel}
\\usepackage[a4paper, margin=0px,landscape]{geometry}
\\usepackage{graphicx}
\\geometry{top=0mm,left=0mm, right=0mm, bottom=0mm}

\\newcommand{\\Cellfill}[2]{\\begin{minipage}[c][50mm][c]{30mm}
			\\begin{center}
                #1 \\\\ #2
			\\end{center}
	\\end{minipage}}

\\setlength\\parindent{0pt}

\\begin{document}\n
\\begin{center}
	\\begin{tabular}{c|c|c|c|c|c|c|c|}""".encode())
    tex_path.write("\\cline{".encode())
    tex_path.write(clines[clis].encode())
    tex_path.write("}".encode())
    clis += 1
    key = min(d.keys())
    tex_path.write("\\multicolumn{1}{|c|}{\\Cellfill{".encode())
    tex_path.write(str(key).encode())
    tex_path.write("}{".encode())
    tex_path.write(str(d[key]).split()[1].encode())
    tex_path.write("}}".encode())
    del d[key]
    for j in range(3):
        for i in range(5):
            key = min(d.keys())
            tex_path.write("&\\Cellfill{".encode())
            tex_path.write(str(key).encode())
            tex_path.write("}{".encode())
            tex_path.write(str(d[key]).split()[1].encode())
            tex_path.write("}".encode())
            del d[key]
        if j == 2:
            pass
        else:
            tex_path.write("\\\\".encode())
            tex_path.write("\\cline{".encode())
            tex_path.write(clines[clis].encode())
            tex_path.write("}\n".encode())
            clis += 1
    key = min(d.keys())
    tex_path.write("&\Cellfill{".encode())
    tex_path.write(str(key).encode())
    tex_path.write("}".encode())
    tex_path.write("{".encode())
    tex_path.write(str(d[key]).split()[1].encode())
    tex_path.write("}\\\\".encode())
    tex_path.write("\\cline{".encode())
    tex_path.write(clines[clis].encode())
    tex_path.write("}\n".encode())
    tex_path.write("\\end{tabular}\n\\end{center}".encode())
    tex_path.write("\\end{document}".encode())
    tex_path.close()
