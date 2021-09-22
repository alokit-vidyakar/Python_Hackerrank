print ("some basic learning going on!")


#defining variable 
message = "this is varibale definition"
print(message)

#combine two variales and print in a line 
number =9
print(message, ":", number)

#changing value of variable 
message = "changed value of definition"
number=10
print(message,":",number)

message = 'Single quote string with "double" quote string inside'
print(message)
message = "Double quote string with 'single' quote string inside"
print(message)

#multiple variable, one value
message = message1= message2 = "1 value for 3 varibale"
print(message, message1, message2)

#multiple variable, multiple value 
message, message1, message2 = "message-value", "message1-value", 'message2-value with single quote'
print(message, message1, message)

#unpacking a group 
messages = ("message-unpacked-value", "message1-unpacked-value", 'message2-unpacked-value with "single" quote')
message,message1,message2= messages
print("this in '\\n' print:","\n",message, "\n", message1,"\n", message)

#function definition
message = "this is value OUTSIDE the fucntion"
def changeOfValue():
	message = "this is value INSIDE the fucntion"
	print(message)
changeOfValue()
print(message, ": Global value didn't change outside fucntion")

def changeOfValueGlobally():
	global message 
	message = "this value is changing gloablly now."
	print(message)
changeOfValueGlobally()
print(message, ":it's changed outside function as well")

#f-string 
full_message = f"{message1} and {message2}"
print(full_message)
print("this is: ", full_message.title())
