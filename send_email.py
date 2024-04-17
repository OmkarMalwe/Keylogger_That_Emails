import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = "dummy_sender@gmail.com"
	# do not use regular password as it will give an error..
    # instead use an **app password**
	# refer the following link for the same
    # https://www.youtube.com/watch?v=vswB4BMqqI8
	password = "xxxx xxxx xxxx xxxx" ## password of dummy_sender.gmail.com
	# do not forget to include the spaces in the password
	receiver_email = "dummy_reciever@gmail.com"

	context = ssl.create_default_context()

	try:
		server = smtplib.SMTP(smtp_server,port)#initialise the server
		server.ehlo()
		server.starttls(context=context)
		server.ehlo()
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
	except Exception as e:
		print(e)
	finally:
		server.quit()
