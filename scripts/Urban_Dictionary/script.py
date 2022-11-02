import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

UD_API_KEY = os.environ.get("UD_API_KEY")

word = str(input("Enter Word : "))

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":word}

headers = {
	"X-RapidAPI-Key": UD_API_KEY,
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_str = json.dumps(response.text)
y = json.loads(response.text)
print(
"\n",
"Showing Results for", y["list"][0]["word"], "\n",
"Definition : ", y["list"][0]["definition"], "\n", 
"Permalink " , y["list"][0]["permalink"], "\n", 
"Written On : " , y["list"][0]["written_on"], "\n", 
"Example : " , y["list"][0]["example"], "\n", 
"Author : " , y["list"][0]["author"], "\n", 
)
