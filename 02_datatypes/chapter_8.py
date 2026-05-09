# sets
develop_city = {"faridabad", "gurugram", "noida"}
undevelop_city = {"rewari", "palwal", "faridabad"}

# union
all_city = develop_city | undevelop_city
print(f"all city: {all_city}")

# intersection
common_city = develop_city & undevelop_city
print(f"common city: {common_city}")

develop_city_only = develop_city - undevelop_city
print(f"develop city only: {develop_city_only}")

undevelop_city_only = undevelop_city - develop_city
print(f"undevelop city only: {undevelop_city_only}")

print(f"Is Nuh develop: {"nuh" in develop_city}")

frozen_set = frozenset({4,5,6})
print("frozen set", frozenset)