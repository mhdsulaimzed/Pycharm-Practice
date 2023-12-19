import sys
import os

script ,input_file,output_file =sys.argv

in_file=open(input_file)
data = in_file.read()

print(f"teh file is {len(data)} bytes")
print("do you want to continue press return")
input()
to_file=open(output_file,'w')
to_file.write(data)
in_file.close()
to_file.close()
