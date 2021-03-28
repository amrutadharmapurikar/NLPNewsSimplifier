# python unit test
import news_extraction_api
import unittest
import glog as log
import spacy
from transformers import pipeline

#TODO: finish step 2 (make array of sentences to process) and step 3 (make shorter sentences)

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

    #array of sentences, array of their respective summaries (to make it easier to process)
    


    def test_separate_text(self):
        sentences = [["They walked unsteadily, in sneakers too loose after their shoelaces were confiscated and discarded along with all their other personal items when they were detained by the United States Customs and Border Protection.", "They walked unsteadily in sneakers too loose confiscated"], 
                        ["My dog is very furry and is a putrid green color that looks like somebody threw up on him. My cat is very smart and is a interesting red color that looks like somebody threw up on him.", "My dog is very furry and is color My cat is very smart and is color"], 
                        ["Democrats suffered a critical defeat in their bid to preserve President Biden’s $1.9 trillion stimulus package on Thursday  after the Senate’s top rule enforcer said a plan to increase the federal minimum wage could not advance as part of it, effectively knocking out a crucial piece of his plan backed by progressives. Elizabeth MacDonough, the Senate parliamentarian, told senators and staff that the provision, which would gradually increase the wage to $15 an hour by 2025, violated the strict budgetary rules that limit what can be included in the package, two aides said on Thursday. The aides disclosed the ruling on condition of anonymity because they were not authorized to comment on it. The House is expected to vote on the $1.9 trillion package as early as Friday, with the wage increase included, and it was not clear whether the decision would alter their plans. But it gave Republicans grounds to jettison the provision when the Senate considers the stimulus measure shortly after under a fast-track process known as budget reconciliation, which shields it from a filibuster, allowing it to pass without Republican support. Democrats are working to win enactment of the pandemic aid package before mid-March, when federal unemployment benefits begin to lapse. Doing so through reconciliation ensures speed, but it also comes with stringent rules that aim to prevent the process from being abused for policy initiatives that have no direct effect on the federal budget. Republicans had argued that the minimum wage increase championed by Mr. Biden and top Senate Democrats was such an abuse, in part because it had a “merely incidental” effect on the budget. Ms. MacDonough, the arbiter of Senate procedure, agreed, ruling that it was in violation of the so-called Byrd Rule, named for former Senator Robert Byrd, Democrat of West Virginia and a master of procedural tactics. The fate of the provision had long been tenuous in the Senate, particularly because two moderates, Senators Joe Manchin III of West Virginia and Kyrsten Sinema of Arizona, have publicly said they do not support such a large increase to the federal minimum wage. While the majority typically follows advice from the parliamentarian, Democrats could also try to overrule her guidance, forcing a vote  and effectively insisting on including the wage increase in the legislation anyway. Before the ruling, top Democrats had signaled that they would not support taking such an unusual step, and it was not clear whether they could muster a majority for doing so.", "Democrats suffered a critical defeat in after enforcer said a advance a MacDonough told senators violated two aides said on Thursday The aides disclosed the ruling on because they were not authorized comment on The House is expected to vote on early included and it was not clear alter But it gave Republicans grounds to jettison provision considers it allowing it to pass Democrats are working to win enactment before to Doing so through ensures speed but it also comes with Republicans had argued that increase was abuse in had MacDonough arbiter agreed ruling was The fate of had long been tenuous in Senate particularly because moderates of of have publicly said support While majority typically follows advice Democrats could also try to overrule guidance forcing Before ruling top Democrats had signaled that they would not support taking and it was not clear they muster"]]
        for s in sentences:
            sent = news_extraction_api.separate_text(s[0])
            if sent == s[1]:
                print("True")
            else:
                print("False")
            print("--------------------")
            #log.info(sent)
            #assert (sent == s[1])
        #log.info(type(sent))
        #assert (sent == "They walked unsteadily in sneakers too loose confiscated")
        
        print("******************")
        #log.info(sent)

    def test_paragraph_delineation(self):
        text = "They walked unsteadily, in sneakers too loose after their shoelaces were confiscated and discarded along with all their other personal items when they were detained by the United States Customs and Border Protection."
        sent = news_extraction_api.separate_text(text)
        log.info(sent)
        #assert(sent == "My dog is very furry and is color My cat is very smart and is color")
        
    def test_separate_text_transformers(self):
        to_tokenize = "Democrats suffered a critical defeat in their bid to preserve President Biden’s $1.9 trillion stimulus package on Thursday  after the Senate’s top rule enforcer said a plan to increase the federal minimum wage could not advance as part of it, effectively knocking out a crucial piece of his plan backed by progressives. Elizabeth MacDonough, the Senate parliamentarian, told senators and staff that the provision, which would gradually increase the wage to $15 an hour by 2025, violated the strict budgetary rules that limit what can be included in the package, two aides said on Thursday. The aides disclosed the ruling on condition of anonymity because they were not authorized to comment on it. The House is expected to vote on the $1.9 trillion package as early as Friday, with the wage increase included, and it was not clear whether the decision would alter their plans. But it gave Republicans grounds to jettison the provision when the Senate considers the stimulus measure shortly after under a fast-track process known as budget reconciliation, which shields it from a filibuster, allowing it to pass without Republican support. Democrats are working to win enactment of the pandemic aid package before mid-March, when federal unemployment benefits begin to lapse. Doing so through reconciliation ensures speed, but it also comes with stringent rules that aim to prevent the process from being abused for policy initiatives that have no direct effect on the federal budget. Republicans had argued that the minimum wage increase championed by Mr. Biden and top Senate Democrats was such an abuse, in part because it had a “merely incidental” effect on the budget. Ms. MacDonough, the arbiter of Senate procedure, agreed, ruling that it was in violation of the so-called Byrd Rule, named for former Senator Robert Byrd, Democrat of West Virginia and a master of procedural tactics. The fate of the provision had long been tenuous in the Senate, particularly because two moderates, Senators Joe Manchin III of West Virginia and Kyrsten Sinema of Arizona, have publicly said they do not support such a large increase to the federal minimum wage. While the majority typically follows advice from the parliamentarian, Democrats could also try to overrule her guidance, forcing a vote  and effectively insisting on including the wage increase in the legislation anyway. Before the ruling, top Democrats had signaled that they would not support taking such an unusual step, and it was not clear whether they could muster a majority for doing so."
        summarizer = pipeline("summarization")
        summarized = summarizer(to_tokenize, min_length=75, max_length=300)
        sent = summarized[0].get('summary_text')
        log.info(sent)
        assert(sent == " The Senate parliamentarian said a plan to increase the federal minimum wage could not advance as part of the stimulus package . The House is expected to vote on the $1.9 trillion package as early as Friday, with the wage increase included . It gave Republicans grounds to jettison the provision when the Senate considers the stimulus measure shortly after under a fast-track process known as budget reconciliation .")

if __name__ == '__main__':
    unittest.main()
