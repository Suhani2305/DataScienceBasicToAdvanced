# nested loop
colors = ["Red", "Green", "Blue"]
items = ["Shirt", "Pant", "Socks"]
for color in colors:
    for item in items:
        print(f"{color} {item}")  # This will print combinations of colors and items
        
        
# nested while loop
i = 0
while i<3 :
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")  # This will print combinations of i and j
        j += 1  # Incrementing j
    i += 1  # Incrementing i
    
# for loop inside while loop
for i in range(3):
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")  # This will print combinations of i and j
        j += 1  # Incrementing j
        
        
# while loop inside for loop
for i in range(3):
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")  # This will print combinations of i and j
        j += 1  # Incrementing j