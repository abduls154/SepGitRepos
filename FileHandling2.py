def process_lower(text):
    print("I am in process of lower  block")
    lowerCase = text.lower()
    return lowerCase

file_name = input("Enter the file name you want to process")
with open(file_name,"r") as file:
    print("I am reading the file called ", {file_name})
    content = file.read() 
       
results= process_lower(content)
print(results) 