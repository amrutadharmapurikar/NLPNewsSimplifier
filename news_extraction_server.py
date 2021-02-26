from flask import Flask, request
import news_extraction_api
from flask_cors import CORS
import glog as log


summarized_text = ""

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
@app.route('/separate_text', methods = ['POST'])
def separate_text():
    original_text = str(request.data)
    summary = news_extraction_api.separate_text(original_text)
    #summary.headers.add("Access-Control-Allow-Origin", "*")
    global summarized_text
    summarized_text = summary
    #log.info(summarized_text)
    #print(summarized_text)
    return summary

# This method takes a block of text and returns the summarized version.
@app.route('/separate_text_transformers', methods = ['POST'])
def separate_text_transformers():
    print("INSEPARATE_TEXT_TRANSFORMERS")
    original_text = str(request.data)
    summary = news_extraction_api.separate_text_transformers(original_text)
    #summary.headers.add("Access-Control-Allow-Origin", "*")
    global summarized_text
    summarized_text = summary
    log.info(summarized_text)
    log.info("-------------------------")
    #print(summarized_text)
    return summary


# This method takes a block of text and returns the summarized version.
@app.route('/get_separate_text', methods = ['GET'])
def get_separate_text():
    original_text = request.args.get("text", "")
    log.info(original_text)
    summary = news_extraction_api.separate_text(original_text)
    #summary.headers.add("Access-Control-Allow-Origin", "*")
    global summarized_text
    summarized_text = summary
    #log.info(summarized_text)
    #print(summarized_text)
    return summary




# This method will return the summarized_text
@app.route('/return_text', methods = ['GET'])
def return_text():
    print("IN_RETURN_TEXT")
    global summarized_text
    #log.info(summarized_text)
    #summarized_text += "<br> Hello</br>"
    log.info(summarized_text)
    log.info("--------------------------------")
    return summarized_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000)