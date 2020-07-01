@app.route('/getdiy',methods=['POST'])

def submit_file(getdiy):
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
        webbrowser.open(search)
        return redirect('/')
