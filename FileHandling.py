
def process_lower(text):
    print("I am in process of lower  block")
    lowerCase = text.lower()
    return lowerCase

#Open the file
# C:\Users\sakha\OneDrive\Documents\SepDemo\input.txt
# input.txt
file = open("input.txt","r")


#Read the file
content=file.read()

#print(content)   
results= process_lower(content)
print(results) 