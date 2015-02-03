# Define function "total" and declare parameters
def total(initial = 5, *numbers, **keywords): 
    count = initial 
    for number in numbers:
        # Count = count + number
        count += number
    for key in keywords:
        # Count = count + keywords
        count += keywords [key]
    return count
    
print total(10, 1, 2, 3, vegetables = 50, fruits = 100)
        