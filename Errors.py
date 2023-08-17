def getError(ID):   
    if ID == 0:
        return "Success!"
    if ID == 1:
        return "User already exists"
    elif ID == 2:
        return "Invalid credentials"
    elif ID == 3:
        return "Pass Codes doesn't match"