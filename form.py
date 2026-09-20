





#= name.find("a")
#rint(x)




"""i=0
for i in "fariborz":
    i=i+1
    print(i)
print(i)"""




#x=name.isnumeric()
#e=name.isdigit()
#q=name.isdecimal()
##if x==True:
##    print("ok")
#
#
#print(x,e,q)


#name= "fariborz"
#full_name= "saheb ekhtiari"
#print(f"welcome \n {name}".format(full_name))
#

#
#full_name= "saheb ekhtiari"


#print(name[-1::-1])

#container data 
#list
#tuple
#dict
#set
#str

#n="    ali"
#print(n.strip())
#str -> seq ,dup ,iter 

#name= "ali"
#
#
#print(f"i am{name:+<6}ai dev.")

#print("\U0001f600")







while True:

    menu_login_sabtenam= input("1.sabtenam  2.voorood  3.exit:")

    data =["parsa","fallah","09121111111","teh","fallah123","1234"]
    while True:
        match menu_login_sabtenam:
            case"1":
                name = input("nameto bezan:").strip()
                famili = input("famili:").strip()
                phone = input("phone:").strip()
                address= input("address:").strip()
                name_new = name.capitalize()
                famili_new= famili.capitalize()
                user = input("user:").strip()
                password= input("password:").strip()
                
                if user.isalnum()==True:
                    print("user ok ")
                    
                else:
                    print("user ghabol nashod .")
                    break
                
                
                if password.isalnum()==True:
                    print("password ok. ")
                                    
                else:
                    print("password  ghabol nashod .")
                    break
                
                if phone.isdigit()==True:
                    print("mobile ok")
                    
                    
                else:
                    print("mobile ro eshteb zadi yo ","\U0001f410")
                    break
                
                    
                if address.isalnum()==True:
                    print("adress vared shod.")
                else:
                    print("address eshtebah")
                    break
                
                
                
                data.append(name_new)
                data.append(famili_new)
                data.append(phone)
                data.append(address)
                
                print(data)
                data.append(user)
                data.append(password)
                
                break
            
            case "2":
                user_vorodi= input("user bezan:")
                password_voroodi = input("password bezan:")
                if user_vorodi in data:
                    print("ok user dorost.")
                if user_vorodi not in data:
                    print("lotfan sabtenam konid .")
                i=0
                while True:
                    if password_voroodi in data:
                        print("login")
                        break
                    else:
                        i=i+1
                        if i== 3:
                            print("masdood shodid.")
                            break
                break
            
            case "3":
                print("sepas as shoma .")
                break
    break        
                
            
