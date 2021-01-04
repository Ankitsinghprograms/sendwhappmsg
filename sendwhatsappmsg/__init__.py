
"""

===========================
sendwhatsappmsg- Send any message to whatsapp
==========================

===============================
----------------------------------------
----sendwhatsappmsg module------------
----Version-(0.0.1) {First Release}---
---------------------------------------
===============================


========Third Party Modules========

webbrowser
	Install via pip install webbrowser or pip3 install webbrowser
	
time
	builtin module No need to install

===============================


======== Getting Errors??========

If You get error then contact me at ankitsingh300307@gmail.com

=============================


=========== Author ==========

Name-Ankit Singh 
Email-ankitsingh300307@gmail.com
Github-https://github.com/Ankitsinghprograms
Country-India

===========================

"""



#Importing modules

import webbrowser

import time



#Code starts 


#sendmsg Function

def sendmsg(message_text):
	
	
	"""
	Open whatsapp share page to send any given message to any contact
	
	
	Parameters
	-----------
	
	message_text:- String,For new line character Use '%0a' instead of '\n'
	
	
	"""
	
	
	print("SENDING MESSAGE\n")
	
	
	link=f"https://wa.me/?text={message_text}"
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	
	

#sendmsgafter Function

def sendmsgafter(message_text,seconds):
	
	"""
	
	Open whatsapp share page after the seconds given to send given message to any contact
	
	
	Parameters
	----------
	
	message_text:- String,For new line character Use '%0a' instead of '\n'
	
	seconds-int
	

	"""

	
	message_text=str(message_text)
	
	try:
		
		seconds=int(seconds)
		
	except:
		
		print("ERROR: SECOND ARGUMENT (SECONDS) SHOULD BE IN INT FORM!!\n")
		
		return None
		
	print(f"SENDING MSG AFTER {seconds}secs\n")
	
		
	time.sleep(seconds)
	
	print("SENDING MESSAGE\n")
	
	link=f"https://wa.me/?text={message_text}"
	
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	


#sendmsgat Function

def sendmsgat(message_text,hour,minutes,seconds="00"):
	
	
	"""
	Open whatsapp share page at a given time to send given message to any contact
	
	Important-Time should be 24hr format 
	
	
	Parameters
	----------
	
	message_text:- String,For new line character Use '%0a' instead of '\n'
	
	hour-string, Should be between 00 to 24 
	
	minutes-string, should be between 00 to 60
	
	seconds-optional,Default-00, string,Should be between 00 to 60
	
	
	"""
	
	
	#Changing parameters to string form
	
	
	message_text=str(message_text)
	
	hour=str(hour)
	
	minutes=str(minutes)
	
	seconds=str(seconds)
	
	
	if len(hour)==1:
		
		hour="0"+hour
		
	if len(minutes)==1:
		
		minutes="0"+minutes
		
	if len(seconds)==1:
		
		seconds="0"+seconds
		
	
	print(f"MESSAGE WIILL BE SENT AT {hour}:{minutes}:{seconds}\n")
	
	print("DON'T CLOSE THIS PROGRAM ELSE MESSAGE WILL NOT BE SENT!!\n")
	
	while True:
		
		now_hour=time.strftime("%H")
		
		now_minute=time.strftime("%M")
		
		now_second=time.strftime("%S")
	
	
		if now_hour==hour and now_minute==minutes and now_second==seconds:
			
			break
			
	
	print("SENDING MSG\n")
		
		
	link=f"https://wa.me/?text={message_text}"
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	
	


#Send message to any particular mobile no. Functions



#sendmsgto Function

def sendmsgto(send_msg_to_mobile_no,message_text):
	
	"""
	
	Open whatsapp share page to send any given message to any contact
	
	
	Parameters
	-----------
	
	send_msg_to_mobile_no:- String,With country code. Without spaces
	
	Mobile no Format
	
	countrycodemobileno
	
	Example:-+91933XXXXXXX
	
	Note:-No spaces
	
	message_text:- String,For new line character Use '%0a' instead of '\n'
	

	"""
	
	print("SENDING MESSAGE\n")
	
	
	link=f"https://wa.me/{send_msg_to_mobile_no}/?text={message_text}"
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	
	

#sendmsgtoafter Function
def sendmsgtoafter(send_msg_to_mobile_no,message_text,seconds):
	
	"""
	Open whatsapp share page after the seconds given to send given message to any contact
	
	
	Parameters
	----------
	
	send_msg_to_mobile_no:- String,With country code. Without spaces
	
	Mobile no Format
	
	countrycodemobileno
	
	Example:-+91933XXXXXXX
	
	Note:-No spaces
	

	message_text:- String,For new line character Use '%0a' instead of '\n'
	
	
	seconds-int
	
	
	"""
	
	send_msg_to_mobile_no= str(send_msg_to_mobile_no)
	
	message_text=str(message_text)
	
	try:
		
		seconds=int(seconds)
		
	except:
		
		print("ERROR: THIRD ARGUMENT (SECONDS) SHOULD BE IN INT FORM!!\n")
		
		return None
		
	print(f"SENDING MSG AFTER {seconds}secs\n")
	
		
	time.sleep(seconds)
	
	print("SENDING MESSAGE\n")
	
	link=f"https://wa.me/{send_msg_to_mobile_no}/?text={message_text}"
	
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	
	
	
		
#sendmsgtoat Function
def sendmsgtoat(send_msg_to_mobile_no,message_text,hour,minutes,seconds="00"):
	
	
	"""
	
	Open whatsapp share page at a given time to send given message to any contact
	
	Important-Time should be 24hr format 
	
	Parameters
	----------
	
	send_msg_to_mobile_no:- String,With country code. Without spaces
	
	Mobile no Format
	
	countrycodemobileno
	
	Example:-+91933XXXXXXX
	
	Note:-No spaces
	
	
	message_text:- String,For new line character Use '%0a' instead of '\n'
	
	hour-string, Should be between 00 to 24 
	
	minutes-string, should be between 00 to 60
	
	seconds-optional,Default-00, string,Should be between 00 to 60
	
	"""
	
	
	#Changing parameters to string form
	
	
	send_msg_to_mobile_no= str(send_msg_to_mobile_no)
	
	message_text=str(message_text)
	
	hour=str(hour)
	
	minutes=str(minutes)
	
	seconds=str(seconds)
	
	
	if len(hour)==1:
		
		hour="0"+hour
		
	if len(minutes)==1:
		
		minutes="0"+minutes
		
	if len(seconds)==1:
		
		seconds="0"+seconds
		

	
	print(f"MESSAGE WIILL BE SENT AT {hour}:{minutes}:{seconds}\n")
	
	print("DON'T CLOSE THIS PROGRAM ELSE MESSAGE WILL NOT BE SENT!!\n")
	
	while True:
		
		now_hour=time.strftime("%H")
		
		now_minute=time.strftime("%M")
		
		now_second=time.strftime("%S")
		
		
		if now_hour==hour and now_minute==minutes and now_second==seconds:
			
			break
			
	
	print("SENDING MSG\n")
		
		
	link=f"https://wa.me/{send_msg_to_mobile_no}/?text={message_text}"
	
	webbrowser.open(link)
	
	print("MESSAGE SENT\n")
	
