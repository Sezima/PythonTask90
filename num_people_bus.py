def number(bus_stops):
    return sum([i - k for i, k in bus_stops])
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])