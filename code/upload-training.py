import os, requests

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'UploadFile/'
categories = ["Tshirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle_Boot"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG"]
image_folder_path = "./images/train/"

model_id = os.environ.get('NANONETS_MODEL_ID')
AUTH_KEY = os.environ.get('NANONETS_API_KEY')

for category in categories:        
    class_image_path = os.path.join(image_folder_path, category)    
    all_class_images = [os.path.join(class_image_path, x) for x in os.listdir(class_image_path) if x.endswith(tuple(ext))]        
    for image in all_class_images:
        print (image)
        data = {'file' :open(image, 'rb'), 'category' :('', category), 'modelId' :('', model_id)}
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")

