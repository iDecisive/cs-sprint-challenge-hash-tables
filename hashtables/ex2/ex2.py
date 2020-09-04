#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    ticketHT = {}
    for i in range(length):
        ticketHT[tickets[i].source] = tickets[i].destination

    route = []
    current = ticketHT["NONE"]

    while current != "NONE":
        route.append(current)
        current = ticketHT[current]
    route.append(current)
    
    return route
