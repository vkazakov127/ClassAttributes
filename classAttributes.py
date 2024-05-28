class Building:
    totals = 0
    def __init__(self):
        Building.totals += 1

houses = []
for i in range(40):
    houses.append(Building())
    print(houses[i]) # Building object
    print(f'houses[{i}]. Totals = {Building.totals}')
