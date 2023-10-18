import requests

def call_api(url, payload, headers):
    response = requests.post(url, data=payload, headers=headers)
    return response.text

url = "https://text-translator2.p.rapidapi.com/translate"

payload = {
	"source_language": "en",
	"target_language": "id",
	"text": "What is your name?"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "a1d1519551msh0be91d8c02a5155p1bfb4ajsnf52f4f692d5b",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}



print(call_api(url, payload, headers))