# Role-Based Access Control (RBAC) with NLP-based Permission Check

## Deskripsi

Aplikasi ini mengimplementasikan **Role-Based Access Control (RBAC)** dengan menggunakan backend berbasis model **Natural Language Processing (NLP)** untuk mendeteksi niat (intent) dari input teks pengguna, seperti "Can I edit this document?" dan memberikan akses sesuai dengan peran dan izin yang ditentukan di database.

Aplikasi ini terdiri dari beberapa komponen:
- **Flask** sebagai framework backend untuk menyediakan API.
- **SQLite** sebagai database untuk menyimpan data pengguna, peran (roles), dan izin (permissions).
- **CountVectorizer** dari `scikit-learn` untuk mengubah input teks menjadi representasi vektor numerik yang digunakan untuk membandingkan intent pengguna dengan izin yang ada.
- **Cosine Similarity** untuk menghitung kesamaan antara intent pengguna dan izin yang tersedia.

## Struktur Database

Database terdiri dari beberapa tabel utama:
1. **Users** - Menyimpan informasi pengguna.
2. **Roles** - Menyimpan peran yang tersedia.
3. **Permissions** - Menyimpan izin yang ada.
4. **RolePermissions** - Menyimpan relasi antara peran dan izin yang dimiliki.

## Tabel-tabel

1. **Users**
    - `id` (INTEGER, PK)
    - `name` (TEXT)
    - `role_id` (INTEGER, FK ke Roles.id)

2. **Roles**
    - `id` (INTEGER, PK)
    - `role_name` (TEXT)

3. **Permissions**
    - `id` (INTEGER, PK)
    - `permission_name` (TEXT)

4. **RolePermissions**
    - `id` (INTEGER, PK)
    - `role_id` (INTEGER, FK ke Roles.id)
    - `permission_id` (INTEGER, FK ke Permissions.id)

## Fitur

1. **Cek Akses Pengguna**
   - Endpoint untuk memeriksa akses pengguna berdasarkan input teks.
   - Mendeteksi intent dari teks pengguna dan mencocokkannya dengan izin yang ada di database.
   - Mengembalikan status akses (diberikan atau ditolak) dan izin yang terkait.

2. **Database untuk Pengelolaan Pengguna dan Peran**
   - Menyimpan data pengguna, peran, dan izin dalam database.
   - Menentukan izin yang dimiliki oleh setiap peran.

## Instalasi

1. **Clone Repositori**
    ```bash
    git clone <repository-url>
    cd <folder-repository>
    ```

2. **Install Dependencies**
    Pastikan Anda sudah menginstall Python dan `pip`. Kemudian, install dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

3. **Siapkan Database**
    - Jalankan script untuk membuat database dan tabel-tabel yang diperlukan:
    ```bash
    python create_db.py
    ```

4. **Isi Tabel dengan Data**
    - Jalankan script untuk mengisi tabel dengan data yang sesuai:
    ```bash
    python add_data.py
    ```    

## Menjalankan Aplikasi

Untuk menjalankan aplikasi, gunakan perintah berikut:
```bash
python app.py

Aplikasi akan berjalan di http://127.0.0.1:5000/check-access melalui postman
```

Contoh test input dan juga output berada pada dokumen test.txt
