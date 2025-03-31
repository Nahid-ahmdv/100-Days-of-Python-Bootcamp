from gavel_art import logo
import os 
def winner_bidder_calculator(mydic):
    sorted_bids = list(mydic.values())
    sorted_bids.sort()
    highest_bid = sorted_bids[-1]
    for key in mydic:
        if mydic[key] == highest_bid:
            winner_bidder = key
    return highest_bid, winner_bidder

print(logo, "\n", "welcome to the secret auction program.")

bidders_dic = {}
while True:
    bidder_name = input("what is your name? ")
    bidder_bid = int(input("what is your bid? $"))
    bidders_dic[bidder_name] = bidder_bid
    any_other = input("Are there any other bidders? ").lower()
    os.system('cls')
    if any_other == "no":
        break
    #at this point i want clear the terminal except the logo and "welcome to the secret auction program."
   
print(bidders_dic)

price, person = winner_bidder_calculator(bidders_dic)
print(f"The winner is {person} with a bid of ${price}!")

#better function:
def winner_bidder_calculator(mydic):
    highest_bid = max(mydic.values())  # Get the highest bid directly
    winner_bidder = max(mydic, key=mydic.get)  # Find the corresponding bidder
    return highest_bid, winner_bidder
'''
Example 1: Using max() on a Dictionary (Default Behavior)
mydict = {3: "apple", 1: "banana", 5: "cherry"}

print(max(mydict))  # Output: 5 (since 5 is the largest key)
🔹 By default, max() considers only the dictionary keys, not the values.



Example 2: Finding the Key with the Maximum Value
To find the key corresponding to the maximum value, use the key argument with .get:
mydict = {"Alice": 90, "Bob": 85, "Charlie": 95}

max_key = max(mydict, key=mydict.get)  # Finds key with highest value
print(max_key)  # Output: "Charlie" (since 95 is the highest value)
🔹 Here, mydict.get retrieves the values, and max() finds the key with the largest value.


"when max() is used on a dictionary, it always returns the key, not the value."
'''