names = [
    "Himanshu Sharma", "Ashu Sharma", "Himanshu Sharma"
]

unique_name = {name for name in names if len(name) > 8}

# print(unique_name)

# sets = set() # set() 
# print(sets)

courses = {
    "BTech": ["CSE", "ECE", "EE", "ME"],
    "BCOM": ["Commerce", "Accounts"],
    "BA": ["Politics", "Social"]
}

branches = {branch for course in courses.values() for branch in course}

print(branches)