# -*- coding: utf-8 -*-

# This simple app performs a GET request to retrieve a list of languages
# supported by Microsoft Translator.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid


import os, requests, uuid, json

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-languages
base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/languages?api-version=3.0'
constructed_url = base_url + path

headers = {
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

request = requests.get(constructed_url, headers=headers)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
