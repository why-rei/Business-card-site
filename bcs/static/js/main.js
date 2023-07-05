function copyText(text) {
    navigator.clipboard.writeText(text);
}

let lang = document.getElementById("lang");

lang.onclick = function() {
    switch (lang.text) {
        case "ru":
            window.location = "/en/resume";
            break;
        case "en":
            window.location = "/ru/resume";
            break;
    }
    console.log(lang.text);
}