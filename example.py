import ankaramesi

encrypt,keys = ankaramesi.encrypt_text_with_keys("Messi is the Goat")
print("______________________________Encrypted data___________________________________________")
for encripted_data in encrypt:
    print(encripted_data)

print("______________________________Keys_______________________________________________________")

for allkeys in keys:
    print(allkeys)
