# python unit test
import news_extraction_api
import unittest
import glog as log

sentence = "The Trump team appears poised to argue before the Senate that no evidence exists where Trump explicitly commands a rioter to go to the Capitol and commit acts of violence."

class news_extraction_api_test(unittest.TestCase):

    def test_summarize(self):
        instance = news_extraction_api.news_extraction_api(sentence)
        s = instance.summarize()
        assert (s == "appears team poised.")
        #log.info(s)

    def test_tokenize(self):
        instance = news_extraction_api.news_extraction_api(sentence)
        assert(len(instance.tokens) == 31)
        #log.info(len(tokens))
    
    def test_who(self):
        instance = news_extraction_api.news_extraction_api(sentence)
        who = instance.who()
        assert(who.text == "team")
        #log.info(who)

    def test_what(self):
        instance = news_extraction_api.news_extraction_api(sentence)
        what = instance.what()
        #log.info(what)
        assert(what.text == "appears")


    # def setUp(self):
   #     super(news_extraction_api_test, self).setUp()
    #    self.instance = news_extraction_api.news_extraction_api()
    #def tearDown(self):
     #   super(news_extraction_api_test, self).tearDown()
      #  self.instance = None

if __name__ == '__main__':
    unittest.main()