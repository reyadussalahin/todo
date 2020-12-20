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

// function deleteTask(event) {
//     console.log("deteting task...");
//     event.preventDefault();

//     url = getUrl() + "/delete/";
//     let xhr = new XMLHttpRequest();
//     xhr.open("POST", url);
//     xhr.addEventListener("readystatechange", function() {
//         if(xhr.readyState === 4 && xhr.status === 200) {
//             let response = JSON.parse(xhr.responseText);
//             if(response["status"] === "success") {
//                 console.log("deleted task successfully...");
//             } else {
//                 console.log("error: " + response["message"])
//             }
//             window.location = getOrigin() + "/";
//         }
//     });
//     // xhr.setRequestHeader("Content-Type", "x-www-form-url-encoded");
//     const formData = new FormData();
//     formData.append("csrfmiddlewaretoken", getCSRFMiddlewareToken());
//     xhr.send(formData);
// }


// function initApp() {
//     let taskDelete = document.querySelector(".task-delete");
//     if(taskDelete !== null) {
//         taskDelete.addEventListener("click", deleteTask);
//     }
// }


// initApp();