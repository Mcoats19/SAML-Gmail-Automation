# 📧 SAML-Gmail Automation

Automate email sending using the **Gmail API** while securing user authentication with **SAML**. This project combines robust authentication with email automation for seamless integration into modern applications.

---

## 🚀 Features
- **🔒 SAML Authentication:** Secure login through your Identity Provider (IdP).
- **📨 Gmail API Integration:** Automate sending emails programmatically.
- **🔗 RESTful Endpoints:** Simple and scalable endpoints for email automation.

---

## 📂 Project Structure
```plaintext
saml-gmail-automation/
├── src/
│   ├── saml_auth.py       # Handles SAML authentication
│   ├── gmail_api.py       # Gmail email automation logic
│   ├── config.py          # Configuration file
│   └── app.py             # Flask app entry point
├── credentials/
│   ├── credentials.json   # Gmail API OAuth credentials
│   └── saml_metadata.xml  # SAML IdP metadata
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
└── .gitignore             # Files to ignore
