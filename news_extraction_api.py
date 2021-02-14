import spacy
import glog as log
import nltk

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
        log.info("starting to summarize")
        """This function should put into a string tokens that are above a certain depth.
        """
        self.important(self.what(), 0)
        s = ""
        punct = [".", ",", "?", "!"]
        for w in self.sentence.split(" "):
            if w[-1] in punct:
                w = w[0:-1]
            if w in self.keywords:
                if len(s) != 0:
                    s += " "
                s += w
        return s
   
    def important(self, tok, depth):
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

def separate_text():
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
    f = open("/Users/23amrutad/Projects/NLPNewsSimplifier/test_data_1.txt", "r")
    text = f.read()
    sentences = tokenizer.tokenize(text)
    s = ""
    log.info("Here I am starting to tokenize the sentences.")
    nlp = spacy.load("en_core_web_sm")
    for sent in sentences:
        if len(sent) != 0:
            instance = news_extraction_api(sent, nlp)
            s += instance.summarize()
    log.info("Finished tokenizing the sentences.")
    return s