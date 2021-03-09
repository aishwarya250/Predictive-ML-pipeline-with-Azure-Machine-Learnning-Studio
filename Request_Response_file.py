import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'age': "39",   
                            'workclass': "State-gov",   
                            'fnlwgt': "77516",   
                            'education': "Bachelors",   
                            'education-num': "13",   
                            'marital-status': "Never-married",   
                            'occupation': "Adm-clerical",   
                            'relationship': "Not-in-family",   
                            'race': "White",   
                            'sex': "Male",   
                            'capital-gain': "2174",   
                            'capital-loss': "0",   
                            'hours-per-week': "40",   
                            'native-country': "United-States",   
                            'income': "<=50K",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/3e59d73b3b4f4f8ebc28b652cb4d5aaa/services/f96215166cfa4790a12921b544df7693/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
