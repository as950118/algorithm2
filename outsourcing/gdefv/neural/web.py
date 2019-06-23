from flask import Flask,render_template,request
from werkzeug import secure_filename
import flask
import sys
import time
import os
#import TFNST as NST

app = Flask(__name__)



@app.route('/main')
def render_main():
    return render_template('upload.html')

@app.route('/upload',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = flask.request.files.getlist('image[]')
        folderName = str(time.time())
        folderName = folderName.split('.')
        folderName = folderName[0] + folderName[1]
        os.makedirs('./uploads/'+folderName)
        for i in range(0,len(f)):
            f[i].save("./uploads/"+folderName+"/"+secure_filename(f[i].filename))
        
        contentpath = './uploads/'+folderName+"/"+f[0].filename
        stylepaths = []
        for i in range(1,len(f)):
            stylepaths.append('./uloads/'+folderName+"/"+f[i].filename)
        
        styleweight = 1
        styleweight /= len(stylepaths)

        return ""
    
    
            
if __name__ == '__main__':
    app.run()