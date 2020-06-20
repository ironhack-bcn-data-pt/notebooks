def convert_units(heroes, heights, weights): 
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]
    hero_data = {}
    for i,hero in enumerate(heroes): 
        hero_data[hero] = (new_hts[i], new_wts[i])
    
    return hero_data