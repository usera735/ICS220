class Passenger:
    def __init__(self, name, seat_number, flight_number):
        self.name = name
        self.seat_number = seat_number
        self.flight_number = flight_number

    def set_name(self, name):
        self.name = name

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_name(self):
        return self.name

    def get_seat_number(self):
        return self.seat_number

    def get_flight_number(self):
        return self.flight_number

    def check_in(self):
        pass  # This function should handle the check-in process.


class BoardingPass:
    def __init__(self, passenger, gate, departure_time):
        self.passenger = passenger
        self.gate = gate
        self.departure_time = departure_time

    def set_passenger(self, passenger):
        self.passenger = passenger

    def set_gate(self, gate):
        self.gate = gate

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_passenger(self):
        return self.passenger

    def get_gate(self):
        return self.gate

    def get_departure_time(self):
        return self.departure_time

    def display_boarding_pass(self):
        pass  # This function should display the boarding pass details.


class Flight:
    def __init__(self, number, destination, terminal):
        self.number = number
        self.destination = destination
        self.terminal = terminal

    def set_number(self, number):
        self.number = number

    def set_destination(self, destination):
        self.destination = destination

    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_number(self):
        return self.number

    def get_destination(self):
        return self.destination

    def get_terminal(self):
        return self.terminal

    def update_boarding_time(self, new_time):
        pass  # This function should update the boarding time for the flight.


class CheckInSystem:
    def __init__(self, flights):
        self.flights = flights

    def check_in_passenger(self, passenger, flight):
        pass  # This function should handle the check-in process for a passenger.

    def issue_boarding_pass(self, passenger, flight):
        pass  # This function should issue a boarding pass for a passenger on a flight.
