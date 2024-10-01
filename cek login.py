def cek_login(username , password):
    database_username = "AHMADZ354"
    database_password = "heheh"
    if(username == database_username and password == database_password):
        return "selmat anda bisa login"
    else :
        return "password dan userbame anda ada yang salah"

print(cek_login("AHMADZ354","lupa sandi"))