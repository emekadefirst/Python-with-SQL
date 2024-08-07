import sqlite3

con = sqlite3.connect('opay.db')
db = con.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS users
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT VARCHAR(12) NOT NULL,
                last_name TEXT VARCHAR(12) NOT NULL,
                other_name TEXT VARCHAR(12) NOT NULL,
                username TEXT VARCHAR(12) UNIQUE NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone_number INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                address TEXT NOT NULL,
                nin INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
           ''')


def create_user(first_name,
                last_name,
                other_name,
                email,
                username,
                password,
                phone_number,
                account_number,
                address,
                nin):
    db.execute(
        "INSERT INTO users (first_name, last_name, other_name, email, username, password, phone_number, account_number, address, nin) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (
            first_name,
            last_name,
            other_name,
            email,
            username,
            password,
            phone_number,
            account_number,
            address,
            nin
            )
    )
    con.commit()
    return "New user created successfully"

def get_all():
    db.execute("SELECT * FROM users")
    rows = db.fetchall()
    return rows
    
def get_by_id(id):
    db.execute("SELECT * FROM users WHERE id =?", (id,))
    row = db.fetchone()
    return row

def update(id,
           first_name,
                last_name,
                other_name,
                email,
                username,
                password,
                phone_number,
                account_number,
                address,
                nin
           ):
    db.execute("UPDATE users SET first_name =?, last_name =?, other_name =?, email =?, username =?, password =?, phone_number =?, account_number =?, address =?, nin =? WHERE id =?", 
        first_name,
        last_name,
        other_name,
        email,
        username,
        password,
        phone_number,
        account_number,
        address,
        nin,
        id
        )
    con.commit()
    return "User updated successfully"

def delete(id):
    db.execute("DELETE FROM users WHERE id =?", (id,))
    con.commit()
    return "User deleted successfully"

# con.close()