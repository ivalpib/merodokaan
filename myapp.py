import requests
import json
url = "http://127.0.0.1:8000/product/"

data = {
    'sku': 'B0028138',
    'product_name': 'Tamar Valley',
    'product_description': 'Greek Style Yogurt',
    'category': 9,
    'product_price': 7.86,

}
data_json = json.dumps(data)
headers = {
    'Content-Type': 'application/json'
}
r = requests.post(url=url, data = data_json, headers=headers)

data = r.json()
print(data)