class User:
	def __init__(self,name,email,password,):
		self.name=name
		self.email=email
		self.password=password
		self.friend_list=[]
		self.posts=[]

	def add_friend(self,email):
		self.friend_list.append(email)
		print(self.name+" has added "+email+" as a friend")

	def remove_friend(self,email):
		self.friend_list.pop(email)
		print(self.name+" has removed "+email+" from is friend list")

	def post(self,text):
		self.posts.append(text)
		print(self.name+" has posted "+text)

	def get_ui(self):
		print("Name: "+self.name+"\n Email: "+self.email+"\n Password: "+self.password+"\n 	Friends: "+str(self.friend_list)+"\n Posts: "+str(self.posts))

	def msg_user(self,email):
		if email in self.friend_list:
			x=True
			print("type what you want to say to: "+email)
			while x==True:
				msg=input()
				print(self.email+": "+msg)
				if msg=="exit":
					x=False
					print("exiting")
		else:
			print("you dont have a friend with this email address")
	



			




user1=User("Barak","broman@gmail.com","weirdisgood132")
user2=User("Shahar","themememan@tea.com","iliketea5884")

user2.add_friend('broman@gmail.com')
user2.msg_user("broman@gmail.com")
