#####question_1##############
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores=scores.split(" ")
a_scores=0
for i in range(len(scores)):
    scores[i]=int(scores[i])
    if scores[i]>= 90:
        a_scores+=1 
#####################################
#######Question_2####################
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=[]
org=org.split(" ")
for n in org:
    if n in stopwords:
        continue
    else:
        acro.append(n[0])
acro="".join(acro)
acro=acro.upper()
#####################################
######Question_3#####################
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro=[]
sent=sent.split(" ")
for n in sent:
    if n in stopwords:
        continue
    else:
        acro.append(n[0:2])
acro=". ".join(acro)
acro=acro.upper()
##############################
#####Question_4############## 
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]

print(r_phrase)
#############################
########Question_5###########
for i in inventory:
    yoo = i.split(',')
    name = yoo[0]
    item = yoo[1]
    price = yoo[2]
    
    print("The store has{} {}, each for{} USD.".format(item, name, price))        