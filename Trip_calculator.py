city = str(input('Where do you want to go, Madrid, Warsaw, Rome or Prague?: '))
days = int(input('How many days do you want to spend?: '))
spending_money = int(input('How much money do you want to spend?: '))

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Madrid":
    return 183
  elif city == "Warsaw":
    return 220
  elif city == "Rome":
    return 222
  elif city == "Prague":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print(trip_cost(city, days, spending_money))

