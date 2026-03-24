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
    if any(not c.isalnum() for c in password): #random but my cat was peaking at me at the door while coding, that jumpscared me so bad
        score += 1
    #i am 90% sure that this code is optimizable but my python knowledge ends here, maybe in the future
    if password.lower() in ["password", "123456", "qwerty"]: #NO WAY theres actual people who do this tho
        score -= 3
    if len(set(password)) < len(password) / 2:
        score -= 1 
    return score # almost forgot this
#levels to score
def get_strength(score):
    if score <= 2:
        return "Very Weak"
    elif score <= 4:
        return "Weak"
    elif score <= 6:
        return "Medium"
    elif score <= 8:
        return "Strong"
    else:
        return "Very Strong"
def feedback(password):
    tips = []

    if len(password) < 12:
        tips.append("Make it longer")

    if not any(c.isupper() for c in password):
        tips.append("Add uppercase letters")

    if not any(c.isdigit() for c in password):
        tips.append("Add numbers")

    if not any(not c.isalnum() for c in password):
        tips.append("Add symbols (!@#)")

    return tips
pw = input("Enter password: ")

score = passwordcheck(pw)
strength = get_strength(score)

print("Score:", score)
print("Strength:", strength)

for tip in feedback(pw):
    print("-", tip)
    #please no bugs plz
    #there were no bugs YAY
