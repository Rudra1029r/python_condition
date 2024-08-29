pswd = "Rudra@123"

if len(pswd) < 6:
    show = "Weak password"
elif len(pswd) <=10:
    show = "Medium password"
elif len(pswd) >10:
    show = "Strong password"
    
print(show);    
    