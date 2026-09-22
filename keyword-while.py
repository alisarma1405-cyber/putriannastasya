should_continue = True

while should_continue:
    n = int(input("enter an even greater than 0: "))
    
    if n <= 0 or n % 2 == 1:
        print(n, "is not an even greater than 0")
        should_continue = False
    else:
        print("number", n)