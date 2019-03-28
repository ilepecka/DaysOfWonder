import csv

class TicketInfo:

    def __init__(self, from_station, to_station, points):
        self.from_station = from_station
        self.to_station = to_station
        self.points = points

    def stringify(self):
       return 'Ticket from {} to {} is worth {} points'.format(self.from_station, self.to_station, self.points)


def parse_ticket(file_path):
    with open (file_path) as ticket_file:
        reader = csv.reader(ticket_file, delimiter=',')
        is_first_line = True
        ticket_infos = []
        
        for line in reader:
            if is_first_line:
                is_first_line = False
            else:
                ticket_info = TicketInfo(line[0], line[1], line[2])
                ticket_infos.append(ticket_info)

        return ticket_infos

ticket_infos = parse_ticket('tickets/nordic_countries_tickets.csv')
for ticket_info in ticket_infos:
    print(ticket_info.stringify())
