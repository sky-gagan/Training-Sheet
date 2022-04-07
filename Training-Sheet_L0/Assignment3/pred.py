import os

import json
import fastai
from fastai import *
from fastai.text.all import *



def init():
    global model

    model = load_learner(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "m.pkl"))
    
def run(request):
    
    text = json.loads(request)
    ans = model.predict(text["Text"])
    
    return ans

