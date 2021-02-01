"""
Django secret settings example.
"""
settings_secret = {
    'SECRET_KEY': 'l@#4p%$jn2)_qycb($*fsc4kekh+q&twr)wvb^9zd*-#y&c!3=',

    # Databases
    'DATABASES': {
        'default': {
            'name': 'db',
            'host': 'db',
            'user': 'root',
            'password': 'root',
            'port': 3306
        }
    }
}
