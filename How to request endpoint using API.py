import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


# Request data goes here
data = {
    "data":
    [
        {
            'Date': "2021-07-08 08:00:00",
        },
         {
            'Date': "2021-07-08 09:00:00",
        },
          {
            'Date': "2021-07-08 10:00:00",
        },
          {
            'Date': "2021-07-08 11:00:00",
        },
    ],
}


body = str.encode(json.dumps(data))

url = URI_ENDPOINT
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    result1 = json.loads(result)
    result2 = json.loads(result1)
    # print(type(result))
    # print(type(result1))
    # print(type(result2))
    print(result2["forecast"])

  

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())