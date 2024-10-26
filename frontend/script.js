document.addEventListener('DOMContentLoaded', function() {
    const refreshButton = document.getElementById('refreshButton');
    const reservationCard = document.getElementById('ReservationCard');
    const closeReservationButton = document.getElementById('closeReservation');
    const configCard = document.getElementById('ConfigCard');
    const submitConfigButton = document.getElementById('submitConfig');
    const cancelConfigButton = document.getElementById('closeConfig');
    const showConfigButton = document.getElementById('showConfigButton');

    // make reservation button shows reservation card
    refreshButton.addEventListener('click', function() {
        reservationCard.classList.toggle('hidden');
    });

    // close reservation card
    closeReservationButton.addEventListener('click', function() {
        reservationCard.classList.add('hidden');
    });

    // hide the config card
    function hideConfigCard() {
        configCard.classList.add('hidden');
    }

    // show the config card
    function showConfigCard() {
        configCard.classList.remove('hidden');
    }

    submitConfigButton.addEventListener('click', function() {
        // CONFIG SUBMISSION LOGIC
        hideConfigCard()
    });

    // Event listeners for close and cancel buttons
    cancelConfigButton.addEventListener('click', hideConfigCard);
    showConfigButton.addEventListener('click', showConfigCard);
});
