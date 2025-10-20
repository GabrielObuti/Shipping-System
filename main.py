weight = float(input("Enter the weight of your package here: "))

#Ground Shipping
def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.50 + 20
  elif weight <= 6:
    return weight * 3.00 + 20
  elif weight <= 10:
    return weight * 4.00 + 20
  else:
    return weight * 4.75 + 20

cost_ground = ground_shipping(weight)
print(f"Ground Shipping: ${cost_ground}")

#Premium Ground Shipping
premium_ground_shipping = 125.00
print(f"Premium Ground Shipping: ${premium_ground_shipping}")

#Drone Shipping
def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight <= 6:
    return weight * 9.00
  elif weight <= 10:
    return weight * 12.00
  else:
    return weight * 14.25

cost_drone = drone_shipping(weight)
print(f"Drone Shipping: ${cost_drone}")

#Determine the cheapest shiping method
cheapest = min(cost_ground, premium_ground_shipping, cost_drone)
if cheapest == cost_ground:
  print(f"The cheapest option is Ground Shipping: ${cost_ground}")
elif cheapest == premium_ground_shipping:
  print(f"The cheapest option is Premium Ground Shipping: ${premium_ground_shipping}")
else:
  print(f"The cheapest option is Drone Shipping: ${cost_drone}")

