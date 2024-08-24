import mysql.connector as mc
from time import sleep 
dbc = mc.connect(host = 'localhost',user = 'root',password = '',db = 'miniproject')
mycursor = dbc.cursor()
print('Welcome !')

def atm():
    
    card = input('insert your card : ')
    if card == "Card":
        sleep(2)
        print("Hi,Please do not Remove your Chip Card\nLeave your Card inserted during the Entire Transaction.")
        sleep(4)
        choice = int(input("Dear Customer,Please Select Transaction :\n"+"1.CREATE ACCOUNT\n2.DEPOSIT\n3.WITHDRAWAL\n4.BALANCE INQUIRY : "))
        if choice == 1:
                
                name1 = input('Enter Your name : ')
                sleep(1)
                passwo = int(input("Create Your PIN NO : "))
                sleep(1)
                account = int(input("Enter the Account Number : "))
                sleep(1)
                deposit = int(input("Enter Your Starting Amount 500 : "))
                mycursor.execute("insert into bank(name,password,depo,acc_no) values('{}',{},{},{})".format(name1,passwo,deposit,account))
                mycursor.execute("update bank set balance = depo ".format(deposit))
                dbc.commit()
                print("Please Wait Your Transaction is Processing...") 
                sleep(3)
                print("Account Successfully Created...")
                        
        elif choice == 2:
                passwo = int(input("Please Enter Your Current PIN : "))
                qurey = f"select password from bank where password ='{passwo}'"
                mycursor.execute(qurey)
                result =  mycursor.fetchone()
                passwor= result
                try:
                    if passwo in passwor:
                        deposit = int(input("Enter Your Deposit Amount : "))
                        sleep(1)
                        print("Your Transaction is being Processed.\n\t  Please Wait..")
                        sleep(3)
                        qu = "update bank set depo  = depo + {},balance = depo  where password = {}".format(deposit,passwo)
                        mycursor.execute(qu)
                        dbc.commit()
                        
                        print("Transaction Complete\nPlease Take Your Card.")
                    
                except TypeError:
                      print("Invalid PIN NO...")
                
                except Exception:
                      print("Somthing wrong...!")
                
        elif choice == 3:
                passwo = int(input("Please Enter Your Current PIN : "))
                msg = f"select password from bank where password = '{passwo}'"
                mycursor.execute(msg)
                result = mycursor.fetchone()
                passwor = result
                try:
                    if passwo in passwor:
                        amount = int(input("Please Enter Amount.\n(Cash Available : Rs 100, Rs 500, Rs 200 ) : "))
                        qur1 = "update bank set amount = {} where password ={}".format(amount,passwo)
                        qur2 = "update bank set balance = balance - {} where password ={}".format(amount,passwo)
                        mycursor.execute(qur1)
                        mycursor.execute(qur2)
                        dbc.commit()
                        print("Your Transaction is being Processed.\n\t Please Wait..")
                        sleep(4)
                        print("Please Collect Cash and Take Your Card.")
                        sleep(2)
                        print("           Thank you.")
                        
                except TypeError:
                            print("Incorrect PIN NO...")
                
                except Exception:
                      print("Somthing wrong...!")

        elif choice == 4:
              passwo = int(input("Please Enter Your Current PIN :"))
              ms = "select password from bank where password = %s"% passwo
              mycursor.execute(ms)
              output = mycursor.fetchone()
              res = list(output)
              for x in res:
                        result1 = x
              if passwo ==  result1:
                msg1 = "select balance from bank where password = %s"%passwo
                mycursor.execute(msg1)
                show = mycursor.fetchone()
                show1 = sorted(show)
                print("Your Balance Amount is : ",show1)
              elif passwo not in result:
                    print("Invalid PIN...")
              
              
              
    else:
        print("Invalid Card...")            


atm()










