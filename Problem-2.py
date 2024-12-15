def generate_series(a):
    if a < 1:
        print("Input must be a positive integer.")
        return

    result = []
    for i in range(a):
        result.append(1 + 2 * i)  

    print(", ".join(map(str, result)))  
a = int(input("enter the number:")) 
generate_series(a)