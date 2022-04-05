# numvber checking function
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# ****** MAIN ROUTINE STARTS HERE *********

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()


# Start of calculator loop
keep_going = ""
while keep_going == "":
    
    # get width, length and cost checking for valid input with a 
    # number checking function
    width = num_check("width: ")
    length = num_check("length: ")
    cost_per_meter = num_check("cost per meter: $")
    
    # calculate the perimeter and area
    perimeter = 2 * (width + length)
    cost_p_meter = (perimeter * cost_per_meter)

    # output Cost and perimeter
    print()
    print("Perimeter: {:.2f} units".format(perimeter))
    print()
    print("Costs: ${:.2f}".format(cost_p_meter))
    
    keep_going = input("Press {<enter>} to keep going or any key to quit")

    print()
    print("-" * 30)
    print()
    
print()
print("Thanks for using the Fencing cost calculator")