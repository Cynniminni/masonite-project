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