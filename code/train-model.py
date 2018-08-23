import requests, os, json

model_id = os.environ.get('NANONETS_MODEL_ID')
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'Train/'

querystring = {'modelId': model_id}
response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), params=querystring)

result = json.loads(response.text)
print (result)

print("\n\nNEXT RUN: python ./code/model-state.py")
