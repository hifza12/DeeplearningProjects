#Import necessary libraries
from io import BytesIO
from flask import Flask, render_template, request, url_for, redirect, send_file, flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import  Mail
from werkzeug.utils import secure_filename
import numpy as np
import os
import pymysql
import tensorflow as tf
from keras.preprocessing import image
#from keras.preprocessing.image import load_img
#from keras.preprocessing.image import img_to_array
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.utils import img_to_array


local_server=True
with open("config.json",'r')as c:
    params=json.load(c)["params"]

app = Flask(__name__)
if (local_server):
    ##Database
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)
db.init_app(app)

#load model
model =load_model("model/mobilenet.h5")
print('@@ Model loaded')
class Contacts(db.Model):
    #user_id,user_fullname,user_phno,user_email,user_message
    user_id = db.Column(db.Integer, primary_key=True)
    user_fullname = db.Column(db.String(80), unique=False, nullable=False)
    user_phno=db.Column(db.String(12),nullable=False)
    user_email=db.Column(db.String(80),nullable=False)
    user_message=db.Column(db.String(80),nullable=False)
#
# class Uploaded_images(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     file_name = db.Column(db.String(50),nullable=False)
#     data = db.Column(db.LargeBinary)

class Check_data(db.Model):
    image_id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(100),nullable=False)
    predicted_class = db.Column(db.String(100),nullable=False)
@app.route('/predict',methods=['GET','POST'])
def predict():
    global preds, result, file_path
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
    #         print("@@ Input posted = ", filename)
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
        img = load_img(file_path, target_size=(150, 150))
        x =img_to_array(img)
        # x = np.true_divide(x, 255)
        ## Scaling
        x = x / 255
        x = np.expand_dims(x, axis=0)
        preds = model.predict(x)
        preds = np.argmax(preds, axis=1)
       # classes_x=np.argmax(class_prediction,axis=1)
        if preds == 0:
             preds = "The Plant is effected from Bacterical Blight Disease"
        elif preds == 1:
             preds = 'The Plant is effected from Curl Virus'
        elif preds == 2:
             preds= 'The Plant is effected Fussarium Wilt Disease'
        else:
             preds = "This is the Healthy Cotton Plant With no disease"

        upload = Check_data(image_name=file.filename, predicted_class=preds)
        db.session.add(upload)
        db.session.commit()
        result = preds
        print('@@ Raw result = ', result)
    return render_template('predict.html', result=preds, user_image=file_path)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        message=request.form.get('message')
        # user_id,user_fullname,user_phno,user_email,user_message
        entry = Contacts(user_fullname=name, user_phno=phone,user_email=email,user_message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
# For local system & cloud
if __name__ == '__main__':
    app.run(debug=True)

