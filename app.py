from flask import Flask, request, jsonify
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Buat dummy permission
permissions = {
    "edit_document": "Can i edit this document?",
    "view_document": " Can i view this document"
}
vectorizer = CountVectorizer().fit_transform(permissions.values())
vectors = vectorizer.toarray()

@app.route('/check-access', methods=['POST'])
def check_access():
    data = request.json
    user_id = data.get('user_id')
    intent = data.get('intent')
    
    # Model NLP untuk deteksi intent
    user_intent_vec = vectorizer.transform([intent]).toarray()
    similarities = cosine_similarity(user_intent_vec, vectors)
    best_match_idx = similarities.argmax()
    detected_permission = list(permissions.keys())[best_match_idx]
    
    # cek user's permission dari db
    conn = sqlite3.connect('rbac.db')
    cursor = conn.cursor()
    cursor.execute(""" 
                   select p.permission_name
                   from permission p
                   join rolepermission rp on rp.permission_id =  p.id)
                   join user u on u.role_id = rp.role_id
                   where u.id = ? """, (user_id,))
    user_permissions = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    if detected_permission in user_permissions:
        return jsonify({"access": "granted", "permission": detected_permission})
    return jsonify({"access": "denied",  "permission": detected_permission})

if __name__ == '__main__':
    app.run(debug=True)