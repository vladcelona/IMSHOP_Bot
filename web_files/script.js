const sections = document.querySelectorAll('section[id]')

// The function for scrolling to the selected section on a landing page
function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current=> {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 50,
            sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']')
                .classList.add('active-link')
        } else {
            document.querySelector('.nav__menu a[href*=' + sectionId + ']')
                .classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive);

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

// The function for changing the background header
function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if (this.scrollY >= 80) {
        header.classList.add('scroll-header');
    } else {
        header.classList.remove('scroll-header');
    }
}
window.addEventListener('scroll', scrollHeader);

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

// Items in a popup window
const popupWindow = document.getElementById('popupWindow');
const closeButton = document.getElementById('closeButton');
const popupImage = document.getElementById('popupImage');
const popupPrice = document.getElementById('popupPrice');
const popupDescription = document.getElementById('popupDescription');
const favoritesButton = document.getElementById('favoritesButton');
const shoppingCartButton = document.getElementById('shoppingCartButton');

// Properties for closeButton
closeButton.addEventListener('click', () => {
    popupWindow.style.display = 'none';
});

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

// Item container for items below
const itemContainerCatalog = document.getElementById('itemContainerCatalog');
const itemContainerShoppingCart = document.getElementById('itemContainerShoppingCart');
const itemContainerFavorites = document.getElementById('itemContainerFavorites');

// Example list of items
const items = [
    {
        image: 'https://via.placeholder.com/100',
        price: '$19.99',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        favorites: false,
        shopping_cart: false,
    },
    {
        image: 'https://via.placeholder.com/100',
        price: '$29.99',
        description: 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        favorites: false,
        shopping_cart: false,
    },
    {
        image: 'https://via.placeholder.com/100',
        price: '$109.99',
        description: 'Sed do eiusmod tempor Lorem ipsum dolor sit amet',
        favorites: false,
        shopping_cart: false,
    },
    {
        image: 'https://via.placeholder.com/100',
        price: '$209.99',
        description: 'Sed do eiusmod tempor Lorem ipsum dolor sit amet',
        favorites: false,
        shopping_cart: false,
    },
    {
        image: 'https://via.placeholder.com/100',
        price: '$9.99',
        description: 'Sed do eiusmod tempor Lorem ipsum dolor sit amet',
        favorites: false,
        shopping_cart: false,
    },
  // Add more items here
];

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

// Function for creation of a single item
function createItem(itemData, index) {
    const item = document.createElement('div');
    item.className = 'list-item';
    item.innerHTML = `
        <img src="${itemData.image}" alt="Example Item Image">
        <div class="item-price">${itemData.price}</div>
        <div class="item-description">${itemData.description}</div>
        <div class="button-row">
            <button class="favorites-button" id="itemShoppingCartButton">
                <img class="favorites-icon" src="/web_files/image_files/iconmonstr-heart-thin.svg" alt="Heart Icon">
            </button>
            <button class="shopping-cart-button" id="itemFavoritesButton">
                <span class="shopping-cart-text">Add</span>
            </button>
        </div>
    `;

    item.addEventListener('click', function(itemElement) {
        if (itemElement.target.id !== 'itemShoppingCartButton' && itemElement.target.id !== 'itemFavoritesButton') {
            showPopupWindow(itemData, index);
        }
    });
    return item;
}

// Adding items to itemContainer
function generateItemContainerCatalog() {
    for (var index = 0; index < items.length; index++) {
        const item = createItem(items[index], index);
        itemContainerCatalog.appendChild(item);
    }
}

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

// Function for showing the content of an item
function showPopupWindow(itemData, index) {
    popupWindow.style.display = 'block';
    popupImage.src = itemData.image;
    popupPrice.textContent = itemData.price;
    popupDescription.textContent = itemData.description;

    favoritesButton.addEventListener('click', () => {
        addToFavorites(itemData, index);
    });

    shoppingCartButton.addEventListener('click', () => {
        addToShoppingCart(itemData, index);
    });
}

/* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-= */

function addToFavorites(itemData, index) {
    if (itemData.favorites === false && document.getElementById(`favorites_${index}`) === null) {
        const item = document.createElement('div');
        item.className = 'list-item';
        item.id = `favorites_${index}`;
        item.innerHTML = `
            <img src="${itemData.image}" alt="Example Item Image">
            <div class="item-price">${itemData.price}</div>
            <div class="item-description">${itemData.description}</div>
            <div class="button-row">
                <button class="favorites-button" id="itemShoppingCartButton">
                    <img class="favorites-icon" src="/web_files/image_files/iconmonstr-heart-thin.svg" alt="Heart Icon">
                </button>
                <button class="shopping-cart-button" id="itemFavoritesButton">
                    <span class="shopping-cart-text">Add</span>
                </button>
            </div>
        `;

        item.addEventListener('click', function (itemElement) {
            if (itemElement.target.id !== 'itemShoppingCartButton' && itemElement.target.id !== 'itemFavoritesButton') {
                showPopupWindow(itemData, index);
            }
        });
        itemContainerFavorites.appendChild(item);
    }
}

function addToShoppingCart(itemData, index) {
    if (itemData.favorites === false && document.getElementById(`cart_${index}`) === null) {
        const item = document.createElement('div');
        item.className = 'list-item';
        item.id = `cart_${index}`;
        item.innerHTML = `
            <img src="${itemData.image}" alt="Example Item Image">
            <div class="item-price">${itemData.price}</div>
            <div class="item-description">${itemData.description}</div>
            <div class="button-row">
                <button class="favorites-button" id="itemShoppingCartButton">
                    <img class="favorites-icon" src="/web_files/image_files/iconmonstr-heart-thin.svg" alt="Heart Icon">
                </button>
                <button class="shopping-cart-button" id="itemFavoritesButton">
                    <span class="shopping-cart-text">Add</span>
                </button>
            </div>
        `;

        item.addEventListener('click', function (itemElement) {
            if (itemElement.target.id !== 'itemShoppingCartButton' && itemElement.target.id !== 'itemFavoritesButton') {
                showPopupWindow(itemData, index);
            }
        });
        itemContainerShoppingCart.appendChild(item);
    }
}

window.onload = generateItemContainerCatalog;