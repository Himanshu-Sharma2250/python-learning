# Strings

chai_type = "Black tea"
customer = "Himanshu"

print(f"Customer {customer} ordered : {chai_type}")

chai_characterstics = "Aromatic and Bold"

# Indexing
print(f"First word: {chai_characterstics[0:8]}")
print(f"First word: {chai_characterstics[0:8:2]}")
print(f"Second word: {chai_characterstics[13:]}")

# reverse
print(f"Reverse : {chai_characterstics[::-1]}")

label_word = "Bláck Tea"
encoded_label = label_word.encode("utf-8")

print(f"Label word: {label_word}")
print(f"Encoded Label word: {encoded_label}")

decode_label = encoded_label.decode("utf-8")
print(f"Decoded Label word: {decode_label}")