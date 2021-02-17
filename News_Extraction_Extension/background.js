chrome.browserAction.onClicked.addListener(function() {
    chrome.tabs.create({'url':"http://127.0.0.1:20000/return_text"})
    //var text = document.body.innerText;
    //console.log(text)
    //chrome.tabs.create({url:"http://www.cnn.com"})
    //chrome.tabs.create({'url':"file:///Users/23amrutad/Projects/NLPNewsSimplifier/News_Extraction_Extension/test.html"})
    
})