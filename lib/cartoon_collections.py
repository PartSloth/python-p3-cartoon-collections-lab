def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf) + 1}. {dwarf}')

def summon_captain_planet(planeteers):
    list = [planeteer.capitalize() + "!" for planeteer in planeteers]
    return list

def long_planeteer_calls(words):
    for word in words:
        if(len(word) > 4):
            return True
    return False

def find_the_cheese(foods):
    cheese_check = [food for food in foods if food == "cheddar" or food == "gouda" or food == "camembert"]
    if(len(cheese_check) == 1):
        return cheese_check[0]
    else:
        return None