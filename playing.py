print("Hello World")
doing = input("What is are you doing right now Shaun?")
print(f"Silly goose {doing} is not what you are paid to do Silly")

class EssentialFunctions():
    def __init__(self) -> None:
        pass

    def calculate_percentage():
        original = None
        discounted = None
        while True:
            try:
                original = float(input("What was the original price?"))
                discounted = float(input("What is hte discounted price?"))
            except:
                print("Im sorry I didnt understand one of your price inputs.")
                continue
            else:
                break
            print("TOOFAR")
            break
        print(original+discounted)


test = EssentialFunctions()
test.calculate_percentage()