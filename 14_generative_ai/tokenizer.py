import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

text = "Hello World!"

token = encoder.encode(text)
print("Token:", token)

decoded = encoder.decode(token)
print("Decoded:", decoded)