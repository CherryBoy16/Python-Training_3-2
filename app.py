'''import requests
import os
from dotenv import load_dotenv
api_key=os.getenv("hf_api_key")
if not api_key:
    print("Api key not found")
hearders='{"authorization":f"bearer {api_key}}'
url="https://huggingface.co/"
payload={"inputs":"write a quotation for success"}
data= requests.post(url,headers=hearders,json=payload)
result=data.json()
print(result)'''

from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "mfgDat4DNF6f+QbbipA1Kg==EWt5d3lxWvioJs7O"
API_URL = "https://api.api-ninjas.com/v2/randomquotes"
HEADERS = {"X-Api-Key": API_KEY}

@app.route("/quote", methods=["GET"])
def get_online_quote():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=5)
        response.raise_for_status()
        data = response.json()
        quote_text = data[0]["quote"]
        quote_author = data[0]["author"]
        return jsonify({"quote": quote_text, "author": quote_author})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch quote", "details": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)