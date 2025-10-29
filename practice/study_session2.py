LIMIT = 20

def get_number(number_type):
    while True:
        try:
            entry = input("Enter the number: ")

            if number_type == "integer":
                num = int(entry) #int hace referencia a numeros enteros 
            else:
                num = float(entry) #float hace referencia a numeros 

            if num < LIMIT:
                return num
            else:
                print("THE NUMBER MUST BE LESS THAN 20")

        except ValueError:
            print("Please enter a valid number")

# Main program
NUMBER1 = get_number("integer")
NUMBER2 = get_number("decimal")

result = NUMBER1 + NUMBER2
print("The result is:", result)