class Address:
    def __init__(self, pin_code: int, street: str, city: str, state: str, country: str):
        self.pin_code = pin_code  # ZipCode
        self.street = street
        self.city = city
        self.state = state
        self.country = country