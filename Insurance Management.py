import mysql.connector as p
import os
mydb = p.connect(host="localhost", user="admin",
                 passwd="root", database="insurances")
mycursor = mydb.cursor()
print('\n'*3, '\t'*2, "******************************************************************", '\n'*2, '\t'*5,
      "WELCOME TO RELIANCE INSURANCE", '\n'*2, '\t'*2, "******************************************************************")


def insurancemenu():
    print("INSURANCE POLICIES")
    print("1.REGISTERATION")
    print("2.LOGIN ")
    print("3.HELP")
    print("4.CANCEL POLICY")
    print("5.VIEW POLICY")
    print("6.QUIT")
    n = int(input("ENTER YOUR CHOICE:"))
    if n == 1:
      register()
    elif n == 2:
      login()
    elif n == 3:
      enquiry()
    elif n == 4:
      cancel()
    elif n == 5:
      display()
    elif n == 6:
      exit(0)
    else:
     print("WRONG CHOICE, PLEASE TRY AGAIN")

def register():
    print('\n'*3, '\t'*2, "******************************************************************", '\n'*2, '\t'*5,
          "CLIENT DETAILS", '\n'*2, '\t'*2, "******************************************************************")


    global i
    i = []
    name = input("ENTER YOUR NAME:")
    i.append(name)
    ano = int(input("ENTER YOUR ACCOUNT NO:"))
    i.append(ano)
    bank = input("ENTER YOUR BANK:")
    i.append(bank)
    gender = input("ENTER YOUR GENDER:")
    i.append(gender)
    address = input("ENTER YOUR ADDRESS:")
    i.append(address)
    father = input("ENTER FATHER'S NAME:")
    i.append(father)
    contact = int(input("ENTER YOUR CONTACT NO. :"))
    i.append(contact)
    emailid = input("ENTER YOUR EMAIL ID:")
    i.append(emailid)
    password = input("ENTER YOUR PASSWORD:")
    i.append(password)
    amt = int(input("ENTER YOUR PACKAGE AMOUNT:"))
    i.append(amt)
    client = (i)
    sql = "INSERT INTO REGISTER(name,ano,bank,gender,address,father,contact,emailid,password,amt) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, client)
    mydb.commit()
    print("REGISTRATION IS COMPLETED")
    print("==========================================================")


def login():
    print('\n'*3, '\t'*2, "******************************************************************", '\n'*2,
          '\t'*5, "LOGIN", '\n'*2, '\t'*2, "*****************************************************************")


    i = []
    username = input("ENTER ACCOUNT USER NAME")
    i.append(username)
    password = input("ENTER ACCOUNT PASSWORD")
    i.append(password)
    login = (i)
    sql = "INSERT INTO LOGIN(username,password)values(%s,%s)"
    mycursor.execute(sql, login)
    mydb.commit()
    print(i)
    print("YOUR ACCOUNT IS NOW LOGGED IN")
    print("===========================================================")
    insurancemenu()


def enquiry():
    print('\n'*3, '\t'*2, "******************************************************************", '\n'*2, '\t' *
          5, "HELP FORM", '\n'*2, '\t'*2, "******************************************************************")


    i = []
    name = input("ENTER YOUR NAME:")
    i.append(name)
    gender = input("ENTER YOUR GENDER")
    i.append(gender)
    addres = input("ENTER YOUR ADDRESS")
    i.append(addres)
    contact = input("ENTER YOUR CONTACT NO. ")
    i.append(contact)
    helptext = input("ENTER YOUR HELP TEXT")
    i.append(helptext)
    emailid = input("ENTER YOUR EMAIL ID ")
    i.append(emailid)
    text = (i)
    sq = "INSERT INTO ENQUIRY(name,gender,addres,contact,helptext,emailid)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sq, text)
    mydb.commit()
    print("HELP FORM HAS BEEN ISSUED")
    print("==============================================================")
    insurancemenu()


def cancel():
    print('\n'*3, '\t'*2, "******************************************************************", '\n'*2, '\t'*5,
          "POLICY CANCELLATION", '\n'*2, '\t'*2, "******************************************************************")


    passwd = input("ENTER PASSWORD OF YOUR INSURANCE ACCOUNT")
    pn = (passwd,)
    sql = "update register set name ='remove' where password=%s"
    mycursor.execute(sql, pn)
    mydb.commit()
    print("Cancellation completed")
    print("Go back to menu")
    print("===================================================================")
    insurancemenu()


def display():
    print('\n'*3, '\t'*2, "******************************************************************", '\n'*2, '\t'*5,
          "VIEW POLICIES", '\n'*2, '\t'*2, "******************************************************************")


    s = input("ENTER ACCOUNT PASSWORD")
    pn = (s,)
    sql = "select * from REGISTER where PASSWORD=%s"
    mycursor.execute(sql, pn)
    res = mycursor.fetchall()
    # mydb.commit()
    print("INSURANCE STATUS are as follows : ")
    print("(name,ano,bank,gender,address,father,contact,emailid,password,fees,amt)")
    for x in res:
        print(x)
        #print("Cancellation completed")
    print("Go back to menu")
    print("===================================================================")
    insurancemenu()
# __main__
insurancemenu()
exit()
