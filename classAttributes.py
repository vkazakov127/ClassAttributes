class Building:
    totals = 0
    def __init__(self):
        Building.totals += 1

house = []
for i in range(40):
    house.append(Building())
    print(f'house[{i}]. Totals = {house[i].totals}')
