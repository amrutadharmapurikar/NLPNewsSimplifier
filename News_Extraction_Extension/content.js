if (window.location.hostname != '127.0.0.1') {
    // so that my testing and the extension don't run into each other
    console.log(window.location.hostname)
    var text = document.body.innerText;
    //console.log(text);
    const Http = new XMLHttpRequest();
    const url = 'http://127.0.0.1:20000/summarize_text?text=' + text;
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
    }
}

//alert("Hello from your Chrome extension!")