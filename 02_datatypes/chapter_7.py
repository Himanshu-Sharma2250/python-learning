ingredients = ["water", "sugar", "tea leaves"]

print(f"Ingredients: {ingredients}")

ingredients.append("kali mirch")

print(f"Ingredients: {ingredients}")

ingredients.remove("sugar")

print(f"Ingredients: {ingredients}")

spices = ["kali mirch", "lal mirch"]
spices1 = ["lehsun", "jeera"]

# extend one list with another
spices.extend(spices1)

print(f"spice: {spices}")

# insert at any index
spices.insert(3, "haldi")

print(f"spice: {spices}")

# min 
sugar_level = [1,2,3,4,5]
print(f"min sugar level is {min(sugar_level)}")

# max
print(f"max sugar level is {max(sugar_level)}")

# sort the list
spices.sort()

print(f"spice: {spices}")

# operator overloading
num1 = [1,2]
num2 = [3]

total_num = num1 + num2
print(f"total num: {total_num}")

name = ["Himanshu"]
name_3 = name * 3
print(f"name 3 times: {name_3}")

name2 = ["Himanshu", "Ashu"]

name2_3 = name2 * 3
print(f"name 3 times: {name2_3}")

raw_data = bytearray(b"API GATEWAY")
print(f"byte: {raw_data}")
raw_data = raw_data.replace(b"API", b"ROUTE")
print(f"byte: {raw_data}")