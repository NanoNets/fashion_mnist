import requests, os, sys, json, numpy

model_id = os.environ.get('NANONETS_MODEL_ID')
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
image_path = sys.argv[1]

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'LabelFile/'
data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
result = json.loads(response.text)['result'][0]['prediction']

probabilities = [result_dict['probability'] for result_dict in result]
best_index = numpy.argmax(probabilities)
best_label = result[best_index]['label']
print('The predicted label is: ' + str(best_label))
