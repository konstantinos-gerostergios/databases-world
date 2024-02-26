from funcs import *

class Country:
    def __init__(self, connector):
        self.connector = connector
        self.code = None
        self.name = None
        self.continent = None
        self.region = None
        self.surface_area = None
        self.indep_year = None
        self.population = None
        self.life_expectancy = None
        self.gnp = None
        self.gnp_old = None
        self.local_name = None
        self.government_form = None
        self.head_of_state = None
        self.code2 = None
        self.capital = None

    def __str__(self):
        return f"{self.name} ({self.region} , {self.continent})"

    #inserts a country or a city based on user input
    def insert(self):
        print("="*15)
        print("INSERT SUB-MENU")
        print("="*15)
        print("1. Insert a country")
        print("2. Insert a city")
        print("="*15)
        choice = input("Pick one: ")
        while choice.strip().isdigit() == False or int(choice) > 2 or int(choice) < 1:
            choice = input("Pick a number between 1-2: ")
        choice = int(choice)

        if choice == 1:
            #check for code condition
            self.code = input("Country Code: ")  
            while len(self.code) != 3:
                print("Code must be 3 characters long")
                self.code = input("Country Code: ")   

            #check if code already exists
            query = "SELECT * FROM country WHERE code ='" + self.code + "'"
            results = query_full_results(self.connector, query)
            while len(results) > 0:
                print("Country already exists")
                self.code = input("Country Code: ")
                while len(self.code) != 3:
                    print("Code must be 3 characters long")
                    self.code = input("Country Code: ")
                query = "SELECT * FROM country WHERE code ='" + self.code + "'"
                results = query_full_results(self.connector, query)

            #starting to insert
            self.name = input("Country Name: ")
            self.continent = input("Continent: ")
            self.region = input("Region: ")
            self.surface_area = float(input("Surface Area: "))
            inp = input("Independence Year (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.indep_year = None
            else:
                self.indep_year = int(inp)
            self.population = int(input("Population: "))    
            inp = input("Life Expectancy (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.life_expectancy = None
            else:
                self.life_expectancy = float(inp)
            inp = input("GNP (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.gnp = None
            else:
                self.gnp = float(inp)
            inp = input("GNP Old (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.gnp_old = None
            else:
                self.gnp_old = float(inp)
            self.local_name = input("Local Name: ")
            self.government_form = input("Government Form: ")
            inp = input("Head of State (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.head_of_state = None
            else:
                self.head_of_state = inp
            inp = input("Capital (Type None if it is unknown): ")
            if inp == "None" or inp  == "none":
                self.capital = None
            else:
                self.capital = inp
            self.code2 = input("Code2: ")

            query = "INSERT INTO country "
            query += "VALUES (" 
            query += "'" + self.code + "', "
            query += "'" + self.name + "', "
            query += "'" + self.continent + "', "
            query += "'" + self.region + "', "
            query += str(self.surface_area) + ", "
            if self.indep_year == None:
                query += "NULL, "
            else:
                query += str(self.indep_year) + ", "
            query += str(self.population) + ", "
            if self.life_expectancy == None:
                query += "NULL, "
            else:
                query += str(self.life_expectancy) + ", "
            if self.gnp == None:
                query += "NULL, "
            else:
                query += str(self.gnp) + ", "
            if self.gnp_old == None:
                query += "NULL, "
            else:
                query += str(self.gnp_old) + ", "
            query += "'" + self.local_name + "', "
            query += "'" + self.government_form + "', "
            if self.head_of_state == None:
                query += "NULL, "
            else:
                query += "'" + self.head_of_state + "', "
            if self.capital == None:
                query += "NULL, "
            else:
                query += str(self.capital) + ", "
            query += "'" + self.code2 + "' )"

            insert_query(self.connector, query)
            self.connector.commit()
            print("Country inserted successfully")

        #insert a city
        else:
            name = input("City Name: ")
            country_code = input("Country Code: ")
            district = input("District: ")
            population = int(input("Population: "))

            query = "INSERT INTO city "
            query += "VALUES (" 
            query += "NULL, "
            query += "'" + name + "', "
            query += "'" + country_code + "', "
            query += "'" + district + "', "
            query += str(population) + ")"

            insert_query(self.connector, query)
            self.connector.commit()
            print("City inserted successfully")

    #print a country detailed
    def print_country(self, country):
        print("="*35)
        print(f"Code: {country['Code']}")
        print(f"Name: {country['Name']}")
        print(f"Continent: {country['Continent']}")
        print(f"Region: {country['Region']}")
        print(f"Surface Area: {country['SurfaceArea']}")
        print(f"Independence Year: {country['IndepYear']}")
        print(f"Population: {country['Population']}")
        print(f"Life Expectancy: {country['LifeExpectancy']}")
        print(f"GNP: {country['GNP']}")
        print(f"GNPold: {country['GNPOld']}")
        print(f"Local Name: {country['LocalName']}")
        print(f"Government Form: {country['GovernmentForm']}")
        print(f"Head of State: {country['HeadOfState']}")
        print(f"Capital: {country['Capital']}")
        print(f"Code2: {country['Code2']}")
        return 1

    #prints based on the user's choice
    def print_choice(self ,choice):   
        if choice == 1:
            query = "SELECT * FROM country"
            results = query_iter_many(self.connector,10, query)
            for countries in results:
                for country in countries:
                    self.print_country(country)
                print("="*10 + ". Next? Press Enter...", end="")
                input()
        elif choice == 2:   
            iter_query = query_iter_many(self.connector, 10, "SELECT * FROM country")
            for countries in iter_query:
                for country in countries:
                    print(f"{country['Name']}({country['Continent']}). ")
                print("="*10 + ". Next? Press Enter...", end="")
                input()   
        elif choice == 3:
            continent = input("Continent: ")
            query = "SELECT * FROM country WHERE continent='" + continent + "'"
            results = query_iter_many(self.connector,10, query)
            for countries in results:
                for country in countries:
                    print(f"{country['Name']} ({country['Region']}) - {country['Population']}")
                print("="*10 + ". Next? Press Enter...", end="")
                input()
        elif choice == 4:
            name = input("Country Name: ")
            query = "SELECT * FROM country WHERE name='" + name + "'"
            results = query_full_results(self.connector, query)
            if len(results) == 0:
                print("Country not found")
            else:
                self.print_country(results[0])
        elif choice == 5:
            code = input("Country Code: ")
            query = "SELECT * FROM country WHERE code='" + code + "'"
            results = query_full_results(self.connector, query)
            if len(results) == 0:
                print("Country not found")
            else:
                self.print_country(results[0])  
        elif choice == 6:    
            el_choice = input("MIN-1, MAX-2: ") 
            while el_choice.strip().isdigit() == False or int(el_choice) > 2 or int(el_choice) < 1:
                el_choice = input("Pick a number between 1-2: ")
            el_choice = int(el_choice)  
            if el_choice == 1:
                query = "SELECT * FROM country ORDER BY population ASC"
                results = query_iter_many(self.connector,10, query)
                for countries in results:
                    for country in countries:
                        print(f"{country['Name']} ({country['Region']} , {country['Continent']}) - {country['Population']}")
                    print("="*10 + ". Next? Press Enter...", end="")
                    input()
            else:
                query = "SELECT * FROM country ORDER BY population DESC"
                results = query_iter_many(self.connector,10, query)
                for countries in results:
                    for country in countries:
                        print(f"{country['Name']} ({country['Region']} , {country['Continent']}) - {country['Population']}")
                    print("="*10 + ". Next? Press Enter...", end="")
                    input()
        elif choice == 7:
            country = input("Country Name: ")
            test_query = "SELECT * FROM country WHERE name='" + country + "'"
            results = query_full_results(self.connector, test_query)
            if len(results) == 0:
                print("Country not found")
                return
            else:
                query = "SELECT c.Name, cl.Language, IsOfficial, Percentage FROM country c join countrylanguage cl on c.Code = cl.CountryCode \
                    where c.Name='" + country + "' ORDER BY Percentage DESC"
                results = query_full_results(self.connector, query)
                print(f"Country: {results[0]['Name']}")
                for result in results:
                    print(f"Language: {result['Language']} - Isofficial: {result['IsOfficial']} - Percentage: {result['Percentage']}")
        elif choice == 8:
            country = input("Country Name: ")
            country_query = "SELECT Name, Continent, Region, Code FROM country WHERE name='" + country + "'"
            country_ret = query_full_results(self.connector, country_query)
            if len(country_ret) == 0:
                print("Country not found")
                return
            else:
                print(f"Country: {country_ret[0]['Name']} ({country_ret[0]['Region']} , {country_ret[0]['Continent']})")
                city_query = "SELECT Name, District, Population FROM city WHERE CountryCode='" + country_ret[0]['Code'] + "' ORDER BY Population DESC"
                city_results = query_full_results(self.connector, city_query)
                for city in city_results:
                    print(f"City: {city['Name']} - District: {city['District']} - Population: {city['Population']}")
        elif choice == 9:
            check = 0
            cities_query = "SELECT Name, Population, CountryCode FROM city ORDER BY Population DESC"
            cities_results = query_iter_many(self.connector, 10, cities_query)
            for cities in cities_results:
                for city in cities:
                    if check >= 5:
                        continue
                    print(f"{city['Name']}  - {city['Population']} {city['CountryCode']}")
                check += 1
                if check < 5:
                    print("="*10 + ". Next? Press Enter...", end="")
                    input()
        elif choice == 10:
            check = 0
            el_choice = 0
            el_choice = input("MIN-1, MAX-2: ") 
            while el_choice.strip().isdigit() == False or int(el_choice) > 2 or int(el_choice) < 1:
                el_choice = input("Pick a number between 1-2: ")
            el_choice = int(el_choice) 
            
            if el_choice == 1:
                query = "SELECT * FROM country WHERE gnp != 0 ORDER BY gnp ASC"
                results = query_iter_many(self.connector,10, query)
                for countries in results:
                    for country in countries:
                        if check >= 5:
                            continue
                        print(f"{country['Name']} ({country['Region']} , {country['Continent']}) - {country['GNP']}")
                    check += 1
                    if check < 5:
                        print("="*10 + ". Next? Press Enter...", end="")
                        input()
            else:
                query = "SELECT * FROM country ORDER BY gnp DESC"
                results = query_iter_many(self.connector,10, query)
                for countries in results:
                    for country in countries:
                        if check >= 5:
                            continue
                        print(f"{country['Name']} ({country['Region']} , {country['Continent']}) - {country['GNP']}")
                    check += 1
                    if check < 5:
                        print("="*10 + ". Next? Press Enter...", end="")
                        input()
        elif choice == 11:
            language = input("Language: ")
            query = "SELECT c.Name, cl.Language, IsOfficial, Percentage FROM country c join countrylanguage cl on c.Code = cl.CountryCode \
                    where cl.Language='" + language + "' ORDER BY Percentage DESC"
            results = query_full_results(self.connector, query)
            if len(results) == 0:
                print("Language not found")
                return
            else:
                print(f"Language: {results[0]['Language']}")
                for result in results:
                    print(f"Country: {result['Name']} - Isofficial: {result['IsOfficial']} - Percentage: {result['Percentage']}")
        else:
            city_name = input("City name: ")
            city_query = "SELECT * FROM city WHERE name ='" + city_name + "'"
            city_results = query_full_results(self.connector, city_query)
            if len(city_results) == 0:
                print("City not found")
                return
            else:
                country_query = "SELECT * FROM country WHERE code='" + city_results[0]['CountryCode'] + "'"
                country_results = query_full_results(self.connector, country_query)
                print(f"City: {city_results[0]['Name']} - District: {city_results[0]['District']} - Country: {country_results[0]['Name']} - Population: {city_results[0]['Population']}")

    #finds a country based on the code
    def find_country(self ,country_code):
        query = "SELECT * FROM country WHERE code='" + country_code + "'"
        results = query_full_results(self.connector, query)
        if len(results) == 0:
            print("Country not found")
            return None
        else:
            return self.print_country(results[0])
        
    #updates a country or a city based on user input
    def update(self):
        print("="*15)
        print("UPDATE SUB-MENU")
        print("="*15)
        print("1. Update a country")
        print("2. Update a city")
        print("="*15)
        choice = input("Pick one: ")
        while choice.strip().isdigit() == False or int(choice) > 2 or int(choice) < 1:
            choice = input("Pick a number between 1-2: ")
        choice = int(choice)

        #update a country
        if choice == 1:
            self.code = input("Give me Country Code: ")
            results = self.find_country(self.code)
            if results == None:
                return

            print("="*15)
            print("UPDATE SUB-MENU")
            print("="*15)
            print("What do you want to update?")
            print("1. Name")
            print("2. Continent")
            print("3. Region")
            print("4. Surface Area")
            print("5. Independence Year")
            print("6. Population")
            print("7. Life Expectancy")
            print("8. GNP")
            print("9. GNP Old")
            print("10. Local Name")
            print("11. Government Form")
            print("12. Head of State")
            print("13. Capital")
            print("14. Code2")
            choice = input("Pick one: ")
            while choice.strip().isdigit() == False or int(choice) > 14 or int(choice) < 1:
                choice = input("Pick a number between 1-14: ")
            choice = int(choice)    

            if choice == 1:
                self.name = input("Country Name: ")
                query = "UPDATE country SET name='" + self.name + "' WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 2:
                self.continent = input("Continent: ")
                query = "UPDATE country SET continent='" + self.continent + "' WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 3:
                self.region = input("Region: ")
                query = "UPDATE country SET region='" + self.region + "' WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 4:
                self.surface_area = float(input("Surface Area: "))
                query = "UPDATE country SET surface_area=" + str(self.surface_area) + " WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 5:
                inp = input("Independence Year (Type None if it is unknown): ")
                if inp == "None":
                    self.indep_year = None
                    query = "UPDATE country SET indepyear= NULL WHERE code='" + self.code + "'"
                else:
                    self.indep_year = int(inp)
                    query = "UPDATE country SET indepyear=" + str(self.indep_year) + " WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 6:
                self.population = int(input("Population: "))
                query = "UPDATE country SET population=" + str(self.population) + " WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 7:
                inp = input("Life Expectancy (Type None if it is unknown): ")
                if inp == "None":
                    self.life_expectancy = None
                    query = "UPDATE country SET life_expectancy= NULL WHERE code='" + self.code + "'"
                else:
                    self.life_expectancy = float(inp)
                    query = "UPDATE country SET life_expectancy=" + str(self.life_expectancy) + " WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 8:
                inp = input("GNP (Type None if it is unknown): ")
                if inp == "None":
                    self.gnp = None
                    query = "UPDATE country SET gnp= NULL WHERE code='" + self.code + "'"
                else:
                    self.gnp = float(inp)
                    query = "UPDATE country SET gnp=" + str(self.gnp) + " WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 9:
                inp = input("GNP Old (Type None if it is unknown): ")
                if inp == "None":
                    self.gnp_old = None
                    query = "UPDATE country SET gnp_old= NULL WHERE code='" + self.code + "'"
                else:
                    self.gnp_old = float(inp)
                    query = "UPDATE country SET gnp_old=" + str(self.gnp_old) + " WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 10:
                self.local_name = input("Local Name: ")
                query = "UPDATE country SET local_name='" + self.local_name + "' WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 11:
                self.government_form = input("Government Form (Type None if it is unknown): ")
                if inp == "None":
                    self.government_form = None
                    query = "UPDATE country SET government_form= NULL WHERE code='" + self.code + "'"
                else:
                    self.government_form = inp
                    query = "UPDATE country SET government_form='" + self.government_form + "' WHERE code='" + self.code + "'"
 
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 12:
                inp = input("Head of State (Type None if it is unknown): ")
                if inp == "None":
                    self.head_of_state = None
                    query = "UPDATE country SET head_of_state= NULL WHERE code='" + self.code + "'"
                else:
                    self.head_of_state = inp
                    query = "UPDATE country SET head_of_state='" + self.head_of_state + "' WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            elif choice == 13:
                inp = input("Capital (Type None if it is unknown): ")
                if inp == "None":
                    self.capital = None
                    query = "UPDATE country SET capital= NULL WHERE code='" + self.code + "'"
                else:
                    self.capital = inp
                    query = "UPDATE country SET capital=" + str(self.capital) + " WHERE code='" + self.code + "'"
                
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")
            else:
                self.code2 = input("Code2: ")
                query = "UPDATE country SET code2='" + self.code2 + "' WHERE code='" + self.code + "'"
                update_query(self.connector, query)
                self.connector.commit()
                self.find_country(self.code)
                print("Country updated successfully")

        #update a city
        elif choice == 2:
            city_name = input("City name: ")
            city_query = "SELECT * FROM city WHERE name ='" + city_name + "'"
            city_results = query_full_results(self.connector, city_query)
            if len(city_results) == 0:
                print("City not found")
                return
            else:
                print(f"City: {city_results[0]['Name']} ({city_results[0]['District']}) - {city_results[0]['Population']}")
                print("="*15)
                print("What do you want to update?")
                print("1. Name")
                print("2. District")
                print("3. Population")
                choice = input("Pick one: ")
                while choice.strip().isdigit() == False or int(choice) > 3 or int(choice) < 1:
                    choice = input("Pick a number between 1-3: ")
                choice = int(choice)    

                if choice == 1:
                    name = input("City Name: ")
                    query = "UPDATE city SET name='" + name + "' WHERE id='" + str(city_results[0]['ID']) + "'"
                    update_query(self.connector, query)
                    self.connector.commit()
                    print("City updated successfully")
                elif choice == 2:
                    district = input("District: ")
                    query = "UPDATE city SET district='" + district + "' WHERE id='" + str(city_results[0]['ID']) + "'"
                    update_query(self.connector, query)
                    self.connector.commit()
                    print("City updated successfully")
                else:
                    population = input("Population: ")
                    query = "UPDATE city SET population=" + population + " WHERE id='" + str(city_results[0]['ID']) + "'"
                    update_query(self.connector, query)
                    self.connector.commit()
                    print("City updated successfully")

    #deletes a country or a city based on user input  
    def delete(self):
        print("="*15)
        print("DELETE SUB-MENU")
        print("="*15)
        print("1. Delete a country")
        print("2. Delete a city")
        print("="*15)
        choice = input("Pick one: ")
        while choice.strip().isdigit() == False or int(choice) > 2 or int(choice) < 1:
            choice = input("Pick a number between 1-2: ")
        choice = int(choice)

        #delete a country
        if choice == 1:
            self.code = input("Give me Country Code: ")
            results = self.find_country(self.code)
            if results == None:
                return
            
            city_delete_query = "DELETE FROM city WHERE countrycode='" + self.code + "'"
            delete_query(self.connector, city_delete_query)
            self.connector.commit()
            query = "DELETE FROM country WHERE code='" + self.code + "'"
            delete_query(self.connector, query)
            self.connector.commit()
            print("Country deleted successfully")
        #delete a city
        else:
            city_name = input("City name: ")
            city_query = "SELECT * FROM city WHERE name ='" + city_name + "'"
            city_results = query_full_results(self.connector, city_query)
            if len(city_results) == 0:
                print("City not found")
                return
            else:
                print(f"City: {city_results[0]['Name']} ({city_results[0]['District']}) - {city_results[0]['Population']}")
                query = "DELETE FROM city WHERE id='" + str(city_results[0]['ID']) + "'"
                delete_query(self.connector, query)
                self.connector.commit()
                print("City deleted successfully")


            
            







        





