import sqlite3

# Membuka koneksi ke db
conn = sqlite3.connect('rbac.db')
cursor = conn.cursor()

# Menambah data untuk role
cursor.execute("insert into role(role_name) values('Editor')")
cursor.execute("insert into role(role_name) values('Viewer')")

# Menambah data untuk permission
cursor.execute