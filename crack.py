import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")
word_list = input("File name: ")

try:
   pass_file = open(word_list, "r")
except:
   print("No file found")
   quit() # Quit program if file was not found

for word in pass_file:
   encoded_word = word.encode('utf-8')
   digest = hashlib.md5(encoded_word.strip()).hexdigest()
   
   if digest == pass_hash:
     print("Password has been found")
     print("Password is " + word)
     flag = 1
     break 
   
if flag == 0:
   print("Password is not in the list")
