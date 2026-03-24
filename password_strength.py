def passwordcheck(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 10:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1
    if password.lower() in ["password", "123456", "qwerty"]: #NO WAY theres actual people who do this tho
        score -= 3
    if len(set(password)) < len(password) / 2:
        score -= 1 
    return score # almost forgot this
