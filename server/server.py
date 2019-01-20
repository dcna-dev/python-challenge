#!.venv/bin/python
import base64
from Crypto.Cipher import AES
from flask import Flask, request
from server_settings import *

app = Flask(__name__)

def decrypt_data(data):
    data_dec = base64.b32decode(data)
    key = KEY
    aes = AES.new(key.encode('utf8'), AES.MODE_ECB)
    data_dec = aes.decrypt(data_dec)
    data_dec = data_dec.decode('utf8').rstrip('#')
    return data_dec

@app.route('/vanhack/api/v1.0/upload', methods=['POST'])
def upload_file():
    print('--- Data received, reading it ---')
    name = request.get_json()['file_name']
    data = request.get_json()['data']
    print('--- Decrypting data ---')
    name = decrypt_data(name)
    data = decrypt_data(data)
    print('--- Saving data in xml files (./data_server/)')
    with open(DIR_SERVER + name, 'wb') as xml_file:
        xml_file.write(data.encode('utf8'))
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
