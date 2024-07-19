'''
Railway system

attributes:
    - no of seats
    - fare
    - list of seats

method:
- displaying no of seats avialable and fare of seat
- book a ticket
- cancel the ticket

'''

class Train:
    def __init__(self, tname, tseats, tfare):
        self.tname = tname
        self.tseats = tseats
        self.tfare = tfare
        self.seatList = list(range(1, tseats + 1))

    
    def info(self):
        print(f"train name: {self.tname} and fare is: {self.tfare}")
        print(f"seats available: {self.seatList}")
    
    def bookTicket(self, noOfTickets):
        if noOfTickets <= len(self.seatList):
            for _ in range(noOfTickets):
                seatNo = self.seatList.pop()
                print(f"{seatNo} is booked")
            print(f"Please pay: {noOfTickets * self.tfare} ")
        else:
            print("No of tickets are exceeding")
            print(f"No of seats available: {len(self.seatList)}")
            print(f"Seats available: {self.seatList}")

        
    def cancelTicket(self, ticketNumber):
        if ticketNumber <= 0 or ticketNumber > self.tseats:
            print("Enter the valid ticket number")
        else:
            self.seatList.append(ticketNumber)
            print(self.seatList)
            print(f"Ticket {ticketNumber} is cancelled")




t1 = Train("Rajdhani Express", 5, 50)
# t1.info()   
t1.bookTicket(3)
t1.cancelTicket(5)
t1.info()