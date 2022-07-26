# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    #def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        

    def create_account(self):
        #implement function that creates account here
        name = input("please type in your username")
        while name in self.list_of_people:
          name = input("please type in another username: ")
          if name not in self.list_of_people:
            break
        age = input("please type in age")
        user = Person(name , age)
        self.list_of_people.append(user)
        print("now our username is set to" , name , "and your age is set to " , age)


        
       

class Person:
    def __init__(self , name , age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messagelist = []

    def edit_profile(self):
        newname = input("please type in your new name")
        self.id = newname
        newage = input("please type in your new age")
        self.age = newage
        print("this is your new name", newname, " and this is your new age" , newage)


     

    def add_friend(self):
         name = input("please type in the username: ")
         for i in range(0,len(self.friendlist)):
            if name != self.friendlist[i]:
             self.friendlist.append(name)
             print(name , "added to the friendlist")
            else:
             print("username already added to friendlist")


    def view_friends(self):
        print("your current friend list" , self.friendlist)

       
    

    def send_message(self):
         message = input("type in you message")
         receiver = input("message receiver username: ")
         for i in range(0,SocialNetwork.list_of_people):
            if receiver == SocialNetwork.list_of_people[i]:
                receiver.self.messagelist.append(message)
                print("the message: ", message , "   has been sent to:  " , receiver)

    def view_message(self):
        print("current message list" , self.messagelist)

        #implement sending message to friend here
    

    def block_friends(self):
        notfriend = input("who do you want to block: ")
        for i in range(0,len(self.freindlist)):
            if notfriend == self.friendlist[i]:
                self.friendlist.pop(notfriend)
                print(notfriend , "has been removed from your friend list")
            else:
                print("already not your friend")

   
