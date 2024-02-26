from funcs import *
from country import *


def main():
    connector = open_connection()
    country = Country(connector)

    try:
        while True:
            print("="*15)
            print("1. Insert")
            print("2. Print")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")
            print("="*15)
            choice = input("Pick one: ")
            
            while choice.strip().isdigit() == False or int(choice) > 5 or int(choice) < 1:
                choice = input("Pick a number between 1-5: ")
            choice = int(choice)

            if choice == 1:
                country.insert()
                print(country)
            elif choice == 2:
                print("="*15)
                print("1. Print all countries(detailed)")
                print("2. Print all countries(Simple)")
                print("3. Print countries by continent")
                print("4. Print a country by name")
                print("5. Print a country by code") 
                print("6. Print countries by population")
                print("7. Print a country's languages")
                print("8. Print a country's cities")
                print("9. Print biggest cities by population")
                print("10. Print countries by GDP")
                print("11. Print a language's countries")
                print("12. Print a city")
                print("="*15)

                choice = input("Pick one: ")
                while choice.strip().isdigit() == False or int(choice) > 12 or int(choice) < 1:
                    choice = input("Pick a number between 1-12: ")
                choice = int(choice)    
                country.print_choice(choice) 

            elif choice == 3:
                country.update()
            elif choice == 4:
                country.delete()
            elif choice == 5:
                print("Goodbye!")
                break           
    except MYSQL.Error as e:
        print(e)  

    close_connection(connector)      

main()        