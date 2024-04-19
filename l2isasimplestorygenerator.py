name=input("welcome!imagine a world where you had everything you ever wanted what would your name be?:").lower()
qualities=input("describe {name} in three words:").split()
verb=("i love it!, so now roleplay! what does {name}do?")
dig=("what is{name}passionate about?")
print("so let me get this straight!{qualities},{name}is a {verb} who gets to enjoy{dig} and you dont? and were all supposed to be okay about it?":"")
response= input("Oh what so you just gonna stand there huh? What you too cute to change or you scared?:")
if "cute" in response:
    print("hmm! alrigh, why dont you take a breather! do a 15 min meditation and come back junior")
    break
        
elif  "scared"  in response:
    print("Hmm, alright well alls im saying is you can change that sweetpea. So you want my help? (yes?/no?):").lower()
    help_answer=input().lower
    if help_answer == "yes":
        print("Thats the spirit!,lets spruce this up a bit")
    else:("hmm! alrigh, why dont you take a breather! do a 15 min meditation and come back junior")
else:
    print("what you a statue now? Come on sugar foot, give me something to work with at least:")
