from base64 import encode
import json, os
from utils import translation, writeFile
from config import SRC_DIR
from flask import Blueprint, request, Response


translate_api = Blueprint("translating", __name__)

@translate_api.route("/translating", methods=['POST'])
def translating():

    if request.method == "POST":
        req = request.form
        text_area = req["text_area"]
        option = req["option"]
        print("******************************************************************************************")
        print(text_area)
        print(option)
        writeFile(os.path.join(SRC_DIR, "input.txt"), text_area.split("\n"))
        print("******************************************************************************************")
        print(text_area.split("\n"))
        print("******************************************************************************************")

    translatedText = translation()

    data = {"translation": "done",
            "translated_text_is": translatedText}

    return Response(json.dumps(data),
                mimetype="application/json",
                status=200)
