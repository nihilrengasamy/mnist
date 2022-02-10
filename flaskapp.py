from flask import Flask,render_template,request
import requests
import json
import numpy as np
from PIL import Image

app = Flask(__name__)

'''@app.route("/",methods=['GET'])
def union():
    return render_template('ui.html')'''


@app.route("/predict",methods=["POST"])


def home():
     
    if request.method=='POST':

        #Accepting input image from user 
        #image=request.files['file']ag

        # convert this image to pil image
        pil_image = Image.open(request.files['file'].stream).convert("L")

        img = pil_image.resize((28,28))

        img2arr = np.array(img)
        img2arr = img2arr / 255.0
        img2arr = img2arr.reshape(1,-1)

        #numpydata = input() 

        test = json.dumps({"data": img2arr.tolist()})

        # URL for the web service
        scoring_uri = 'http://5895b6eb-e70e-4fac-8abe-14b2db5b6257.centralindia.azurecontainer.io/score'
        # If the service is authenticated, set the key or token

        # Two sets of data to score, so we get two results back

        # Set the content type 
        headers = {'Content-Type': "application/json"}


        # Make the request and display the response
        resp = requests.post(scoring_uri, test, headers=headers)
        print(resp.text)

if __name__ == '__main__':
   app.run(debug = True)



