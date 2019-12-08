print("Hi! Let Me tell you what the hell we are trying to do with this. This is just another random python script to add the list of variables that can run through your mind. what you can do is you can add a list of variable that may be used in common use based on the platform we will all be working in any of the field. for now we must focus on building a first version of list of variales for us.")
print("what this script will do is do nothing, just ask you to add a vaiable and another is description or the scenario where it is used.")

fp = open('variable.txt', 'a+')
while(1):
    a = str (input('Enter vaiable name: '))
    b = str (input('\n Enter the scenario in which it is used:'))
    fp.write(a+'='+' '+ b+'\n')
    continue