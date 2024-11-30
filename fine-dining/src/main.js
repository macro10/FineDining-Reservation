const { invoke } = window.__TAURI__.core;


let restaurantSelectEl;
let dateInputEl;
let timeInputEl;
let partySizeInputEl;
let outputMsgEl;

// generic card visibility functions
function showCard(card) {
  card.classList.remove('hidden');
}
function hideCard(card) {
  card.classList.add('hidden');
}

async function reserve() {
    // Validate form before proceeding
    if (!restaurantSelectEl.value || !dateInputEl.value || !timeInputEl.value || !partySizeInputEl.value) {
        console.error("Please fill in all required fields");
        return;
    }

    const reservation = {
        restaurant: restaurantSelectEl.value,
        date: dateInputEl.value,
        time: timeInputEl.value,
        partySize: parseInt(partySizeInputEl.value)
    };

    try {
        const response = await invoke("reserve", { reservation });
        console.log("Reservation response:", response);
        hideCard(document.getElementById('ReservationCard'));
    } catch (error) {
        console.error("Reservation failed:", error);
    }
}


window.addEventListener('DOMContentLoaded', () => {
    // Buttons
    const updateReservationButton = document.getElementById('refreshButton');
    const closeReservationButton = document.getElementById('closeReservation');
    const submitReservationButton = document.getElementById('reserveButton');
    const closeConfigButton = document.getElementById('closeConfig');
    const updateConfigButton = document.getElementById('showConfigButton');
    const submitConfigButton = document.getElementById('submitConfig');

    // Cards
    const reservationCard = document.getElementById('ReservationCard');
    const configCard = document.getElementById('ConfigCard');

    // Inputs & Selections
    restaurantSelectEl = document.querySelector('#restaurant');
    dateInputEl = document.querySelector('#date');
    timeInputEl = document.querySelector('#time');
    partySizeInputEl = document.querySelector('#partySize');
    
    // Remove the click event listener from submitReservationButton since we're using form submission
    submitReservationButton.removeEventListener('click', function() {
        hideCard(reservationCard);
    });

    // Update the form submission handler
    document.querySelector('#reservationForm').addEventListener("submit", async (e) => {
        e.preventDefault();
        await reserve();
    });
    
    // update reservation button, (refresh symbol), shows reservation card
    updateReservationButton.addEventListener('click', () => showCard(reservationCard));

    // close reservation button hides reservation card
    closeReservationButton.addEventListener('click', () => hideCard(reservationCard));

    updateConfigButton.addEventListener('click', () => showCard(configCard));
    closeConfigButton.addEventListener('click', () => hideCard(configCard));
    submitConfigButton.addEventListener('click', function() {
        
        hideCard(configCard);
    });


});