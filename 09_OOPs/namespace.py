class Chai:
    origin = "India"

Chai.is_hot = True

print(f"Chai: {Chai.origin}")
print(f"Chai: {Chai.is_hot}") # this is correct but it shows red swigly lines

masala_chai = Chai()
print(f"Masala Chai: {masala_chai.origin}")
print(f"Masala Chai: {masala_chai.is_hot}")

masala_chai.origin = "China"
print(f"Chai: {Chai.origin}")
print(f"Masala Chai: {masala_chai.origin}")

masala_chai.flavor = 'Spice'

print(f"Masala Chai Flavor: {masala_chai.flavor}")