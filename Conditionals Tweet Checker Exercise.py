t_input = input("Enter your tweet! : ")
max = 140
t_len = len(t_input)

excess = t_len - 140

if (t_len < max):
    print(f"That {t_len} char tweet will work!")
else:
    print(f"Your {t_len} char tweet is {excess} chars too long")
    
    