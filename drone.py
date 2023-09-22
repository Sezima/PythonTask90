'drone fly by'
def fly_by(lamps, drone):
    l = len(drone)
    return ''.join(['o' if i < l else 'x' for i in range(len(lamps))])

