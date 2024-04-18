import datetime
summer= ["june", "july"] #sunshine
winter= ["november", "december", "january","february", "march", "april"] #random and cold
gloom_weather =["everyday"] #everyday weather
current_month=datetime.datetime.now().month
current_day=datetime.datetime.now().day
user_season=input("chile!what season is it?")
current_month=datetime.datetime.now().month
if current_month in range (11,5):
    print("youre in for a real british treat")
elif current_month in range(6,8):
    print("well this is awkward? but i guess its nice?")
else:
    print("the good ole brit gloom ey?")