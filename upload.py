## The following code will import the necessary libraries, create the paths to the correct places, load a model, and use it to evaluate a single image put in production. What you guys need to do is put it into a Flask server that simply takes in the image the user uploads, places it in 'production/', and runs this code. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world has most things you'd want to know about flask. So... yeah. Test it by commenting out everything below and instead including a print("It worked!") statement that runs when this code should run. I'll provide the model that will make it work in the morning. 

# import utils; reload(utils)
# from utils import *
# import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = "/Users/ZhipingLu/Downloads/hackduke2017test-master/production"
model_path = UPLOAD_FOLDER + '/models'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return 'success'
# final_model.load(model_path + 'final.h5')
#
# production_path = 'production/'
# batch = get_batches(production_path, batch_size = 1, shuffle = False)
# predictions = final_model.predict(batch, batch_size = 1)
# print(predictions)