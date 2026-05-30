def chai_report():
    return 29, 21, 20

# gives error
# sold, remaining = chai_report()

# ok
sold, remaining, _ = chai_report()

print("Chai Sold: ", sold)
print("Chai Remaining: ", remaining)
