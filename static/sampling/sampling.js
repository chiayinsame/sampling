function copyTextareaContent() {
    var textarea = document.getElementById("results");
    textarea.select();
    document.execCommand("copy");
    textarea.setSelectionRange(0, 0);
}

function clearTextareaContent() {
    document.getElementById("results").value = "";

    var paragraph = document.getElementById("results-generated");
    paragraph.style.display = "none";
}

function clearForm() {
    // Get the form element
    var form = document.getElementById("excel-form");

    // Loop through all form elements
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];

        // Check if the element is an input
        if (element.tagName === "INPUT") {
            // Clear the value of the element
            element.value = "";
        }
    }
}