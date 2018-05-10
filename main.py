import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)



def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def post_fact(text):
    fact = requests.post("http://talkobamato.me/", data={'input_text': text})
    return fact.url
    

@app.route('/')
def home():
    text = get_fact()
    return post_fact(text)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)



