from decouple import config

# Directory where the json files are stored on the client (In this case,
# inside of the container).
DIR_JSON=config('VH_DIR_JSON')
# Directory where the xml  files are stored on the client (In this case, 
# inside of the container).
DIR_XML=config('VH_DIR_XML')
# Key to criptography the data
KEY=config('VH_KEY')
# URL to upload de files
URL=config('VH_URL')
