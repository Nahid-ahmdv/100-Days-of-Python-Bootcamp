#the final project of Day 01: Band Name Generator
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n").capitalize() #After the user inputs their response, the .capitalize() method is called on that string. This method converts the first character of the string to uppercase and all other characters to lowercase.
pet_name = input("What's your pet's name?\n").capitalize()
print("Your band name could be " + city_name + " " + pet_name)
print(f"Your band name could be {city_name} {pet_name}")