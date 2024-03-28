# Initialize list to store meal costs
meal_costs = []

while True:
    # Ask user if they want to add a charge or not
    response = input("\nDo you want to add a charge or sum? (add/sum): ")
    
    if response.lower() == 'add':
        while True:  # Keep asking until we get valid input
            cost = input("Please enter the charge for food: ")
            
            # check if float
            is_float = cost.replace('.', '').isdigit()
            
            if not is_float:
                print("Invalid input. Please enter a charge. Like 12.99")
                continue   # If not valid, ask again
            
            cost = float(cost)  # Convert string to float if it's a number
            
            if cost < 0:  
                print("Cost cannot be negative.")
            else:
                break
        
        meal_costs.append(cost)   # Add cost of meal to list
    
    elif response.lower() == 'sum' and len(meal_costs) > 0:  # If no, but they have added some meals, break the loop
        break  
    
    else:
        print("You haven't entered any charge yet.")
        
# Initialize total cost to 0
total_cost = 0

for meal in meal_costs:
    
    # Calculate tip (18%) and tax (7%) for each meal
    tip = meal * 0.18
    tax = meal * 0.07
    
    # Add the cost of this meal, along with its tip and tax, to the total cost
    total_cost += meal + tip + tax
        
# Print the results
for i in range(len(meal_costs)):
    print("\nCost of meal", (i+1), ": $", format(meal_costs[i], '.2f'))

print("Total cost including tips and taxes: $", format(total_cost, '.2f'))