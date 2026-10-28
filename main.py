import smtplib, ssl
from dotenv import load_dotenv
import os
import requests

load_dotenv()

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&language=en&apiKey=ddaa4299620c4a32964bf0cff8cd1bf9"

response = requests.get(url)
content = response.json()

body = "Subject: Tesla News Update\n\n"

for article in content.get("articles", [])[:20]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")
    article_url = article.get("url", "")

    if title and article_url:
        body += f"{title}\n{description}\n{article_url}\n\n"

body = body.encode('utf-8')

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email(body)
print("Лист успішно відправлено!")