function getOrigin() {
    let origin = window.location.origin;
    if(origin[origin.length - 1] === "/") {
        origin = origin.substr(0, origin.length - 1);
    }
    return origin;
}

function getUrl() {
    let url = window.location.toString();
    if(url[url.length - 1] === "/") {
        url = url.substr(0, url.length - 1);
    }
    return url;
}

function getCSRFMiddlewareToken() {
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    return token;
}
