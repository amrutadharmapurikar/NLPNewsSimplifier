from flask import Flask, request
import news_extraction_api

# Using Flask to create a local server at host 0.0.0.0 and port 200000.
app = Flask(__name__)
# This method takes in the sentence as the parameter and calls the summarize() method 
# from the news_extraction_api class and returns the summary.
@app.route('/summarize', methods = ['GET'])
def summarize():
    sentence = request.args.get("sentence", "")
    instance = news_extraction_api.news_extraction_api(sentence)
    summary = instance.summarize()
    return summary


@app.rout('/separatesentences', methods = ['GET'])
def separate_sentences():
    instance = 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000)