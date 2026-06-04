def brew_chai(flavor):
    if flavor not in ["Masala", "Ginger", "Macha"]:
        raise ValueError("Unsupported flavor")
    print(f"Brewing {flavor} chai")

brew_chai("Masala")
brew_chai("Oolong")