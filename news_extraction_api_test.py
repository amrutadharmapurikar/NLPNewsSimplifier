# python unit test
import news_extraction_api
import unittest
import glog as log
import spacy

sentence = "The Trump team appears poised to argue before the Senate that no evidence exists where Trump explicitly commands a rioter to go to the Capitol and commit acts of violence."

class news_extraction_api_test(unittest.TestCase):

    def test_summarize(self):
        nlp = spacy.load("en_core_web_sm")
        instance = news_extraction_api.news_extraction_api(sentence, nlp)
        instance.max_depth = 1
        s = instance.summarize()
        log.info("starting to assert now")
        log.info(s)
        assert (s == "team appears poised")
        


    def test_tokenize(self):
        nlp = spacy.load("en_core_web_sm")
        instance = news_extraction_api.news_extraction_api(sentence, nlp)
        assert(len(instance.tokens) == 31)
        #log.info(len(tokens))
    
    def test_who(self):
        nlp = spacy.load("en_core_web_sm")
        instance = news_extraction_api.news_extraction_api(sentence, nlp)
        who = instance.who()
        assert(who.text == "team")
        #log.info(who)

    def test_what(self):
        nlp = spacy.load("en_core_web_sm")
        instance = news_extraction_api.news_extraction_api(sentence, nlp)
        what = instance.what()
        #log.info(what)
        assert(what.text == "appears")


    # def setUp(self):
   #     super(news_extraction_api_test, self).setUp()
    #    self.instance = news_extraction_api.news_extraction_api()
    #def tearDown(self):
     #   super(news_extraction_api_test, self).tearDown()
      #  self.instance = None

class sentence_summarization_test(unittest.TestCase):

    def test_separate_text(self):
        #f = open("/Users/23amrutad/Projects/NLPNewsSimplifier/test_data_1.txt", "r")
        #text = f.read()
        text = "America's ex-president, named Trump, who has orange hair was acquitted yesterday by the Senate. He was impeached by the House a few weeks ago."       
        sent = news_extraction_api.separate_text(text)
        log.info(type(sent))
        assert (type(sent) == type(""))
        
        print("******************")
        log.info(sent)

if __name__ == '__main__':
    unittest.main()