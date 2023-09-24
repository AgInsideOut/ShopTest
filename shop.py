""" Simple Shop Program
Using exception handling code blocks such as try/ except / else / finally, write a program that simulates a customer in a shop
(NB: the more code blocks the better, but try to use at least two key words e.g. try/except, raise)
Tasks:
Create a dictionary with a minimum of 3 items and prices
One of the items needs to cost more than £100
Customer's available money is £100
Welcome the customer and display the items and their prices, along with an option to “exit” 
Accept the option as an input, an invalid input should raise a ValueError 
If the customer can afford it, print out a message saying “Here's your {item}!” 
The user should be then greeted out of the shop, and the program terminated.
If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
The purchase should be tried a maximum of 3 items, if it fails a custom error should be raised and the customer will exit the shop.
"""

class MaximumAttemptsReachedError(Exception):
    pass

class InsufficientBudgetError(Exception):
    pass

class NoDesireToBuyError(Exception):
    pass

class NoItemAvailable(Exception):
    pass

apparel = {
    1: {"panda t-shirt": 20.99},
    2: {"low-rise jeans": 49.99},
    3: {"turtleneck sweater": 59.99},
    4: {"wrap dress": 79.99},
    5: {"flat shoes": 89.99},
    6: {"sun hat": 14.99},
    7: {"trench coat": 69.99},
    8: {"a-line skirt": 34.99},
    9: {"tailored tuxedo": 899.99},
    10: {"bermuda shorts": 24.99}
}

def check_attempts(attempts, max_attempts):
    if attempts > max_attempts:
        raise MaximumAttemptsReachedError("Maximum attempts reached.")
    else:
        return True  

def check_item_availability(item_id):
    if item_id in apparel:
        return True
    else:
        raise NoItemAvailable("\nSorry, the item you're looking for is unavailable.")

def check_funds(item_price, customer_budget):
    if item_price <= customer_budget:
        return True
    else:
        raise InsufficientBudgetError("\nSorry, the sum is not enough to buy the item.")
    
def check_add_funds(attempts, max_attempts, item_price, customer_budget):
    trials = max_attempts - attempts
    for t in range(trials):
        attempts += 1
        additional_money = float(input("Do you have additional money? Enter the additional amount: "))
        customer_budget += additional_money
        if customer_budget >= item_price:
            success = True
            break  
        else:
            success = False
    return success

def check_place_order(request):
    if request.upper() == "EXIT":
        raise NoDesireToBuyError("\nI see that you want to leave, have a wonderful day then!")
    else:
        return True

def customer_service():
    attempts = 1
    max_attempts = 3
    customer_budget = 100
    
    while True:
        try:
            # Check attempts
            check_attempts(attempts, max_attempts)
            
            # Check purchase desire
            print("\nHello, today we sell:\n")
            for id, item in apparel.items():
                item_name, price = list(item.items())[0]
                print(f"The item {id}: {item_name}: £{price}")
            request = input("\nWould you be interested in buying anything? Please provide the item ID or type EXIT.\t")
            check_place_order(request)
            
            # Check item availability
            item_id = int(request)
            check_item_availability(item_id)
            
            # Check balance
            item_price = list(apparel[item_id].values())[0]
            check_funds(item_price, customer_budget)
            
            # If four checks pass, break the loop and continue with the purchase
            break
        
        except MaximumAttemptsReachedError as e:
            print(str(e))
            return
        except NoDesireToBuyError as e:
            print(str(e))
            return
        except NoItemAvailable as e:
            print(str(e))
            attempts += 1
        except InsufficientBudgetError as e:
            print(str(e))
            success = check_add_funds(attempts, max_attempts, item_price, customer_budget)
            if success == True:
                break
            else:
                print("\nMaximum attempts reached. Sorry, you need to leave.")
                return
            
    # Final message
    item_name = list(apparel[item_id].keys())[0]
    print(f"\nHere's your {item_name}! Goodbye.")

customer_service()
