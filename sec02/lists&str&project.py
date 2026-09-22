



#str 
#property: iterable -> قابلیت پیمایش با حلقه for 
# seq -> name=mft 
# dup 
# immutable


# list 
#property
#iter 
#seq

#list_1=[1,2,"fariborz"]

#print(len(list_1))

#for index in range(len(list_1)):
#
# 
# 
#     print(list_1[index])


#print(list_1[1::])

#num_1 = 12.5
#num_1 =15.6
#num_2 = 12.5
#
#print('num1:',num_1,"num2:",num_2)
#print(id(num_1))
#print(id(num_2))



#name1 = "fariborz"
#name2= "fariborz"

#print(id(name1))
#print(id(name2))



#num1=12
#num2=12
#num1=15

#print(num1,num2)


#list_1 = [1,2,3]
#list_2 = [1,2,3]
#list_2 = list_1


#list_1[1]=22
#print(id(list_1))
#print(id(list_2))
#print(list_1)
#print(list_2)

#from math import pi
#
# 
# 
# print(pi)

#from sys import getrefcount
#
#
#data= 512
#
#del(data)
#print(getrefcount(512))





#list_1 = [1,2,3]
#list_2 = [1,2,3]
#list_2 = list_1
#list_1[1]=22
#
#print(list_1)
#print(list_2)


#num=list(range(1,1001))
#print(num)

#list_1=[i for i in range(1,10)]
#
# 
# 
# 
# print(list_1)



#list_1 = [i for i in range(1,11)]
#print(list_1)
#

#wallros op 
#print(num:=int(input("num:")))





#l:1: لیستی از دانش آموزان 
#l2:نمره بگیره 
#l2-1:نمرات درس پایتون - درس جاوا 
#l-3 : نمره جاوا و نمره پایتون توی یک لیست 








students=[]
ljava=[]
lpython=[]
while True:
    menu=input("1.python 2,java 3.exit--->")
    match menu:
        case "1":
            while True:
                name_student=input("esm bede =")
                lpython.append(name_student)
                nomre=float(input("nomre bede ="))
                lpython.append(nomre)
                print(lpython)
                break
        case "2":
             while True:
                name_student=input("esm bede =")
                ljava.append(name_student)
                nomre=float(input("nomre bede ="))
                ljava.append(nomre)
                print(ljava)
                break
        case "3":
            students=["python:",lpython,"java:",ljava]
            print(students)
            break
            
            
        