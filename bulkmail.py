import pandas as pd

import re

import smtplib

e = pd.read_excel("Emails.xlsx")

emails = e['Emailss'].tolist()

username=input("Enter your email: ")

password= input("Enter your passowrd: ")


domain = re.split("@", username)[1]

#print(domain)

real_domain = domain.split(".")[0]

#print(real_domain)

class WebDomain:
	def __init__(self,server_name):

		self.name = server_name
		

		if self.name=='gmail':
			self.server = smtplib.SMTP("smtp.gmail.com", 587)

		if self.name=='yahoo':
			self.server= smtplib.SMTP("smtp.mail.yahoo.com", 587)
 
	

			

d=WebDomain(real_domain)

d.server.starttls()

d.server.login(username,password)

msg = "Hello this is email."

subject = "Body"

body = "Subject: {}\n \n {}".format(subject,msg)


for email in emails:
	d.server.sendmail(username, email, body)
	d.server.quit()

