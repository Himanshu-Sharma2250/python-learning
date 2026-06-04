def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError(f"We don't know {flavor} flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")
    
serve_chai("Masala Chai")
serve_chai("unknown")
