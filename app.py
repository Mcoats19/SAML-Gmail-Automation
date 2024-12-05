from flask import Flask, request, jsonify, redirect
from saml_auth import saml_login, saml_logout
from gmail_api import send_email
import config

app = Flask(__name__)

@app.route('/saml/login', methods=['GET'])
def login():
    auth_url = saml_login(request_data=request)
    return redirect(auth_url)

@app.route('/saml/logout', methods=['GET'])
def logout():
    logout_url = saml_logout(request_data=request)
    return redirect(logout_url)

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    sender = data.get('sender')
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    try:
        response = send_email(sender, recipient, subject, body)
        return jsonify({"status": "success", "message_id": response['id']})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
