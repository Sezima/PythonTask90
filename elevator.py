'Closest elevator'
def elevator(left, right, call):
    l = abs(call - left);
    r = abs(call - right);
    if l >= r:
        return "right";
    if l < r:
        return "left"; 