"""
Consider a user who is willing to take up to k connections from their origin city A to their destination B.
Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.
"""
def append_ticket(tickets, new_tickets):
	appended_tickets = []
	for new_ticket in new_tickets:
		for ticket in tickets:
			if ticket[1] == new_ticket[0]:
				appended_tickets.append((new_ticket[0], new_ticket[1], new_ticket[2] + ticket[2], (ticket[3]+(new_ticket[1], ))))
	if appended_tickets != []:
		return appended_tickets + tickets
	else:
		return new_tickets + tickets

def get_price(ticket):
	return ticket[2]

data = [
	('JFK', 'ATL', 150),
	('ATL', 'SFO', 400),
	('ORD', 'LAX', 200),
	('LAX', 'DFW', 80),
	('JFK', 'HKG', 800),
	('ATL', 'ORD', 90),
	('JFK', 'LAX', 500),
]

data = [(i[0], i[1], i[2], (i[0],i[1])) for i in data]
tickets = []
depart = ['JFK']
destination = 'ORD'

while depart != []:
	new_tickets = [i for i in data if i[0] in depart]
	
	tickets = append_ticket(tickets,new_tickets)
	print(tickets)
	depart = [i[1] for i in new_tickets if i[1] != destination]

tickets = [i for i in tickets if i[1] == destination]
tickets.sort(key=get_price)

print("The Best tickets::::")
for ticket in tickets:
	print(ticket[3], ticket[2])
