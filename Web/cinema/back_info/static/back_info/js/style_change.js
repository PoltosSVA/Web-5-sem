document.addEventListener("DOMContentLoaded", function() {
    const content = document.querySelector(".content");


    document.getElementById("text-color").addEventListener("change", function() {
        content.style.color = this.checked ? "green" : "";
    });

    document.getElementById("bg-color").addEventListener("change", function() {
        content.style.backgroundColor = this.checked ? "lime" : "";
    });
});