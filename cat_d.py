def cat_mouse(map_, moves):
    if 'C' not in map_ or 'm' not in map_:
        return 'boring without two animals'
    
    for row, line in enumerate(map_.splitlines()):
        if 'C' in line:
            cat = row, line.index('C')
        if 'm' in line:
            mouse = row, line.index('m')
    
    distance = abs(cat[0] - mouse[0]) + abs(cat[1] - mouse[1])
    
    return 'Caught!' if distance <= moves else 'Escaped!'