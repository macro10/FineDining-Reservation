const { invoke } = window.__TAURI__.core;


let restaurantSelectEl;
let dateInputEl;
let timeInputEl;
let partySizeInputEl;
let outputMsgEl;


async function reserve() {
    const reservation = {
        restaurant: restaurantSelectEl.value,
        date: dateInputEl.value,
        time: timeInputEl.value,
        partySize: partySizeInputEl.value
    };

    outputMsgEl.textContent = await invoke("reserve", { reservation });
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
    
    document.querySelector('#reservationForm').addEventListener("submit", (e) => {
        e.preventDefault();
        reserve(); // When input is submitted it calls the reserve function
    });
    // generic card visibility functions
    function showCard(card) {
        card.classList.remove('hidden');
    }
    function hideCard(card) {
        card.classList.add('hidden');
    }

    
    // update reservation button, (refresh symbol), shows reservation card
    updateReservationButton.addEventListener('click', () => showCard(reservationCard));

    // close reservation button hides reservation card
    closeReservationButton.addEventListener('click', () => hideCard(reservationCard));

    submitReservationButton.addEventListener('click', function() {
        //MAKE RESERVATION LOGIC
        hideCard(reservationCard);
    });

    // update config button, (gear icon), shows config card
    updateConfigButton.addEventListener('click', () => showCard(configCard));

    // close config button hides config card
    closeConfigButton.addEventListener('click', () => hideCard(configCard));
    
    // submit button for submitting config information to storage
    submitConfigButton.addEventListener('click', function() {
        
        hideCard(configCard);
    });


});