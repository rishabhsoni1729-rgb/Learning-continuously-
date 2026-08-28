name = input("Enter the name :")
date = input("Enter the date :")

print(f"Dear {name},\nYou are selected!\n{date}")


#Now simply if i just want to replace ,
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Rishabh Soni").replace("<|Date|>" ,"28 Aug 2026"))