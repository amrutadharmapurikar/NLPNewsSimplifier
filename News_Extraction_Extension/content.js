function content_script() {
    if (window.location.hostname != '127.0.0.1') {
        // so that my testing and the extension don't run into each other
        console.log(window.location.hostname)
        var text = document.body.innerText;
        //console.log(text);
        const Http = new XMLHttpRequest();
        post_url = 'http://127.0.0.1:20000/separate_text?'
        /*const url = 'http://127.0.0.1:20000/separate_text?text=' + text;
        Http.open("GET", url);
        Http.send();
        Http.onreadystatechange = (e) => {
            console.log(Http.responseText)
        }*/
        Http.open("POST", post_url);
        Http.setRequestHeader("Content-Type", "text");
        Http.onreadystatechange = (e) => {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                console.log(Http.responseText)
            }
        }
        Http.send("text=" + text);
    }
}
setTimeout(content_script(), 1000)