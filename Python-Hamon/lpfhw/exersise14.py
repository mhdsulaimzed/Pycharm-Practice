from sys import argv
scripts,user_name=argv
prompt = '>'

print(f"Hi {user_name} i am {scripts}")
print("i would like to ask  few questions ")
print(f"do you like me{user_name}")
likes=input(prompt)
print(f"where do you live {user_name}")
lives=input(prompt)

print(f"""alright you said{likes} and you live in {lives} """)
