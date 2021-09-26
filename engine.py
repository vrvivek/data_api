'''
This is the python module from which the swagger api will call methods from
'''

# -- coding: utf-8 -
# written by Ibrahim Aderinto

# Import system modules
import os
import random
import shutil
import string
from zipfile import ZipFile

ascii_ = string.ascii_letters + string.digits


def generate_id():
    new_id = ''.join([random.choice(ascii_) for i in range(3)])
    os.mkdir(f"data/{new_id}")
    return {'id': new_id}

def upload(id, upload_file):
    print("upload_file",upload_file)
    zip = ZipFile(upload_file)
    print("zip",zip.namelist())
    zip.extractall(f'data/{id}')
    names = []
    for name in zip.namelist():
        shutil.copy(f"data/{id}/{name}", f'data/{id}')
        ind = name.index('/')
        names += [name[ind+1:]]
    shutil.rmtree(f"data/{id}/{name[:ind]}")
    return {"id": id, "uploaded_files" : ', '.join(names)}

