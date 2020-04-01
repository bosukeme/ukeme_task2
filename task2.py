def create_password():
    import random
    import string
    import pprint
    users=[]
    
    first_name=input('What is your first name? :')
    last_name=input('What is your last name? :')
    email_address=input('What is your email address? :')
    
    random_string=''.join(random.choice(string.ascii_letters) for i in range(5))
    password= first_name[:2] + last_name[-2:] +random_string
    print("Your password is: ", password)
    print()
    print('Are you okay with your password? yes/no')
    user_input=input()
    if user_input == "yes":
       # print("Your details are:", [first_name ,last_name, email_address])
        print()
        ##################
        print("Do you want to add another user: yes/no")
        user_input2=input()
        if user_input2== 'no':
            print('Exiting program')
        elif user_input2=='yes':
            first_name2=input('What is your first name? :')
            last_name2=input('What is your last name? :')
            email_address2=input('What is your email address? :')

            random_string2=''.join(random.choice(string.ascii_letters) for i in range(5))
            password2= first_name2[:2] + last_name2[-2:] +random_string2
            print("Your password is: ", password2)
            print()
            print('Are you okay with your password? yes/no')
            user_input3=input()
            if user_input3 == "yes":
                #print("Your details are:", [first_name2 ,last_name2, email_address2])
                print("###")
            else: 
                print('Then Choose a new Password: ')
                new_password=input()

                while len(new_password)<7: 
                    print("Password length is below 7. Try again")
                    new_password=input()

                if len(new_password)>=7:
                    print("Your password is: ", new_password)
                    #print("Your details are:", [first_name2 ,last_name2, email_address2])

        
#####################################################
        
    else: 
        print('Then Choose a new Password: ')
        new_password=input()
        
        while len(new_password)<7: 
            print("Password length is below 7. Try again")
            new_password=input()
        
        if len(new_password)>=7:
            print("Your password is: ", new_password)
           # print("Your details are:", [first_name ,last_name, email_address])
                
                #################
            print("Do you want to add another user: yes/no")
            user_input2=input()
            if user_input2== 'no':
                print('Exiting program')
            elif user_input2=='yes':
                
                first_name2=input('What is your first name? :')
                last_name2=input('What is your last name? :')
                email_address2=input('What is your email address? :')

                random_string2=''.join(random.choice(string.ascii_letters) for i in range(5))
                password2= first_name2[:2] + last_name2[-2:] +random_string2
                print("Your password is: ", password2)
                print()
                print('Are you okay with your password? yes/no')
                user_input=input()
                if user_input == "yes":
                   # print("Your details are:", [first_name2 ,last_name2, email_address2])
                    print('###')
                else: 
                    print('Then Choose a new Password: ')
                    new_password=input()

                    while len(new_password)<7: 
                        print("Password length is below 7. Try again")
                        new_password=input()

                    if len(new_password)>=7:
                        print("Your password is: ", new_password)
                        #print("Your details are:", [first_name2 ,last_name2, email_address2])



    users_details_full={
        "First_name": first_name,
        "last_name": last_name,
        "email_address": email_address
    }
    
    users_details_full2={
        "First_name": first_name2,
        "last_name": last_name2,
        "email_address": email_address2
    }
    users.append(users_details_full)
    users.append(users_details_full2)
    pprint.pprint(users)
	
create_password()