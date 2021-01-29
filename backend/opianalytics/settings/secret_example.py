"""
Django secret settings example.
"""
settings_secret = {
    'SECRET_KEY': '',

    # AWS
    'AWS': {
        'S3': {
            'ACCESS_KEY_ID': '',
            'SECRET_ACCESS_KEY': ''
        }
    },

    # Mailgun
    'MAILGUN': {
        'API': ''
    },

    # Databases
    'DATABASES': {
        'default': {
            'name': '',
            'host': '',
            'user': '',
            'password': '',
            'port': 3306
        }
    },

    # Email configuration
    'EMAIL': {
        'host': '',
        'user': '',
        'password': '',
        'port': 587,
        'tls': True
    }
}
