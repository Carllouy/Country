# Carl Louy, CIS261, Country

def display_menu():
    print("\n==============================")
    print("      Country Dictionary")
    print("==============================")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")
    print("==============================")

def initialize_country_dict():
    return {
        "US": "United States",
        "RU": "Russia",
        "CN": "China"
    }

def view_country(countries):
    print("\nAvailable country codes:")
    for code in countries:
        print(f" - {code}")
    
    code = input("Enter the country code to view: ").strip().upper()
    if code in countries:
        print(f"{code} => {countries[code]}")
    else:
        print("Invalid country code. Please try again.")

def add_country(countries):
    code = input("Enter the new country code: ").strip().upper()
    if code in countries:
        print("This country code already exists. Cannot add duplicate.")
        return
    name = input("Enter the country name: ").strip()
    if name:
        countries[code] = name
        print(f"{code} => {name} added successfully.")
    else:
        print("Country name cannot be empty.")

def delete_country(countries):
    code = input("Enter the country code to delete: ").strip().upper()
    if code in countries:
        deleted = countries.pop(code)
        print(f"{code} => {deleted} has been deleted.")
    else:
        print("Invalid country code. Nothing was deleted.")

def main():
    countries = initialize_country_dict()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_country(countries)
        elif choice == '2':
            add_country(countries)
        elif choice == '3':
            delete_country(countries)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please choose a valid option.")

if __name__ == "__main__":
    main()