class Chai:
    temperature = "Hot"
    price = 20

print("Chai price", Chai.price)
print("Chai Temperature", Chai.temperature)

masala_chai = Chai()
print("Masala Chai price", masala_chai.price)
print("Masala Chai temperature", masala_chai.temperature)

masala_chai.price = 30
print("Masala Chai price after change: ", masala_chai.price)

# deleting the attribute 
del masala_chai.price
print("Masala Chai price after deleting: ", masala_chai.price)

# adding new attribute to masala chai
masala_chai.strength = "Strong"
print("Masala Chai strength : ", masala_chai.stength)

# deleting the strength attribute

# del masala_chai.strength
# print("Masala Chai strength after deleting : ", masala_chai.stength) # gives error because Chai has not strength attribute