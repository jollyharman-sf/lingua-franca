from base64 import encode
import json, os
from utils import translationEng2Pun, translationPun2Eng, writeFile, preprocess
from config import SRC_DIR
from flask import Blueprint, request, Response


translate_api = Blueprint("translating", __name__)

@translate_api.route("/translating", methods=['POST'])
def translating():

    if request.method == "POST":
        req = request.form
        text_area = req["text_area"]
        option = req["option"]
        print("*************************************1****************************************************")
        print(text_area)
        if option == '1':
            data = text_area.split("\n")
            data = [i.strip() for i in data]
            for i in range(len(data)):
                data[i] = preprocess(data[i])
            writeFile(os.path.join(SRC_DIR, "input_english.txt"), data)
            translatedText = translationEng2Pun()
            
        elif option == '2':
            writeFile(os.path.join(SRC_DIR, "input_punjabi.txt"), text_area.split("\n"))
            print(text_area.split("\n"))
            translatedText = translationPun2Eng()
        
        print("**************************************2****************************************************")

    data = {"translation": "done",
            "translated_text_is": translatedText}

    return Response(json.dumps(data),
                mimetype="application/json",
                status=200)
