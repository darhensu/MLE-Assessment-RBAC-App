from flask import Flask, request, jsonify
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Beberapa yang di remark adalah code sebelum perbaikan


app = Flask(__name__)

# Buat dummy permission
# permissions = {
#     "edit_document": "Can i edit this document?",
#     "view_document": " Can i view this document"
# }

# vectorizer = CountVectorizer().fit_transform(permissions.values())
# vectors = vectorizer.toarray()
vectorizer = CountVectorizer()

# Corpus untuk melatih vectorizer
corpus = [
    'Can i edit this document?',
    'Can i view this document?',
    'Can i delete this?',
    'Can i update this document?',
    'Can i download this file?',
    'Can i upload this file?'
]

vectorizer.fit(corpus)

# Fungsi untuk mendapatkan permissions user dari database
def get_user_permissions(user_id):
    conn = sqlite3.connect('rbac.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.permission_name
        FROM permission p
        JOIN rolepermission rp ON rp.permission_id = p.id
        JOIN user u ON u.role_id = rp.role_id
        WHERE u.id = ?
    """, (user_id,))
    user_permissions = [row[0] for row in cursor.fetchall()]
    conn.close()
    return user_permissions

# Endpoint untuk cek akses
@app.route('/check-access', methods=['POST'])
def check_access():
    try:
        data = request.json
        user_id = data.get('user_id')
        intent = data.get('intent')
        print(user_id, intent)
    
    # Tranformasi intent user ke vektor numerik
        user_intent_vec = vectorizer.transform([intent]).toarray()
    # similarities = cosine_similarity(user_intent_vec, vectors)
    # best_match_idx = similarities.argmax()
    # detected_permission = list(permissions.keys())[best_match_idx]
    
    # cek user's permission dari db
    # conn = sqlite3.connect('rbac.db')
    # cursor = conn.cursor()
    # cursor.execute(""" 
    #                select p.permission_name
    #                from permission p
    #                join rolepermission rp on rp.permission_id =  p.id)
    #                join user u on u.role_id = rp.role_id
    #                where u.id = ? """, (user_id,))
    # user_permissions = [row[0] for row in cursor.fetchall()]
    # conn.close()
    
    # if detected_permission in user_permissions:
    #     return jsonify({"access": "granted", "permission": detected_permission})
    # return jsonify({"access": "denied",  "permission": detected_permission})
        # Ambil permissions user dari database
        user_permissions = get_user_permissions(user_id)
        print(f"User Permissions: {user_permissions}")

        # Menentukan permission yang sesuai dengan intent
        if 'edit' in intent:
            permission = 'edit_document'
        elif 'view' in intent:
            permission = 'view_document'
        elif 'delete' in intent:
            permission = 'delete_document'
        else:
            permission = 'unknown'

        # Cek user memiliki permission untuk melakukan aksi
        if permission in user_permissions:
            access = 'granted'
        else:
            access = 'denied'

        return jsonify({
            'access': access,
            'permission': permission
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)