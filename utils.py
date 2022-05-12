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
        # myfileop.writelines(["%s\n" % item  for item in data])
        myfileop.write('\n'.join(data))
        
def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)

def preprocess(sentence: string):

    sentence = sentence.lower()
    sentence = re.sub('([.,:;!?|()\-_"])', r' \1 ', sentence)
    sentence = re.sub('\s{2,}', ' ', sentence)
    return sentence

def translationEng2Pun():

    output_filepath = os.path.join(OP_DIR, "output_punjabi.txt")
    remove_file(output_filepath)

    os.system("python3 model/helpers/2-subword.py model/english-tokenizer.model model/punjabi-tokenizer.model static/ip_files/input_english.txt model/helpers/empty_file.txt")
    
    os.system("onmt_translate -model model/english2punjabi_lat.pt -src static/ip_files/input_english.txt.subword -output static/op_files/output_punjabi.txt")
    
    os.system("python3 model/helpers/3-desubword.py model/punjabi-tokenizer.model static/op_files/output_punjabi.txt")

    read_output = readFile(os.path.join(OP_DIR, "output_punjabi.txt.desubword"))
    
    read_output = "".join(read_output)
    read_output = read_output.strip()
    print(read_output)
    return read_output

def translationPun2Eng():
    
    output_filepath = os.path.join(OP_DIR, "output_english.txt")
    remove_file(output_filepath)

    os.system("python3 model/helpers/2-subword.py model/punjabi-tokenizer.model model/english-tokenizer.model static/ip_files/input_punjabi.txt model/helpers/empty_file.txt")
    
    os.system("onmt_translate -model model/punjabi2english_lat.pt -src static/ip_files/input_punjabi.txt.subword -output static/op_files/output_english.txt")
    
    os.system("python3 model/helpers/3-desubword.py model/english-tokenizer.model static/op_files/output_english.txt")

    read_output = readFile(os.path.join(OP_DIR, "output_english.txt.desubword"))
    read_output = "".join(read_output)
    read_output = read_output.strip()
    print(read_output)
    return read_output