while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            print("You selected Option 1.")
            

        elif choice == 2:
            print("You selected Option 2.")
        

        elif choice == 3:
            print("You selected Option 3.")
            

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break 

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


