const burger = document.querySelector("#burger");
const menu = document.querySelector("#menu");

// Attach click event to the burger icon
burger.addEventListener('click', () => {
    // Check if the menu has the class 'hidden'
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
    } else {
        menu.classList.add('hidden');
    }
});