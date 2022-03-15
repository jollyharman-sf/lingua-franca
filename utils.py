import os, re
import string
import numpy as np
from config import OP_DIR, SRC_DIR


def readFile(path):
    with open(path, "r") as myfileip:
        filematerial = myfileip.readlines()
    return filematerial

def writeFile(path, data):
    with open(path, "w") as myfileop:
        myfileop.writelines(["%s\n" % item  for item in data])
        # myfileop.writelines(data)

def preprocess(sentence: string):

    sentence = sentence.lower()
    sentence = re.sub('([.,:;!?|()\-_"])', r' \1 ', sentence)
    sentence = re.sub('\s{2,}', ' ', sentence)

    return sentence

def translation():

    data = readFile(os.path.join(SRC_DIR, "input.txt"))
    data = [i.strip() for i in data]
    for i in range(len(data)):
        data[i] = preprocess(data[i])
    
    writeFile(os.path.join(SRC_DIR, "input.txt"), data)

    os.system("onmt_translate -model model/english2punjabi.pt -src static/ip_files/input.txt -output static/op_files/output.txt")
    # os.system("onmt_translate -model model/punjabi2english.pt -src static/ip_files/input.txt -output static/op_files/output.txt")


    outputString = ""
    output = readFile(os.path.join(OP_DIR, "output.txt"))
    # for x in output:
    #     outputString += x
    output = " ".join(output)
    # output = [i + "\n" for i in output]
    print(output)
    return output

