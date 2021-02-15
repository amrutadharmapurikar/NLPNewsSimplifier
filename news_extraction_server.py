from flask import Flask, request
import news_extraction_api
from flask_cors import CORS

# Using Flask to create a local server at host 0.0.0.0 and port 200000.
app = Flask(__name__)
CORS(app)
# This method takes in the sentence as the parameter and calls the summarize() method 
# from the news_extraction_api class and returns the summary.
@app.route('/summarize_sentence', methods = ['GET'])
def summarize_sentence():
    sentence = request.args.get("sentence", "")
    instance = news_extraction_api.news_extraction_api(sentence)
    summary = instance.summarize()
    return summary

# This method takes a block of text and returns the summarized version.
@app.route('/summarize_text', methods = ['GET'])
def separate_text():
    text = request.args.get("text", "")
    summary = news_extraction_api.separate_text(text)
    #summary.headers.add("Access-Control-Allow-Origin", "*")
    return summary

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000)