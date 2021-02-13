import spacy
import glog as log

class news_extraction_api(object):  


    def __init__(self, sentence):
        self.nlp = spacy.load("en_core_web_sm")
        self.tokens = []
        self.doc = self.nlp(sentence)
        for token in self.doc:
            self.tokens.append(token)
        self.keywords = []
        self.max_depth = 1

    def summarize(self):
        """This function should put into a list tokens that are above a certain depth.
        """
        self.important(self.what(), 0)
        s = ""
        for w in self.keywords:
            if len(s) != 0 and w.dep_ != "punct":
                s += " " 
            s += w.text
        return s
   
    def important(self, tok, depth):
        self.keywords.append(tok)
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
