document.addEventListener('DOMContentLoaded', function() {
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
        // SUBMIT CONFIG LOGIC
        hideCard(configCard);
    });

    // get the config
    async function getConfig() {
        const config = await store.get('userConfig');
        if (config) {
            document.getElementById('username').value = config.username;
            document.getElementById('password').value = config.password;
            document.getElementById('phoneNumber').value = config.phoneNumber;
        }
        return config;
    }

    async function saveConfig() {
        const config = {
            username: document.getElementById('username').value.trim(),
            password: document.getElementById('password').value.trim(),
            phoneNumber: document.getElementById('phoneNumber').value.trim()
        };
        
        try {
            // Basic validation to ensure fields aren't empty
            if (!config.username || !config.password || !config.phoneNumber) {
                throw new Error('All fields are required');
            }
            
            await store.set('userConfig', config);
            return config;
        } catch (error) {
            alert('Please fill in all fields');
            return null;
        }
    }
    
});
