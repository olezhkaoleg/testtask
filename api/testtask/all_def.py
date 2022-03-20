import sqlite3

id = '1'

def request_all_orders():
  try:
    sqlite_connection = sqlite3.connect('C:\\Users\\olezhlaoleg\\Documents\\api\\testtask\\test_task.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT customer.full_name, manager.full_name, purchase_amount, date FROM 'order' a INNER JOIN manager on a.manager_id = manager.manager_id INNER JOIN customer on a.customer_id = customer.customer_id GROUP BY a.order_no;")
    all_result = cursor.fetchall()
    cursor.close()
    sqlite_connection.close()
    return all_result
  except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


#print(request_all_orders())

def request_order(id):
  try:
    sqlite_connection = sqlite3.connect('test_task.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT customer.full_name, manager.full_name, purchase_amount, date FROM 'order' a INNER JOIN manager on a.manager_id = manager.manager_id INNER JOIN customer on a.customer_id = customer.customer_id WHERE order_no =" + id + ";")
    result = cursor.fetchone()
    cursor.close()
    sqlite_connection.close()
    return result
  except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

#print(request_order(id))

def request_customer(id):
  try:
    sqlite_connection = sqlite3.connect('test_task.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT customer.full_name, manager.full_name, purchase_amount, date FROM 'order' a INNER JOIN manager on a.manager_id = manager.manager_id INNER JOIN customer on a.customer_id = customer.customer_id WHERE customer.customer_id = " + id +";")
    result = cursor.fetchall()
    cursor.close()
    sqlite_connection.close()
    return result
  except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

#print(request_customer(id))

def request_manager(id):
  try:
    sqlite_connection = sqlite3.connect('test_task.db')
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT customer.full_name, manager.full_name, purchase_amount, date FROM 'order' a INNER JOIN manager on a.manager_id = manager.manager_id INNER JOIN customer on a.customer_id = customer.customer_id WHERE manager.manager_id = " + id +";")
    result = cursor.fetchall()
    cursor.close()
    sqlite_connection.close()
    return result
  except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


#print(request_manager(id))

def new_order(price, date, customer_id, manager_id):
  with sqlite3.connect("test_task.db") as conn:
    orders = (      price,
                    date,
                    customer_id,
                    manager_id)


    conn.execute(
                """
                    insert into 'order'(purchase_amount, date, customer_id, manager_id)
                    values(?, ?, ?, ?)
                """,
                orders
            )

    conn.commit()
