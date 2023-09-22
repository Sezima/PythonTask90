'Playing with cubes II'
class Cube(object):
    def __init__(self, n = 0):
        self._side = abs(n)
        
    def get_side(self):
        return self._side

    def set_side(self, new_side):
        self._side = abs(new_side)