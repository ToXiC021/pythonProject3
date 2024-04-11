import pymysql


def create_database():
    try:
        db_name = input("insert a name: ")
        query = f"""CREATE DATABASE IF NOT EXISTS {db_name}"""
        cursor.execute(query)
        connection.commit()
        print("Done.")
        if input("Will you change current base to this new database (yes or no): ").Lower() in ("yes", "y"):
            query = f"""USE {db_name} database"""
            cursor.execute(query)
    except:
        print("Something wrong. Operation is not completed.")

def change_database():
    try:
        query = f"""USE {input("insert a name: ")}"""
        cursor.execute(query)
        print("Done.")
    except:
        print("Something wrong. Operation is not completed.")
def create_table():
    pass
def insert_info_to_table():
    pass
def delete_info_from_table():
    pass
def update_info_from_table():
    pass
def show_some_info():
    pass



try:
    with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:
        print(connection, "OK")
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)

            cursor.execute("CREATE DATABASE IF NOT EXISTS TESTIK")

            print("-------------")
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)



            cursor.execute("CREATE DATABASE IF NOT EXISTS ACADEMY")
            cursor.execute("USE ACADEMY")

            cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS teachers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100),
                second_name VARCHAR(100),
                age INT
            )
            """
           )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS groups (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    auditory VARCHAR(10)
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS teachers_and_groups (
                    teacher_id INT,
                    group_id INT,
                    PRIMARY KEY(teacher_id, group_id),
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
                    FOREIGN KEY (group_id) REFERENCES groups(id),
                )
                """
            )

            cursor.execute("USE ACADEMY")
            cursor.execute(
                '''INSERT INTO teachers -(first_name, second_name, age)  VALUES ('vasya', 'vasin', 50)'''
            )
            connection.commit()

            cursor.execute("SELECT * FROM teachers")
            for line in cursor:
                print(line)


            while True:
                print("1. Create database.")
                print("2. Change database.")
                print("3. Create table in database.")
                print("4. Insert info in to a table.")
                print("5. Delete info from a table.")
                print("6. Update info in a table.")
                print("7. Show some info.")
                print("0. Quit.")
                user_choice = input("Your choice: ")
                match user_choice:
                    case "1": create_database()
                    case "2": change_database()
                    case "3": create_table()
                    case "4": insert_info_to_table()
                    case "5": delete_info_from_table()
                    case "6": update_info_in_table()
                    case "7": show_some_info()
                    case "0": quit()
                    case_: print("Unknown command. Try again.")




except pymysql.Error as e:
    print(e)







