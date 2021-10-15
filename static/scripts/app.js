// Popup
const addBtnEl = document.querySelector(".add");
const popUpCardContainerEl = document.querySelector(".popup-card-container");
const closeBtnEl = document.querySelector(".close-icon");
const items = document.querySelectorAll(".item-container");

addBtnEl.addEventListener("click", () => {
  popUpCardContainerEl.classList.toggle("hide");
});

closeBtnEl.addEventListener("click", () => {
  popUpCardContainerEl.classList.toggle("hide");
});

items.forEach((item) => {
  const itemTitle = item.querySelector(".item-title");
  const priceDiffEl = item.querySelector(".price-difference span");
  const priceDifference = parseFloat(priceDiffEl.textContent);

  if (priceDifference > 0) {
    itemTitle.classList.add("high-price");
  } else if (priceDifference < 0) {
    itemTitle.classList.add("low-price");
  }
});
