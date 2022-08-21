// The element to display the image with.
const imageElement = document.querySelector('.js-image-display');

// The buttons to go previous and next.
const imageButtons = document.querySelectorAll('.js-image-control');

// Available sources of images.
const imageSources = [
"images/signup_image_1.jpg",
"images/signup_image_2.jpg",
];

// Current displayed image.
let currentImageIndex = 0;

// Variable to store the loop in.
let currentLoop;

// Show first image and start looping.
showCurrentImage();

/**
 * Cancel previous loop, wait for 2 seconds and call nextImage().
 * nextImage() will then call showCurrentImage which will call
 * loop() again. This will keep the cycle going.
 */
function loop() {
  clearTimeout(currentLoop);
  currentLoop = setTimeout(nextImage, 2000);
}

/**
 * Update the src of the imageElement with the 
 * current image index. Then reset the loop.
 */
function showCurrentImage() {
  imageElement.src = imageSources[currentImageIndex];
  loop();
}

/**
 * Remove 1 from the current image index
 * or go back to the end. Then show the image.
 */
function prevImage() {
  if (currentImageIndex === 0) {
    currentImageIndex = imageSources.length - 1;
  } else {
    currentImageIndex--;
  }
  showCurrentImage();
}

/**
 * Add 1 to current image index or go 
 * back to the start. Then show the image.
 */
function nextImage() {
  if (currentImageIndex === imageSources.length - 1) {
    currentImageIndex = 0;
  } else {
    currentImageIndex++;
  }
  showCurrentImage();
}

// Link the prev and next words to their corresponding functions.
// This way you don't have to write a lot of if / else statements
// to get the function based on the value of the button.
const actionMap = {
  'prev': prevImage,
  'next': nextImage
}

/**
 * Decide by reading the value attribute if nextImage or
 * prevImage should be called. event.currentTarget is one
 * of the two buttons that you've clicked. It gets the value
 * and looks up the function to call from the actionMap.
 *
 * @param {Event} event Click event triggerd by the buttons.
 */
function onButtonClick(event) {
  const value = event.currentTarget.value;
  const action = actionMap[value];
  action();
}

// Loop over the buttons and add an click event listener
// for each button in the list. In some older browser imageButtons
// might not be able to use forEach, so Array.from() turns it
// into an array so we know for sure that forEach is possible.
Array.from(imageButtons).forEach(function(button) {
  button.addEventListener('click', onButtonClick);
});