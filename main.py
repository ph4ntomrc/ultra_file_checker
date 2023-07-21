import os
from subprocess import check_output
from flask import Flask, flash, request, redirect, url_for, render_template, render_template_string, send_from_directory
from werkzeug.utils import secure_filename
from flag import FLAG

UPLOAD_FOLDER = '/mnt/d/mytasks/ultra_file_checker/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res = os.popen(f"file uploads/{filename}").read()
            return render_template('index.html', output=res)
        else:
            return render_template_string("Прикол")
    else:
        return render_template('index.html')
app.run("0.0.0.0", 8080)
