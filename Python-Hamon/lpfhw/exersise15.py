from sys import argv
script,filename=argv
text=open(filename)
print(f"here os your file{filename}")
print(text.read())
