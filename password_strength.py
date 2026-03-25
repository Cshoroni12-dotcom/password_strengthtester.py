import random
import string

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
def strongpass():
    chars = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(chars) for _ in range(16))
    print("p.s dont forget to write it somewear")
    print("-------------------------------------")
    print(result)
    print("-------------------------------------")
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


def advanced_charset(password):
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(not c.isalnum() for c in password)

    size = 0

    if lower:
        size += 26
    if upper:
        size += 26
    if digit:
        size += 10
    if symbol:
        size += 32

    variety = sum([lower, upper, digit, symbol])
    size += variety * 2  #this should help
    return size


#going to add a system that will track how long it will to take a skilled hacker to crack your password
def estimate_crack_time(password):
    charset = advanced_charset(password)
    combinations = charset ** len(password) #big brain math stuff

    guesses_per_second = 1_000_000_000 #assuming hacker is SPEED or just pro
    seconds = combinations / guesses_per_second

    return seconds


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years" #ok if its years just give up hacking bro

print("Hello Please Enter the password you want to check the strength of: ")
print("----------------------------------") #please dont let this grt over the screen
pw = input("Enter password: ")

score = passwordcheck(pw)
strength = get_strength(score)
time_sec = estimate_crack_time(pw)

print("Score:", score)
print("Strength:", strength)
print("Estimated crack time:", format_time(time_sec))

tips = feedback(pw)
if tips:
    print("Suggestions:")
    for tip in tips:
        print("-", tip) #i am not going to lie, no ordered me to put this what does this do? let me delete this//ook that's what it does how d ca id i not think? maybe its cause its midnight and i have  a history  test twomorrow
        print("----------------------------------") #please dont let this grt over the screen--
yn = input("or will you want us to generate a crack-proof password? press y for yes n for no: ")
if yn == 'y':
    print("Cool! here's a good password for you:")
    strongpass()
elif yn == 'n':
    print("thank you for checking! have a nice day!")
            
    #please no bugs plz
    #there were no bugs YAY
    #add more cool print menu soooooo maybe twomorrow mornign
    #added more cool print menu and also a random password generator
    #ummm so the tip menu always appears.....
    #that was a wierd error
    #hmmm i think it was because its the loop fixed tho!
