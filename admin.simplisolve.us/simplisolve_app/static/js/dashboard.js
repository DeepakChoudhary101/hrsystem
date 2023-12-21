function removeNewDataIndicator() {
    fetch("{% url 'remove_new_data_indicator' %}")
        .then(response => response.json())
        .then(data => {
            if (data.message === "Indicator removed") {
                document.querySelector('.new-data-indicator').style.display = 'none';
            }
        })
        .catch(error => console.error("Error:", error));
}
// Check for hash change (user navigating back)
window.addEventListener("hashchange", function (event) {
    if (location.hash !== '#apply_candidate') {
        removeNewDataIndicator();
    }
});
    