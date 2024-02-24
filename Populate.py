# Create objects of all identified classes
from Classes import BoardingPass, CheckInSystem, Flight, Passenger


passenger1 = Passenger("James Smith", "09A", "NA4321")
flight1 = Flight("NA4321", "New York JFK", "2")
boarding_pass1 = BoardingPass(passenger1, "03", "11:40")
check_in_system = CheckInSystem([flight1])

# Use object functions to populate and display boarding pass details
passenger1.set_name("John Doe")
passenger1.set_seat_number("05B")
passenger1.set_flight_number("NA1234")

boarding_pass1.display_boarding_pass()
