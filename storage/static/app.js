//-------------------------
// Hide/Show mobile menu when clicking burger icon
//-------------------------
const burger = document.querySelector("#burger");
const menu = document.querySelector("#menu");
const post_block = document.querySelector("#post-block");

// Attach click event to the burger icon
burger.addEventListener('click', () => {
    // Check if the menu has the class 'hidden'
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden'); // Show the mobile menu
    } else {
        menu.classList.add('hidden'); // Hide mobile menu
    }
});

//-------------------------
// Disable Submit button until text is entered
//-------------------------
const submit_button = document.querySelector("#submit-button");
let text_area = document.querySelector("#text-area");

text_area.addEventListener('keyup', () => {
    // If the <textarea> has text in it
    if (text_area.value.trim() != '') {
        // Remove 50% opacity class
        if (submit_button.classList.contains("opacity-50")) {
            submit_button.classList.remove("opacity-50");
        }
        // Enable the submit button
        submit_button.disabled = false;
    } else {
        // Add 50% opacity class
        if (!submit_button.classList.contains("opacity-50")) {
            submit_button.classList.add("opacity-50");
        }
        // Disable the submit button
        submit_button.disabled = true;
    }
});

