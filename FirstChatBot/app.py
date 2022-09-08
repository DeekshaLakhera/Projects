from flask import Flask, request, jsonify
import requests
import re


app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount={}".format(target_currency, source_currency, amount)

    payload = {}
    headers = {
      "apikey": "w7pF1t2X7F7EqPafec7EoF3EpVWIpAXz"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    converted_currency = result.split(',')[-1].split(':')[-1]
    converted_currency = round(float(('.').join(re.findall(r'\d+', converted_currency))),2)

    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, converted_currency, target_currency)
    }

    return jsonify(response)


if __name__ == "__main__":
  app.run(debug=True)
