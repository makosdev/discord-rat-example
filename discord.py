import requests

webhook_url = "https://discord.com/api/webhooks/1037793092973109249/Yj8bB3qpS7WKCBslGJrVO0kzpOv_6-x7hBMW7LdR1cDlzEWEjOwjCTk95Y_lnQMtPTyR" 


message = {
    "content": "@everyone https://github.com/makosdev"
}

response = requests.post(webhook_url, json=message)
