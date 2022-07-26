#Various import Statements can go here
from  social_network_classes import SocialNetwork, Person
import social_network_ui






#Create instance of main social network object
ai_social_network = SocialNetwork()


#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == 1:
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == 2:
            inner_menu_choice = social_network_ui.manageAccountMenu()
            while True:
                current_user = None
                current_user_name = input("please give current account")
                for people in ai_social_network.list_of_people:
                    if people.id == current_user_name:
                        current_user = people
                if inner_menu_choice == 1:
                    print("you can now edit your profile")
                    current_user.edit_profile()

                elif inner_menu_choice == 2:
                    friend_choice = input("these are your options to do with friends\n 1. add friend\n 2. remove friend\n :")
                    if friend_choice == "1":
                        print("add friends here now")
                        current_user.add_friend()
                    elif friend_choice == "2":
                        print("remove friend of your choice")
                        current_user.block_friends()

                elif inner_menu_choice == 3:
                    print("view friends here")
                    current_user.view_friends()

                elif inner_menu_choice == 4:
                    message_choice = input("these are your options to do with friends\n 1. send message \n 2. view my messages ")
                    if message_choice == "1":
                        print("send a message here")
                        current_user.send_message()
                    elif message_choice == "2":
                        print("view message here")
                        current_user.view_message()
        

                
                if inner_menu_choice == 5:
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == 3:
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
