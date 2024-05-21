import json
import requests

headers = {"Authorization": "PASTE YOUR OWN EDEN AI api KEY HERE"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Naveen"
}

# response = requests.post(url, json=payload, headers=headers)

# result = json.loads(response.text)
# print(result['openai']['generated_text'])

def call_to_openai(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])

call_to_openai("Tell me about Hindusism")
