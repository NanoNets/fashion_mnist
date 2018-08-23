import requests, os, json

model_id = os.environ.get('NANONETS_MODEL_ID')
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + "Model/"
querystring = {'modelId': model_id}

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY,''), params=querystring)
result = json.loads(response.text)

state = result["state"]
status = result["status"]

if state != 5:
	print "The model isn't ready yet, it's status is:", status
	print "We will send you an email when the model is ready. If your imapatient, run this script again in 10 minutes to check."
	print "\n\nmore details at:"
	print "https://app.nanonets.com/classify/?appId="+model_id
else:
	print "NEXT RUN: python ./code/prediction.py ./images/test/Bag/test_0006.jpeg"

