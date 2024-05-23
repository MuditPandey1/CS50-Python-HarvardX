from validator_collection import validators

value=input("Email address: ")
try:
    email_address = validators.email(value, allow_empty = True)
    print("Valid")
except:
    print("Invalid")