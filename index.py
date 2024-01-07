from models.ordermenu import OrderMenu
def HomeScreen():
    print("Welcome to the delicious deli how can we help?")
    
    while(True):
        print("1 : New Order")
        print("2 : Quit ")
        choice = input("")
        
        if(choice == "1"):
            print("Starting the order")
            menu = OrderMenu()
            try:
                menu.run()

               
            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("Quitting the application")
            

            
     
     
