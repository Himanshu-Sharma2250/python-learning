daily_sales = [3,5,2,6,7,7]

sales = sum(sale for sale in daily_sales if sale < 4)

print(sales)