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


#Calculate everything
def calculate_all(weight):
    return {
        "ground": ground_shipping(weight),
        "premium": 125.00,
        "drone": drone_shipping(weight)
    }


def cheapest_option(costs):
    method = min(costs, key=costs.get)
    return method, costs[method]


def validate_weight(weight):
    if weight <= 0:
        raise ValueError("Weight must be greater than 0!")


def main():
    weight = float(input("Enter the weight of your package here: "))

    validate_weight(weight)

    costs = calculate_all(weight)
    method, price = cheapest_option(costs)

    print(costs)
    print(f"Cheapest: {method} -> ${price}")


if __name__ == "__main__":
    main()
