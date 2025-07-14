food = ["Dahi Bhalley", "Chole Bhature", "Paneer Tikka", "Aloo Tikki", "Samosa"]
print(food)
print(food[0])  # Accessing the first element
print(food[1])  # Accessing the second element
print(food[2])  # Accessing the third element   

food[2] = "Paneer Pakora"  # Modifying the third element
print(food[2])  # Accessing the modified third element


# set
food_set = {"Dahi Bhalley", "Chole Bhature", "Paneer Tikka", "Aloo Tikki", "Samosa"}
print(food_set) 
print("Dahi Bhalley" in food_set)  # Checking if an item is in the set
print("Pizza" in food_set)  # Checking if an item is not in the set
# food_set[2] = "Paneer Pakora"  # This will raise an error because sets are unordered and do not support indexing
# Adding an item to the set
food_set.add("Paneer Pakora")

# dictionary
food_dict = {
    "Dahi Bhalley": 50,
    "Chole Bhature": 80,
    "Paneer Tikka": 100,
    "Aloo Tikki": 30,
    "Samosa": 20
}
print(food_dict)  # Printing the entire dictionary
print(food_dict["Dahi Bhalley"])  # Accessing the price of Dahi Bhalley
print(food_dict["Chole Bhature"])  # Accessing the price of Chole Bhature
food_dict["Paneer Tikka"] = 120  # Modifying the price of Paneer Tikka
print(food_dict["Paneer Tikka"])  # Accessing the modified price of Paneer Tikkant