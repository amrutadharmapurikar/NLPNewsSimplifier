import spacy
import glog as log
import nltk
from transformers import pipeline


class news_extraction_api(object):  

    def __init__(self, sentence, nlp):
        self.nlp = nlp
        self.sentence = sentence
        self.tokens = []
        self.doc = self.nlp(sentence)
        for token in self.doc:
            self.tokens.append(token)
        self.keywords = []
        self.max_depth = 2
        self.words = []

    def unjumble(self):
        s = ""
        punct = [".", ",", "?", "!"]
        for w in self.sentence.split(" "):
            if w[-1] in punct:
                w = w[0:-1]
            if w in self.keywords:
                s += w
        return s

    def summarize(self):
        #log.info("starting to summarize")
        """This function should put into a string tokens that are above a certain depth.
        """
        self.important(self.what(), 0)
        s = ""
        punct = [".", ",", "?", "!"]
        for w in self.sentence.split(" "):
            if len(w) == 0:
                continue
            if w[-1] in punct:
                w = w[0:-1]
            if w in self.keywords:
                if len(s) != 0:
                    s += " "
                s += w
        return s

    def summarize_h1(self):
        #log.info("starting to summarize")
        """This function should put into a string tokens that are above a certain depth.
        """
        self.important(self.what(), 0)
        s = ""
        punct = [".", ",", "?", "!"]
        
        in_order = []

        for token in self.doc:
            if token.text in self.keywords:
                for w in self.words:
                    if w[1] == token.head and w[0] == token.text:
                        in_order.append(str(token))
        
        for w in self.sentence.split(" "):
            if len(w) == 0:
                continue
            if w[-1] in punct:
                w = w[0:-1]
            if w in in_order:
                if len(s) != 0:
                    s += " "
                s += w
        return s
   
    def important(self, tok, depth):
        l = [tok.text, tok.head]
        self.words.append(l)
        self.keywords.append(tok.text)
        depth += 1
        if depth <= self.max_depth:
            for child in tok.children:
                self.important(child, depth)

    def who(self):
        for t in self.tokens:
            if t.dep_ == "nsubj":
                return t

    def what(self):
        for t in self.tokens:
            if t.dep_ == "ROOT":
                return t

def separate_text_transformers(text):
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
    split_paragraphs = text.split("\\n")
    summary = ""
    sentences = []
    summarizer = pipeline("summarization")
    for para in split_paragraphs: # each paragraph
        para = str(para)
        log.info(para)
        to_tokenize = para
        max_len = int (len(para.split(" "))/2)
        log.info(para.split(" "))
        max_len += 2
        log.info(max_len)
        summarized = summarizer(to_tokenize, min_length=0, max_length=max_len)
        log.info(len(summarized))
        log.info(summarized)
        t = summarized[0].get('summary_text')
        log.info(len(t))
        log.info(t)
        summary += t
        if len(t) != 0:
            summary += "<br></br>"
        log.info(summary)
    return summary

def separate_text(text):
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
    split_paragraphs = text.split("\\n")
    log.info(len(split_paragraphs))
    sentences = []
    for para in split_paragraphs:
        if len(sentences) != 0:
            sentences.append("\n")
        sentences += tokenizer.tokenize(para)
    #sentences = tokenizer.tokenize(text)
    s = ""
    #log.info("Here I am starting to tokenize the sentences.")
    nlp = spacy.load("en_core_web_sm")
    for sent in sentences:
        #log.info(sent)
        if len(sent) != 0:
            if sent == "\n":
                s += "<br></br>"
                log.info("i got HERERERERERERERERERERERERERERERERERERe.")
            else:
                instance = news_extraction_api(sent, nlp)
                if len(s) != 0:
                    s += " "
                s += instance.summarize()
    #log.info("Finished tokenizing the sentences.")
    log.info(s)
    return s