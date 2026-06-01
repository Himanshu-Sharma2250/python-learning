def infiniteCounting():
    count = 0
    while True:
        yield f"Counting #{count}"
        count += 1

suresh_counting = infiniteCounting()
raj_counting = infiniteCounting()

print("Suresh is Counting")
for _ in range(10):
    print(next(suresh_counting))


print("Raj is Counting")
for _ in range(10):
    print(next(raj_counting))