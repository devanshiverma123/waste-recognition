from flask import Flask, render_template, request, redirect, url_for, flash
import inference
from flask_bootstrap import Bootstrap
from inference import get_prediction
import os
import urllib.request
from werkzeug.utils import secure_filename
import webbrowser

UPLOAD_FOLDER = r'C:\Users\NDH60042\MAJOR PROJECT\Flask project'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)
"""
Routes
"""
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request_url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            print(file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            new_file = os.path.join(r'C:\Users\NDH60042\MAJOR PROJECT\Flask project',filename)
            result, accuracy = get_prediction(new_file)
            if len(result.split())==2:
                search = "https://www.google.com/search?q=DIY+Reusing+Ideas+for"+result.split()[0]+result.split()[1]
            else:
                search = "https://www.google.com/search?q=DIY+Reusing+Ideas+for"+result
            flash(result)
            flash(accuracy)
            flash(filename)
            webbrowser.open(search)
            return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
