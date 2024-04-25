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

function adjustTextareaHeight(textarea, maxHeight) {
    // Reset the height to auto to shrink it if needed
    textarea.style.height = 'auto';
    // Set the height to the minimum value between scroll height and max height
    textarea.style.height = Math.min(textarea.scrollHeight, maxHeight) + 'px';
}

document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('results');
    var maxHeight = 200;
  
    textarea.addEventListener('input', function() {
        adjustTextareaHeight(this, maxHeight);
    });

    adjustTextareaHeight(textarea, maxHeight);
});