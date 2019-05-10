import sys 
import re

class City:
    def __init__(self, name, lat, lon ,node, ):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.node = node



def main():

    solved = open(sys.argv[1],"r")
    input = open(sys.argv[2],"r")

    node_list = []

    for line in input:
        if ":" not in line and "NODE_COORD_SECTION" not in line:
            line = line.lstrip().rstrip().lower()
            if 'eof' in line:
                break
            
            vls = line.split(' ')
            city = City(str(vls[5]),float(vls[1]),float(vls[2]), int(vls[0])-1)
            node_list.append(city)

    import operator
    node_list.sort(key=operator.attrgetter('node'))

    # Empty dict 
    dict = {}

    for line in solved:
        if 'arc ' in line:
            line = line.lstrip().rstrip().lower()
        
            pair = re.findall(r'\d+', line)
            dict[pair[0]] = pair[1]
            
    next_city = None
    tot_dist = 0

    sorted_nodelist = []

    for i in dict:
        if next_city == None:
            sorted_nodelist.append(node_list[0])
            next_city= int(dict["0"])
        
        sorted_nodelist.append(node_list[next_city])
        next_city= int(dict[str(next_city)])
    
    previous_lat = None
    previous_lon = None

    for i in sorted_nodelist:
        print(i.name)
        if previous_lat != None:
            tot_dist += calc_distance(i.lat, i.lon, previous_lat, previous_lon)
        previous_lat = i.lat
        previous_lon = i.lon

    print(f"Total distance:",tot_dist)
            
def calc_distance(lat1, lon1, lat2, lon2):
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


if __name__ == "__main__":
    main()