first_name=(input("Entre your name"))
last_name=(input("entre your last name"))
name=first_name+" "+last_name
print(name)
first_name_length=len(first_name)
print(first_name_length)
extracted_last_name=name[first_name_len+1:]
print(extracted_last_name)