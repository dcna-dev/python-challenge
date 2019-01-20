import json
import os
import base64
import requests
from dicttoxml import dicttoxml
from Crypto.Cipher import AES
from sender_settings import *
from time import sleep


def convert_json_to_xml(json_file):
    name = json_file.split('.')[0] + '.xml'
    with open(DIR_JSON + json_file) as json_data:
        data = json.load(json_data)
    data_xml = dicttoxml(data)
    with open(DIR_XML + name, 'wb') as xml_file:
        xml_file.write(data_xml)


def encrypt_file(file, key):
    aes = AES.new(key.encode('utf8'), AES.MODE_ECB)
    with open(DIR_XML + file) as f:
        data = f.read()
        data = data+'#'*(16-len(data)%16)
        data_encrypted = aes.encrypt(data.encode('utf8'))
    file = file +'#'*(16-len(file)%16)
    file_name = aes.encrypt(file.encode('utf8'))
    return [file_name, data_encrypted]

if __name__ == '__main__':
    key = KEY
    print('--- Converting json files ---')
    print('--- Reading from ./data_json/ ---')
    print('--- Saving converted XML files in ./data_xml/ ---')
    for file in os.listdir('./data_json/'):
        convert_json_to_xml(file)
    print('--- Encrypting XML data ---')
    for file in os.listdir('./data_xml/'):
        data_enc = encrypt_file(file, key)
        data64 = base64.b32encode(data_enc[1])
        name64 = base64.b32encode(data_enc[0])
        data_send = {'file_name': name64.decode('utf8'),
                     'data': data64.decode('utf8')}
        print('--- Sending encrypted data ---')
        resp = requests.post(URL, json=data_send)
        if resp.status_code != 200 and resp.text != "OK":
            print("Error: " + str(resp.status_code))
    sleep(60)

