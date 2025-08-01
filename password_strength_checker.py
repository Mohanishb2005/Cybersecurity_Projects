import re
def password_checker(password):
    score = 0
    feedback = []

    if len(password) > 8:
        score +=1
    else:
        feedback.append("Password should be atleast 8 characters long")

    if re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("Add atleast one lowercase characters") 

    if re.search(r"\d",password):
        score +=1
    else:
        feedback.append("Add atleast one digit")

    if re.search(r"[!@#$%^&*(),./?{}|]",password):
        score +=1
    else:
        feedback.append("Add atleast one special character")

    if score==5:
        strength="strong"

    elif score >= 3:
        strength="Moderate"

    else:
        strength="Weak"

    return strength,feedback                                          


