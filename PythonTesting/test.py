import requests
from io import BytesIO
import playsound

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

payload = {
	"voice_code": "en-US-1",
	"text": "hello, what is your name?",
	"speed": "1.00",
	"pitch": "1.00",
	"output_type": "audio_url"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "a1d1519551msh0be91d8c02a5155p1bfb4ajsnf52f4f692d5b",
	"X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.headers)

print(response.json())

print(response.json().keys())

print(response.json())

audio_url = response.json()['result']['audio_url']
print(audio_url)

audio_content = BytesIO(requests.get(audio_url).content)

print(audio_content)

playsound.playsound(audio_content)