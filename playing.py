print("Hello World")
doing = input("What is are you doing right now Shaun?")
print(f"Silly goose {doing} is not what you are paid to do Silly")

class EssentialFunctions():
    def __init__(self) -> None:
        pass

    def calculate_percentage(self):
        original = None
        discounted = None
        print("Please enter all amounts without the currency symbol.")
        while True:
            try:
                original = float(input("What was the original price?"))
                discounted = float(input("What is the discounted price?"))
            except:
                print("Im sorry I didnt understand one of your price inputs.")
                continue
            else:
                break
            print("TOOFAR SOMETHING IS BROKEN")
            break
        print("The calculated percentage is.")
        print((1.0-(discounted/original))*100)


test = EssentialFunctions()
test.calculate_percentage()