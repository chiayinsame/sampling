function copyTextareaContent() {
    // Select the textarea
    var textarea = document.getElementById("results");

    // Select its content
    textarea.select();

    // Copy the selected text
    document.execCommand("copy");

    // Deselect the textarea
    textarea.setSelectionRange(0, 0);

    // Alert the user that the text has been copied
    alert("Text copied to clipboard!");
}