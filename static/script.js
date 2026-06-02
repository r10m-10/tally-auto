const input = document.getElementById("floatingInputGroup1");
const button = document.querySelector(".btn");

input.addEventListener("input", () => {
    if (input.value.trim() !== "") {
        button.style.opacity = "1";
        button.style.visibility = "visible";
    } else {
        button.style.opacity = "0";
        button.style.visibility = "hidden";
    }
});

button.addEventListener('click', function(){
    let expression = document.getElementById('floatingInputGroup1').value
    fetch('/auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expression: expression })
    })
    .then(function(response) {
        return response.json()
    })
})