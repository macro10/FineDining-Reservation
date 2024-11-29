const { invoke } = window.__TAURI__.core;
const { listen } = window.__TAURI__.event;

listen("event_name", (eventPayload) => {
  console.log(eventPayload);
});

let greetInputEl;
let greetMsgEl;
let restaurantInputEl;
let partySizeInputEl;

async function reserve() {
  // * invokes rust function "reserve", passing in an object containing the user's name input
  // * await waits for the rust function to complete and returns the result
  // * result is displayed on frontend by setting it as the text content of greetMsgEl
  const reservation = {
    name: greetInputEl.value,
    restaurant: restaurantInputEl.value,
    partySize: partySizeInputEl.value
  };

  greetMsgEl.textContent = await invoke("reserve", { reservation });
}

window.addEventListener("DOMContentLoaded", () => {
  greetInputEl = document.querySelector("#greet-input");
  restaurantInputEl = document.querySelector("#restaurant-input");
  partySizeInputEl = document.querySelector("#party-size-input")
  greetMsgEl = document.querySelector("#greet-msg");
  document.querySelector("#greet-form").addEventListener("submit", (e) => {
    e.preventDefault();
    reserve(); // When input is submitted it calls the reserve function
  });
});
