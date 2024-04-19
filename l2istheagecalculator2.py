import datetime
name = input("Heya, so what's your name?: ")
print(f"Thanks, {name}, now let's figure out ya age!") 
current_year = datetime.datetime.now().year
age = (current_year - int(input("What year were you born?:"))) * 365  
if age >= 18:
    print(f"Chile, you got a lot of adventures ahead of you {name}!")
if age >= 50:
    print(f"yes {name}, with the gold brick roads, Come on Dorothy!") 
if age >= 80:
    print("Damn! Cool! But it's giving very much knowledge")
else:
    print("Senpai")