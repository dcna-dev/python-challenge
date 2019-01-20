This is a solution for a challenge that wants:

  - Write a Python script that converts json files to xml, encrypts and transfers to a remote location.
  - Solution should be prepared as two Docker images, 1st to send files, and 2nd to receive them.
  - Pipeline: json -> XML -> encryption -> transfer -> decryption -> XML

This solution:

  - Sender container:
    - Have a python script that:
        - Read json files from ./data_json/, converts it and save the XML files in ./data_xml/.
        - Read the XML files, encrypt the data and send to server using HTTP POST and jso: {'file_name': 'encrypted_name', 'data': 'encrypted_data'}

  - Server container:
    - Have a Flask app that:
      - Receives encrypted data via HTTP POST
      - Decrypts received data
      - Saves the in XML files in ./data_server/ using the same name as used in sender

To use:
  - Puts the json files in ./data/data_json/
  - Run docker-compose
  - The sender XML files will be saved in ./data/data_xml/ (in plain text, the data is encrypted only when will be transfer)
  - The XML files received and decrypted by the server will be saved in ./data/data_server/
