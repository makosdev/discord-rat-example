import requests

webhook_url = "WEBHOOK-HERE" 


message = {
    "content": "@everyone https://github.com/makosdev"
}

response = requests.post(webhook_url, json=message)
