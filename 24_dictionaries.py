customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
print(customer.get("name", "Hey"))
print(customer.get("birthdate"))

# Jack Smith
# Jan 1 1980


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
