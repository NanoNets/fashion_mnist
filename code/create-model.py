import requests, os, json, sys

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
url = BASE_URL + "Model/"

categories = ["Tshirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle_Boot"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG"]

data = {'categories' : categories}
headers = {
        'accept': 'application/x-www-form-urlencoded'
    }

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), data=data)
result = json.loads(response.text)
if not("model_id" in result.keys()):
    print('Error')
    print(result)
    sys.exit(1)
model_id = result["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")
