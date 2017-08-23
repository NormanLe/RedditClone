function dropdown_menu() {
    "use strict";
    var bar = document.getElementById("sorting_click");
    if (bar.className === "banner") {
        bar.className += " responsive";
    } else {
        bar.className = "banner";
    }
}