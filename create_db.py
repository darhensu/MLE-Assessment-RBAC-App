import sqlite3

# Membuat komeksi ke db 
conn = sqlite3.connect('rbac.db')
cursor = conn.cursor()

# Mmbuat tabel role
cursor.execute(""" create table if not exists role (
    id integer primary key autoincrement,
    role_name text not null
)""")

# MEmbuat tabel permission
cursor.execute(""" create table if not exists permission (
    id integer primary key autoincrement,
    permission_name text not null
)""")

# Membuat tabel user
cursor.execute(""" create table if not exists user (
    id integer primary key autoincrement,
    username text not null,
    email text not null,
    role_id integer,
    foreign key (role_id) references role(id)
)""")

# Membuat tabel rolepermission
cursor.execute(""" create table if not exists rolepermission(
    id integer primary key autoincrement,
    role_id integer,
    permission_id integer,
    foreign key (role_id) references role(id),
    foreign key (permission_id) references permission(id)
)""")

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()

print("Database and tables created sucessfuly!")
