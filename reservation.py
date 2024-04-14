class Reservation:
    def __init__(self) -> None:
        """
        constructor for reservation object
        """
        self.restaurant = None
        self.party_size = None
        self.hour = None
        self.minute = None
        self.username = None
        self.password = None
        self.phone_number = None
        self.complete = None

    def set_params(self, restaurant, party_size, hour, minute, username, password, phone_number, complete) -> None:
        """
        sets reservation object parameters
        """
        self.restaurant = int(restaurant)
        self.party_size = int(party_size)
        self.hour = str(hour)
        self.minute = str(minute)
        self.username = str(username)
        self.password = str(password)
        self.phone_number = int(phone_number)
        self.complete = bool(complete)
