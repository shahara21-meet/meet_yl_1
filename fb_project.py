emails=["broman@gmail.com","themememan@tea.com"]
class User:
	def __init__(self,name,email,password,):
		self.name=name
		self.email=email
		self.password=password
		self.friend_list=[]
		self.posts=[]
		emails.append(email)

	def add_friend(self,email):
		if email in emails:
			self.friend_list.append(email)
			print(self.name+" has added "+email+" as a friend")
		else:
			print("there is no such user")

	def remove_friend(self,email):
		if email in friend_list:
			self.friend_list.pop(email)
			print(self.name+" has removed "+email+" from is friend list")
		else:
			print("you have no such friend")

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

barak=User("barak","broman@gmail.com","weirdisgood132")
shahar=User("shahar","themememan@tea.com","iliketea5884")

user_dict={"shahar":"iliketea5884","barak":"weirdisgood132"}
users={'iliketea5884':shahar,"weirdisgood132":barak}


def create_user():
	x=input("how do you want to call your user? ")
	y=input("what email do you want to use for your email? ")
	z=input("write your desired password ")
	if z in user_dict:
		z=input("choose another password ")

	user_dict[x]=z
	username=User(x,y,z)
	users[z]=username

def login():
	l_name=input("write username ")
	l_password=input("write password ")
	if user_dict[l_name]==l_password:
		current_user=users[l_password]
		print("you've logged in!!")
		return current_user
	else:
		print("username or password incorrect")




			


print("login/create new user ")




while True:
	check=input()
	if check=="msg "+shahar.name:
		current_user.msg_user(bhahar.email)
	elif check=="msg "+barak.name:
		current_user.msg_user(barak.email)
	elif check=="create new user":
		create_user()
	elif check=="login":
		current_user=login()
	elif check=="add friend":
		n_friend=input("what is his email? ")
		current_user.add_friend(n_friend)
	elif check=="remove friend":
		n_friend=input("what is his email? ")
		current_user.remove_friend(n_friend)




















