from flask import Flask, render_template, request
from microsofttranslator import Translator
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', message="翻訳したい文章を入力してください")

@app.route('/', methods=['POST'])
def post_request():
    # request.formにPOSTデータがある
    source = request.form["source"]
    df=pd.read_csv("secret_bing_translate.csv", header=None)
    NAME_TRANS = df[0][0]
    KEY_TRANS = df[0][1]
    translator = Translator(NAME_TRANS, KEY_TRANS)
    to_lang = request.form["to_lang"]
    from_lang = request.form["from_lang"]
    result = translator.translate(source, to_lang, from_lang)
    global firstevent
    histories[source] = result
    return render_template('index.html', message="翻訳結果", source = source, result=result, histories = histories)

if __name__ == '__main__':
    histories = {}
    app.run()
