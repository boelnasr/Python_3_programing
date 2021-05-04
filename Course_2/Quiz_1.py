########################
######Question_1########
file=open("travel_plans.txt","r")
content=file.read()
num=len(content)
########################
######Question_2########
file=open("emotion_words.txt","r")
lines=file.readlines()
num_words=0
for i in range(len(lines)):
    x=lines[i].split(" ")
    num_words+=len(x)
file.close()               
########################
######Question_3########
file=open("school_prompt.txt","r")
lines=file.readlines()
num_lines=len(lines)
########################
######Question_4########
file=open("school_prompt.txt","r")
content=file.read()
beginning_chars=content[0:30]
########################
######Question_5########
file=open("school_prompt.txt","r")
lines=file.readlines()
three=[]
for i in range(len(lines)):
    x=lines[i].split(" ")
    three.append(x[2])
file.close()               
########################
######Question_6########
file=open("emotion_words.txt","r")
lines=file.readlines()
x=lines[0].split(" ")
emotions=[]
for i in range(len(lines)):
    x=lines[i].split(" ")
    emotions.append(x[0])
########################
######Question_7########
file=open("travel_plans.txt","r")
content=file.read()
first_chars=content[0:33]
#########################
######Question_8########
file=open("school_prompt.txt","r")
lines=file.readlines()
x=lines[0].split(" ")
p_words=[]
for line in lines:
    word = line.split()
    for i in word:
        
        if 'p' in i:
            print(i)
            p_words.append(i)
file.close()               
            
