document.addEventListener('DOMContentLoaded', function() {
    const refreshButton = document.getElementById('refreshButton');
    const reservationCard = document.getElementById('ReservationCard');
    const closeReservationButton = document.getElementById('closeReservation');
    const configCard = document.getElementById('ConfigCard');
    const closeConfigButton = document.getElementById('closeConfig');
    const cancelConfigButton = document.getElementById('cancelConfig');
    const showConfigButton = document.getElementById('showConfigButton');

    refreshButton.addEventListener('click', function() {
        reservationCard.classList.toggle('hidden');
    });

    closeReservationButton.addEventListener('click', function() {
        reservationCard.classList.add('hidden');
    });

    // Function to hide the config card
    function hideConfigCard() {
        configCard.classList.add('hidden');
    }

    // Function to show the config card
    function showConfigCard() {
        configCard.classList.remove('hidden');
    }

    // Event listeners for close and cancel buttons
    closeConfigButton.addEventListener('click', hideConfigCard);
    cancelConfigButton.addEventListener('click', hideConfigCard);
    showConfigButton.addEventListener('click', showConfigCard);

    // You'll need to add logic to show the config card when needed
    // For example:
    // document.getElementById('showConfigButton').addEventListener('click', function() {
    //     configCard.classList.remove('hidden');
    // });
});
