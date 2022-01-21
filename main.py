class garage():
    
        def __init__(self):
            self.cars_added = []
            self.spots = {'a1': '','a2': '', 'b1': '', 'b2': '', 'c1': '', 'c2':'', 'd1': '', 'd2': '', 'e1': '', 'e2': ''}
            self.carinfo = {}
            self.bill = None

        
        def add_car(self):
            print(f"Here are the spots available: {self.spots}")
            add = input("What spot would you like? ")
            for key,value in self.spots.items():
                if key == add and value == '':
                    self.spots[add] = 'taken'
                elif key == add and value == 'taken':
                    print("This spot is taken.")   




        def spots_available(self):
            print("Any spot with a blank ticket is empty. ('')")
            print(f"These are the spots available: {self.spots}")

        def remove_car(self):
            hour = int(input("Enter how long you were in parking spot (Enter hours rounded up.)? "))
            bill = hour * 5
            print(f"You owe: ${bill}")
            paid = input("Would you like to pay this now ('yes'/'no')? ")
            if paid == 'yes':
                print(f"{self.spots}")
                who_car = input("Which vehicle belongs you? ")
                for key, value in self.spots.items():
                    if key == who_car and value == 'taken':
                        del self.spots[who_car]
                        self.spots[who_car] = ''
                        print("Have a great day!")
                    elif key == who_car and value == '':
                        print("There is no car here.")
            elif paid == 'no':
                print(f"Gtfo, we're keeping your car.")

        def run(self):
            while True:
                user = input("What did you want to do? 'P' = park, 'L' = leave , 'S' = show spots available: ")
                user = user.lower()
                if user == 'p':
                    mygarage.add_car()
                elif user == 'l':
                    mygarage.remove_car()
                elif user == 's':
                    mygarage.spots_available()


mygarage = garage()
print(mygarage.run())

