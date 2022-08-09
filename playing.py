print("Hello World")
doing = input("What is are you doing right now Shaun?")
print(f"Silly goose {doing} is not what you are paid to do Silly")

class EssentialFunctions():
    def __init__(self) -> None:
        self.prompt = "What would you like to do?: \n [0]Calculate Percentage \n [1]Calculate Additional Percentage \n [2]Calculate Discounted Price"
        self.actions = {0:self.calculate_percentage,1:self.calculate_seccond_discount,2:self.calculate_discounted_price}
    def calculate_percentage(self):
        """Calculate the percentage given an origninal price and discounted price"""
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
                if float(0) == original:
                    print("ZEROS ARE RUDE DONT USE THEM")
                    continue

                break
            print("TOOFAR SOMETHING IS BROKEN")
            break
        print("The calculated percentage is.")
        print(f"{(1.0-(discounted/original))*100:.2f}%")

    
    def calculate_seccond_discount(self):
        """Calculate an increased percentage given an original price discounted price and the percentage to add
        E.G. 20% off an item discounted from 15% off"""
        curr_price = None
        original_price = None
        add_percentage = None
        while True:
            try: #Collect all inputs as floats
                current_price = float(input("What is the current price of the item?"))
                original_price = float(input("What was the original price of the item?"))
                add_percentage = float(input("What is the additional percentage you would like to add?"))/100
            except: #Catch any errors arrising from incomplete inputs
                print("There was an error with one of your inputs. Starting from the begining.")
                continue
            else:
                if 0 in (current_price,original_price,add_percentage):
                    print("ZEROS ARE RUDE DONT USE THEM")
                    continue
                calculated_percentage = 100*(1-(current_price-(add_percentage*current_price))/original_price)
                print(f"The new calculated percentage is {calculated_percentage:.2f}%")
                break
    
    def calculate_discounted_price(self):
        """Calcualte the discounted price given a discount percentage and price"""
        current_price = None
        percent_off = None
        while True:
            try:
                current_price = float(input("What is the current price of the product?"))
                percent_off = float(input("What is the percentage off?"))/100
            except:
                print("There was an error with one of your inputs. Starting from the begining.")
                continue
            else:
                new_price = current_price-(current_price*percent_off)
                print(f"Your discounted price is ${new_price}!")

    def run_interactive(self):
        action_input = None
        while True:
            try:
                action_input = int(input(f"{self.prompt}"))
            except:
                print("Sorry. There was an error with your input please try again \n")
                print("###################################################################")
                continue
            else:
                self.actions[action_input]

test = EssentialFunctions()

test.run_interactive()

#test.calculate_percentage()
#test.calculate_seccond_discount()