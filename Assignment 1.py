from datetime import datetime
from enum import Enum

class Airline(Enum):
    NationalAirlines = 1
    flyEmirates = 2
    EttihadAirways = 3

class Ticket(Enum):
    Economy = 1
    Business = 2
    FirstClass = 3

class Passenger:
    """ A class that represents the passengers"""

    #constructor
    def __init__(self, fName = "", lName = "", age = 0, passportID = "", passportExpiryDate = ""):
        self.__fName = fName
        self.__lName = lName
        self.__age = age
        self.__passportID = passportID
        self.__passportExpiryDate = passportExpiryDate

    #setter and getter
    def setfName(self, fName = ""):
        self.__fName = fName

    def getfName(self):
        return self.fName

    def setlName(self, lName=""):
        self.__lName = lName

    def getlName(self):
        return self.__lName

    def setAge(self, age=0):
        self.__age = age

    def getAge(self):
        return self.__age

    def setPassportID(self, passportID=""):
        self.__passportID = passportID

    def getPassportID(self):
        return self.__passportID

    def setPassportExpiryDate(self, passportExpiryDate=""):
        self.__passportExpiryDate = passportExpiryDate

    def getPassportExpiryDate(self):
        return self.__passportExpiryDate

    # Get the full name of the passenger
    def getFullName(self):
        return f"{self.__fName} {self.__lName}"

    # Display the passenger's information
    def displayInfo(self):
        print("Passenger Information:")
        print(f"Full Name: {self.getFullName()}")
        print(f"Age: {self.__age}")
        print(f"Passport ID: {self.__passportID}")
        print(f"Passport Expiry Date: {self.__passportExpiryDate}")

    # Check if the passport is valid
    def checkPassportValidity(self):
        current_date = datetime.now()
        expiry_date = datetime.strptime(self.__passportExpiryDate, "%Y-%m-%d")

        if current_date < expiry_date:
            print("Passport is valid.")
        else:
            print("Passport has expired!")

    def isAdult(self):
        return self.__age >= 18

class Staff:
    """ A class that represents the staff in the airport"""

    #constructor
    def __init__(self, fName = "", lName = "", employeeID = "", password = ""):
        self.__fName = fName
        self.__lName = lName
        self.__email = fName + "." + lName + '@airport.ac.ae'
        self.__employeeID = employeeID
        self.__password = password

    #setter and getter
    def setfName(self, fName = ""):
        self.__fName = fName

    def getfName(self):
        return self.__fName

    def setlName(self, lName=""):
        self.__lName = lName

    def getlName(self):
        return self.__lName

    def setEmail(self, email=""):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setEmployeeID(self, employeeID=""):
        self.__employeeID = employeeID

    def getEmployeeID(self):
        return self.__employeeID

    def setPassword(self, password=""):
        self.__password = password

    def getPassword(self):
        return self.__password

    def getFullName(self):
        return f"{self.__fName} {self.__lName}"

    # Display the employee's information
    def displayInfo(self):
        print("Staff Information:")
        print(f"Full Name: {self.getFullName()}")
        print(f"Employee ID: {self.__employeeID}")
        print(f"Email: {self.__email}")

   # Change the emplyee's password
    def changePassword(self, new_password):
        self.__password = new_password
        print("Password has been changed successfully.")

class Flight:
    """ A class that represents the flights"""

    # constructor
    def __init__(self, airlineName="", flightID="", departureTime="", arrivalTime="", arrivalAirport = ""):
        self.__airlineName = airlineName
        self.__flightID = flightID
        self.__departureTime = departureTime
        self.__arrivalTime = arrivalTime
        self.__arrivalAirport = arrivalAirport

    # setter and getter
    def setAirlineName(self, airlineName=""):
        self.__airlineName = airlineName

    def getAirlineName(self):
        return self.__airlineName

    def setFlightID(self, flightID=""):
        self.__flightID = flightID

    def getFlightID(self):
        return self.__flightID

    def setDepartureTime(self, departureTime=""):
        self.__departureTime = departureTime

    def getDepartureTime(self):
        return self.__departureTime

    def setArrivalTime(self, arrivalTime=""):
        self.__arrivalTime = arrivalTime

    def getArrivalTime(self):
        return self.arrivalTime

    def setArrivalAirport(self, arrivalAirport=""):
        self.__arrivalAirport = arrivalAirport

    def getArrivalAirport(self):
        return self.__arrivalAirport

    # Display the information of the flight
    def displayInfo(self):
        print("Flight Information:")
        print(f"Airline Name: {self.__airlineName}")
        print(f"Flight ID: {self.__flightID}")
        print(f"Departure Time: {self.__departureTime}")
        print(f"Arrival Time: {self.__arrivalTime}")
        print(f"Arrival Airport: {self.__arrivalAirport}")


    # A function that calculates the time flight takes to arrive to the destination
    def calculateFlightDuration(self):
        departure_datetime = datetime.strptime(self.__departureTime, "%Y-%m-%d %H:%M:%S")
        arrival_datetime = datetime.strptime(self.__arrivalTime, "%Y-%m-%d %H:%M:%S")
        duration = arrival_datetime - departure_datetime
        return duration

class Gate:
    """ A class that represents the gates that take the passengers to the airplane"""

    # constructor
    def __init__(self, terminal=0, gateNumber=0, timeBoardingOpen="", timeBoardingClose="", gateAgent=""):
        self.__terminal = terminal
        self.__gateNumber = gateNumber
        self.__timeBoardingOpen = timeBoardingOpen
        self.__timeBoardingClose = timeBoardingClose
        self.__gateAgent = gateAgent

    # setter and getter
    def setTerminal(self, terminal=""):
        self.__terminal = terminal

    def getTerminal(self):
        return self.__terminal

    def setGateNumber(self, gateNumber=""):
        self.__gateNumber = gateNumber

    def getGateNumber(self):
        return self.__gateNumber

    def setTimeBoardingOpen(self, timeBoardingOpen=""):
        self.__timeBoardingOpen = timeBoardingOpen

    def getTimeBoardingOpen(self):
        return self.__timeBoardingOpen

    def setTimeBoardingClose(self, timeBoardingClose=""):
        self.__timeBoardingClose = timeBoardingClose

    def getTimeBoardingClose(self):
        return self.__timeBoardingClose

    def setGateAgent(self, gateAgent=""):
        self.__gateAgent = gateAgent

    def getGateAgent(self):
        return self.__gateAgent

    # Display the gate's information
    def displayInfo(self):
       print("Gate Information:")
       print(f"Terminal: {self.__terminal}")
       print(f"Gate Number: {self.__gateNumber}")
       print(f"Time Boarding Open: {self.__timeBoardingOpen}")
       print(f"Time Boarding Close: {self.__timeBoardingClose}")
       print(f"Gate Agent: {self.__gateAgent}")

    # Is the gate opened for boarding
    def isBoardingOpen(self):
       current_time = datetime.now()
       boarding_open_time = datetime.strptime(self.__timeBoardingOpen, "%Y-%m-%d %H:%M:%S")
       boarding_close_time = datetime.strptime(self.__timeBoardingClose, "%Y-%m-%d %H:%M:%S")

       if boarding_open_time <= current_time <= boarding_close_time:
          return True
       else:
          return False

    # function for assigning new agent to the gate
    def assignNewGateAgent(self, new_gate_agent):
       self.__gateAgent = new_gate_agent
       print(f"Gate agent has been assigned to {new_gate_agent}.")

class BoardingPass:
    """ A class that represents the boarding pass"""

    #constructor
    def __init__(self, passangerName="", airlineName="", ticketCategory="",departurePlace="",arrivalPlace="",date="",time="",flightID="", gateDetails = "", seatPlace = "", ticketID = ""):
        self.__passengerName = passangerName
        self.__airlineName = airlineName
        self.__ticketCategory = ticketCategory
        self.__departurePlace = departurePlace
        self.__arrivalPlace = arrivalPlace
        self.__date = date
        self.__time = time
        self.__flightID = flightID
        self.__gateDetails = gateDetails
        self.__seatPlace = seatPlace
        self.__ticketID = ticketID

    #Setter and Getter
    def setPassengerName(self, passenger_name):
        self.__passengerName = passenger_name

    def getPassengerName(self):
        return self.__passengerName

    def setAirlineName(self, airline_name):
        self.__airlineName = airline_name

    def getAirlineName(self):
        return self.__airlineName

    def setTicketCategory(self, ticket_category):
        self.__ticketCategory = ticket_category

    def getTicketCategory(self):
        return self.__ticketCategory

    def setDeparturePlace(self, departure_place):
        self.__departurePlace = departure_place

    def getDeparturePlace(self):
        return self.__departurePlace

    def setArrivalPlace(self, arrival_place):
        self.__arrivalPlace = arrival_place

    def getArrivalPlace(self):
        return self.__arrivalPlace

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def setFlightID(self, flight_id):
        self.__flightID = flight_id

    def getFlightID(self):
        return self.__flightID

    def setGateDetails(self, gate_details):
        self.__gateDetails = gate_details

    def getGateDetails(self):
        return self.__gateDetails

    def setSeatPlace(self, seat_place):
        self.__seatPlace = seat_place

    def getSeatPlace(self):
        return self.__seatPlace

    def setTicketID(self, ticket_id):
        self.__ticketID = ticket_id

    def getTicketID(self):
        return self.__ticketID

    # Display the boarding pass information
    def displayInfo(self):
        print("Boarding Pass Information:")
        print(f"Passenger Name: {self.__passengerName}")
        print(f"Airline: {self.__airlineName}")
        print(f"Ticket Category: {self.__ticketCategory}")
        print(f"Departure Place: {self.__departurePlace}")
        print(f"Arrival Place: {self.__arrivalPlace}")
        print(f"Date: {self.__date}")
        print(f"Time: {self.__time}")
        print(f"Flight ID: {self.__flightID}")
        print(f"Seat Place: {self.__seatPlace}")
        print(f"Ticket ID: {self.__ticketID}")
        # Display Gate Information if available
        if self.__gateDetails:
            print("Gate Information:")
            print(f"Terminal: {self.__gateDetails.getTerminal()}")
            print(f"Gate Number: {self.__gateDetails.getGateNumber()}")
            print(f"Time Boarding Open: {self.__gateDetails.getTimeBoardingOpen()}")
            print(f"Time Boarding Close: {self.__gateDetails.getTimeBoardingClose()}")
            print(f"Gate Agent: {self.__gateDetails.getGateAgent()}")

    #Assign the gate from the Gate class
    def setGateDetailsFromGate(self, gate):
        self.__gateDetails = gate

    def updateSeatPlace(self, new_seat_place):
        self.__seatPlace = new_seat_place
        print("Seat place has been updated to", new_seat_place)

passenger1 = Passenger("Hamad", "Alnuaimi", 19, "AB1092889", "2025-10-17")
passenger1.displayInfo()
passenger1.checkPassportValidity()
if passenger1.isAdult():
    print("Passenger is an adult.")
else:
    print("Passenger is not an adult.")

print("----------------------------------------------------")

staff_member1 = Staff("Abdullah", "Aldosari", "20111234", "abdulla.password")
staff_member1.displayInfo()
staff_member1.changePassword("abdullah.newpassword")
print(staff_member1.getPassword())

print("----------------------------------------------------")

flight1 = Flight(Airline.NationalAirlines,  "NA4321", "2024-02-25 01:00:00", "2024-02-25 10:00:00", "London")
flight1.displayInfo()
print("Flight Duration:", flight1.calculateFlightDuration())

print("----------------------------------------------------")

gate1 = Gate(2, 11, "2024-02-24 00:15:00", "2024-02-24 00:40:00", "Agent Ahmed")
gate1.displayInfo()
print("Is Boarding Open:", gate1.isBoardingOpen())

gate1.assignNewGateAgent("Agent Yousef")

print("----------------------------------------------------")

boardingPass1 = BoardingPass("Hamad Alnuaimi", Airline.NationalAirlines, Ticket.FirstClass, "Abu Dhabi", "Londod","2024-02-24", "01:00:00", "NA4321", None, "A12", "629" )
boardingPass1.setGateDetails(gate1)
boardingPass1.displayInfo()
boardingPass1.updateSeatPlace("B22")