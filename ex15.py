#Import the argv ("feature") from sys
from sys import argv

#script, filename = argv
#
##CReates a file object in the variable txt
#txt = open(filename)
#
#print(f"Here's your file {filename}")
##prints the content of the txt file without any parameter.
#print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()