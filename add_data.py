import sqlite3

# Membuka koneksi ke db
conn = sqlite3.connect('rbac.db')
cursor = conn.cursor()

# Menambah data untuk role
cursor.execute("insert into role(role_name) values('Editor')")
cursor.execute("insert into role(role_name) values('Viewer')")

# Menambah data untuk permission
cursor.execute("insert into permission(permission_name) values('edit_document')")
cursor.execute("insert into permission(permission_name) values('view_document')")

# Menambah user dengan role
cursor.execute("insert into user(username, email, role_id) values('suhendar','suhendar@example.com', 1)")
cursor.execute("insert into user(username, email, role_id) values('aditya','aditya@example.com', 2)")

# Menambah role permission
cursor.execute("insert into rolepermission(role_id, permission_id) values(1, 1)") # Editor -> edit_document
cursor.execute("insert into rolepermission(role_id, permission_id) values(2, 2)") # Viewer -> view_document

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()

print("Data added successfully!")