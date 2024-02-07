


weight = 7000
print(f"Today's weight is {weight} g")

output1 = "Today's weight is " + str(weight / 1000) +" kg"
output2 = f"Today's weight is {weight / 1000} kg"
print(output1)
print(output2)

def calculation():
    return weight / 1000

print(f"Today's weight is {calculation()} kg")