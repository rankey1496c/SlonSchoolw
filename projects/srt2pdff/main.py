from flask import Flask, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from subprocess import Popen, PIPE, STDOUT, run
import os
import secrets

app = Flask(__name__)

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

UPLOAD_PATH = "./uploaded"
NAME_LENGTH = 5

app.config["UPLOAD_FOLDER"] = UPLOAD_PATH
app.secret_key = "tqeqrrqyqfttryfyeqte"

def isAllowed(file_name):
    return file_name.endswith(".tex")

@app.route("/get_pdf", methods = ['GET', 'POST'])
def get_pdf():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            print("NO file part")
            for i in request.files:
                print(i)
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            print("No selected file")
            return redirect(request.url)
        if file and isAllowed(file.filename):
            filename = ''.join([secrets.choice(alphabet) for i in range(NAME_LENGTH)]) + ".tex"
            filepath = app.config['UPLOAD_FOLDER'] + "/" + filename
            file.save(filepath)
            compileProc = run(["pdflatex", filepath], input="X", encoding="ascii")
            filename = filename.replace("tex", "pdf")
            if compileProc.returncode == 0:
                os.rename(filename, app.config['UPLOAD_FOLDER'] + "/" + filename)
                return redirect(url_for('uploaded_file', filename=filename.replace(".pdf", "")))
            else:
                flash("BAD .tex file = compilation error")
                print("compilation error")
                return redirect(request.url)
        else:
            print("bad not .tex")
            flash("Bad file - send .tex")
            return redirect(request.url)
    return '''
    <!doctype html>
    <body>
        <h1>Upload .tex file</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    </body>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename + ".pdf")

if __name__ == "__main__":
    app.run()
