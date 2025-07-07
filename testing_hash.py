import hashlib

hasher = hashlib.sha256()


string_test = "testingtesitng"

string_test_bytes = string_test.encode("utf-8")
# print(string_bytes

hasher.update(string_test_bytes)

hashed_string_hex = hasher.hexdigest()
hashed_string_dec = int.from_bytes(hasher.digest(), "big")
print(hashed_string_dec)


# string_test_hashed_bytes = string_test_hashed_bits.digest()
# print(string_test_hashed_bytes)
