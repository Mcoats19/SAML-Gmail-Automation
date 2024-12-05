from onelogin.saml2.auth import OneLogin_Saml2_Auth

def init_saml_auth(request_data):
    settings = {
        'sp': {
            'entityId': 'https://your-app-url.com/metadata/',
            'assertionConsumerService': {
                'url': 'https://your-app-url.com/acs/',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
            },
            'singleLogoutService': {
                'url': 'https://your-app-url.com/sls/',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
            }
        },
        'idp': {
            'entityId': 'https://idp-entity-id',
            'singleSignOnService': {
                'url': 'https://idp-sso-url',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
            },
            'x509cert': open("credentials/saml_metadata.xml").read()
        }
    }
    return OneLogin_Saml2_Auth(request_data, settings)

def saml_login(request_data):
    auth = init_saml_auth(request_data)
    return auth.login()

def saml_logout(request_data):
    auth = init_saml_auth(request_data)
    return auth.logout()
