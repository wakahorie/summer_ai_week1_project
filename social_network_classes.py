# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        #implement function that creates account here
        username = input("please type in your username: ")
        age = input("please type in age")

        user = Person(username , age)
        self.list_of_people.append(user)


        #for loop to check name in list_of_people
        #if username != self.list_of_people:
            #self.list_of_people.append(username)
        #     age = input("please type in age")
        #     #do not know if this is correct #
            
        #     self.list_of_age.append(age)
        #     print("Creating ...")
        #     print("account created")
            
        # else:
        #     print("username already used")
        #     print("please try again")
        
        #how to ask for the username again
        
        #implement function that creates account here
        # pass


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        #implement sending message to friend here
        pass
