
"""
Bus fare calculator

This program calculates how much money I spend on bus rides.
It asks for the number of regular rides and rush hour rides,
calculates the cost for each type, and adds them together
to show the total amount spent on bus fares.
"""


def bus_ride_cost_calculator(fare_type):
    # This function calculates the cost of bus rides for one type of fare.
    # The fare_type parameter tells us whether we are calculating regular
    # fares or rush hour fares, so we can reuse the same function twice.

    # Ask the user how many times they rode the bus using this fare type.
    # int() converts the answer into a whole number because rides are counted
    # as whole numbers, such as 3 rides or 10 rides.
    number_of_rides = int(input(
        f'How many times did you ride the bus paying {fare_type} fares? '
    ))

    # Ask how much one bus ticket costs for this type of fare.
    # float() allows the user to enter a price with decimals, such as 2.50.
    bus_fare = float(input(
        f'What is the cost of one {fare_type} bus ticket? $'
    ))

    # Multiply the number of rides by the price of one ticket.
    # For example, 5 rides at $2.50 each would cost $12.50.
    total_cost = number_of_rides * bus_fare

    # Show the number of rides and the price of one ticket.
    # :.2f makes the ticket price display two decimal places,
    # which is the usual way to display money.
    print(
        f'You rode the bus {number_of_rides} times '
        f'and each ride costs ${bus_fare:.2f}'
    )

    # Show how much the user spent on this type of fare.
    # The fare_type variable makes the message say either regular or rush hour.
    print(f'Your total {fare_type} expense is ${total_cost:.2f}')

    # Send the calculated cost back to the part of the program
    # that called this function, so it can be used in another calculation.
    return total_cost


def main():
    # Display the program title so the user knows what the program does.
    print('Bus fare calculator program')

    # Call the calculator function to calculate regular bus expenses.
    # The returned amount is saved in total_regular_cost for later use.
    total_regular_cost = bus_ride_cost_calculator('regular')

    # Call the same function again for rush hour expenses.
    # Only the argument changes, so we do not need to write the
    # calculation code a second time.
    total_rush_hour_cost = bus_ride_cost_calculator('rush hour')


    total_special_discount_cost = bus_ride_cost_calculator('special discount')

    # Add the regular fare cost and rush hour fare cost and special discount cost together
    # to find the total amount spent on all bus rides.
    total_bus_expense = total_regular_cost + total_rush_hour_cost + total_special_discount_cost

    # Display the final amount spent on all bus rides.
    # :.2f makes sure the final amount always has two decimal places.
    print(f'Your total expense is ${total_bus_expense:.2f}')


# Call main() to start the program.
# Defining a function does not automatically run it, so we call it here.
main()
