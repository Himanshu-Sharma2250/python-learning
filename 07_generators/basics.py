def shop():
    yield "Mango: 50"
    yield "Orange: 30"
    yield "Banana: 40"

fruit_price = shop()

# for fruit in fruit_price:
#     print(fruit)

# normal function
def student_names():
    return ["Ashish", "Rahul", "Piyush"]

# generator function
def student_names_gen():
    yield "Ashish"
    yield "Rahul"
    yield "Piyush"

students = student_names_gen()
print(students) # output : <generator object student_names_gen at 0x000001F5C7064BF0>
print(next(students)) # output : Ashish
print(next(students)) # output : Rahul