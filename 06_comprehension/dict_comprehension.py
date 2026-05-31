prices = {
    "Green Tea": 80,
    "Kali Chai": 20,
    "Macha Tea": 100
}

pricesInUSD = {tea:price/90 for tea, price in prices.items()}

print(pricesInUSD)