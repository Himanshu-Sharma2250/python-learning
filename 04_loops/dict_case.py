users = [
    {"id": 1, "total": 500, "coupon": "P40"},
    {"id": 2, "total": 550, "coupon": "R50"},
    {"id": 3, "total": 200, "coupon": "G20"}
]

discounts = {
    "P40": (0.4, 0),
    "R50": (0.5, 0),
    "G20": (0.2, 10)
}

for user in users:
    percent, flat = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + flat
    print(f"{user["id"]} paid {user["total"]} and get discount {discount}")