def get_user_name():
    user_name= input("Imagine a world where you had everything you ever wanted what would your name be?:").lower()
    print ("Hello," user_name, "welcome to Superconscious You!")
    return user_name
name=get_user_name
def get_qualities():
    while True:
        user_qualities=input("describe {name} in three words: ").split()
        if len(user_qualities) == 3:
            print ("okay", qualities[0], "i see you!," ,qualities[1],",",qualities[2], ",come through qualities")
            return user_qualities
    elif len(user_qualities) > 3:
        print:("chile! did you even try?,Come on 3")
        return user_qualities
    else 
        print:("alright,over achiever, i only asked for 3")
        return user_qualities
qualities=get_qualities
verb=("i love it!, so now roleplay! what does {name}do?")
dig=("what is{name}passionate about?")
print("so let me get this straight!{qualities},{name}is a {verb} who gets to enjoy{dig} and you dont? and were all supposed to be okay about it?":"")
response= input("Oh what so you just gonna stand there huh? What you too cute to change or you scared?:")
if "cute" in response:
    print("hmm! alright(user_name), why dont you take a breather! do a 15 min meditation and come back junior")
    break
        
elif  "scared"  in response:
    print("Hmm, alright well alls im saying is you can change that sweetpea. So you want my help? (yes?/no?):").lower()
    help_answer=input().lower
    if help_answer == "yes":
        print("Thats the spirit!,lets spruce this up a bit")
    else:("hmm! alrigh(user_name), why dont you take a breather! do a 15 min meditation and come back junior")
else:
        print("what you a statue now? Come on sugar foot, give me something to work with at least:")
