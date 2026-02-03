import time as t
import mysql.connector


def bill():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password", #enter your password
    database="your database name", #enter your database name
    use_pure=True
    )
    cur = con.cursor()
    Order_id=int(input("enter the order id: "))
    Prod_Name=input("enter the product name: ")
    Prod_Price=float(input("enter the P_Price: "))
    prod_Quantity=int(input("enter the Quantity: "))
    Amount=Prod_Price*prod_Quantity
    sql = "INSERT INTO order1 (Order_id,Prod_name,Prod_Price,prod_Quantity,Amount) VALUES (%s,%s,%s,%s,%s)"
    values = (Order_id,Prod_Name,Prod_Price,prod_Quantity,Amount)
    cur.execute(sql,values)
    con.commit()
    print("Data successfully inserted into Products table!")

    amount=Prod_Price*prod_Quantity
    name=str(Order_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time}
    --------------------
    order id: {Order_id}
    product name: {Prod_Name}
    Quantity: {prod_Quantity}
    ---------------------
    final amount: {amount}''')
    f.close()
    cur.close()
    con.close()
    
bill()
