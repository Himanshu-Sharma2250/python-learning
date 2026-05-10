# Dictionary

info = dict(name="Himanshu Sharma", age=22, course="BTech CSE")
print(f"Info: {info}")

course = {}
course["name"] = "BTech"
course["duration"] = "4 year"
print(f"Course Info: {course}")

# del course["duration"]
# print(f"Course Info after del: {course}")

# print(f"Is name in course: {"name" in course}")
# print(f"Is duraion in course: {"duration" in course}")

# print(f"Order of course (keys): {course.keys()}")
# print(f"Order of course (values): {course.values()}")

# last_item = course.popitem()
# print(f"Last Item: {last_item}")

new_course_info = {"annual_fee": "40k"}
course.update(new_course_info)
print(f"Updated course: {course}")

location = course.get("location", "No location given")
print(f"Location: {location}")

# all operations of set exist in dictionary also like union and intersection