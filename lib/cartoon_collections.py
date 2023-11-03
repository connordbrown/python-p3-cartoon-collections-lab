def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")

def summon_captain_planet(planeteer_elements):
    return [f'{element.title()}!' for element in planeteer_elements]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    for item in ingredients:
        if item in ["cheddar", "gouda", "camembert"]:
            return item
    return None
