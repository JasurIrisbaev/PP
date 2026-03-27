import csv
from connect import connect
from config import load_config


# 1. Добавление из CSV
def insert_from_csv(conn, filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        with conn.cursor() as cur:
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
    conn.commit()
    print("Data inserted from CSV")


# 2. Добавление с консоли
def insert_from_console(conn):
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
    conn.commit()
    print("Contact added")


# 3. Обновление
def update_contact(conn):
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )
    conn.commit()
    print("Updated")


# 4. Поиск
def search_contacts(conn):
    keyword = input("Search: ")

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s",
            (f"%{keyword}%", f"{keyword}%")
        )
        rows = cur.fetchall()

        for row in rows:
            print(row)


# 5. Удаление
def delete_contact(conn):
    value = input("Enter name or phone to delete: ")

    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM phonebook WHERE name = %s OR phone = %s",
            (value, value)
        )
    conn.commit()
    print("Deleted")


# 6. Показать все
def show_all(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()

        for row in rows:
            print(row)


# МЕНЮ
def main():
    config = load_config()
    conn = connect(config)

    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Insert from CSV")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Search")
        print("5. Delete")
        print("6. Show all")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv(conn, "contacts.csv")
        elif choice == "2":
            insert_from_console(conn)
        elif choice == "3":
            update_contact(conn)
        elif choice == "4":
            search_contacts(conn)
        elif choice == "5":
            delete_contact(conn)
        elif choice == "6":
            show_all(conn)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()