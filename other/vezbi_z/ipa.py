import requests
import json

class fca:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def caa(self, prompt, max_tokens=2500):
        data = {
            'model': 'gpt-4',
            'messages': [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            'max_tokens': max_tokens
        }
        response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data))
        if response.status_code == 200:
            message = response.json()['choices'][0]['message']['content']
            print(message)
            #return message
        else:
            error_message = f"Error: {response.status_code}, {response.text}"
            print(error_message)
            #return error_message
'36hPJ8MwhFUzwuiAfT3BlbkFJxw38ODsLIn8xmtdCcN6F'