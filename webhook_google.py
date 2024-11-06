import requests

class Webhook:
    def __init__(self, content):
        self.content = content
    def trigger_google_chats(self):    
        webhook_url = "https://chat.googleapis.com/v1/spaces/AAAA5S0hMqg/messages?key={YOUR_WEBHOOK_KEY}"
        message = {"text" : self.content}
        def webhook_send_message(url : str, content : dict):
            
            headers = {"Content-Type": "application/json; charset=UTF-8"}
            try:
                response = requests.post(url, json=content, headers=headers)
                print(response.status_code)
            except:
                print("deu erro guys aqui acabou gg")
        webhook_send_message(webhook_url, message)

