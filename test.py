AWS_SECRET_KEY = '4e&6bz+(5&cg^_!05r(&7_#dghg_smrojq(yk)xa^bwg7j)^*j'
KEY = '0fXmr002SuelwlPgNWs1FIiMSRcRvm9e'
USER = "Vishal"
PASSWORD = "PASS@!23"
DB = "db+srv://my-user:PASS@!23@clustername.db.net/"
PASS = "abc12345abc12345abc12345abc12345abc12345abc"
def login(user, password):
    if user==USER and password==PASSWORD:
        return True
    else:
        return False
login(user="Vishal", password="PASS@!23")

SECRET_KEY = '.v2QPKHl7LcdVYsjaR4LgQiZ1zw3MAnMyiondXC63'