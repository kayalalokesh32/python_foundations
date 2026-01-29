password='9696' #existing password.
while (True):
    CheckPassword=input("Enter password :")
    if (password != CheckPassword):#for checking the password.
     print("Wrong password, please try again.")
     continue
    else :
     print("Welcome User.")# welcome user.
     break