import csv

class ConnectionInfo:

    def __init__(self, from_station, to_station, colour, connection_type, length, number_of_locomotives):
        self.from_station = from_station
        self.to_station = to_station
        self.colour = colour
        self.connection_type = connection_type
        self.length = length
        self.number_of_locomotives = number_of_locomotives

    def stringify(self):
       return 'Connection from ' + self.from_station + ' to ' + self.to_station + ' is a ' + self.colour + ' ' + self.connection_type + ' connection and has ' + self.length + ' wagons (including ' + self.number_of_locomotives + ' locomotives).'


def parse(file_path):
    with open (file_path) as connections_file:
        reader = csv.reader(connections_file, delimiter=',')
        is_first_line = True
        connection_infos = []
        
        for line in reader:
            if is_first_line:
                is_first_line = False
            else:
                connection_info = ConnectionInfo(line[0], line[1], line[2], line[3], line[4], line[5])
                connection_infos.append(connection_info)

        return connection_infos

connection_infos = parse('maps/nordic_countries.csv')
for connection_info in connection_infos:
    print(connection_info.stringify())
