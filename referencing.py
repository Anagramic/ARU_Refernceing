source = ""
while source =="":
    source = input("What type of source is it?(eg PDF) ")
authors = []

title = ""
while title =="":
    title = input("What is the title of the dcument? ")


while True:
    author = input("Add an author (or press ENTER to end): ")   
    
    if author !="":
        try:
            a,b = author.split(" ")
            authors.append(author)
        except:
            print("First and last name required")
            continue

    elif len(authors)!=0:
        break


finalauthors = []
for author in authors:
    fname, sname = author.split(" ")
    fnameInitial = fname[0].upper()
    finalauthors.append(sname.capitalize()+","+fnameInitial+".")


final = []
if len(finalauthors)-1 != 0:

    for i in range(0,len(finalauthors)):

        if i < len(finalauthors)-1:
            final.append(finalauthors[i]+", ")
        else:
            final.append("and "+finalauthors[i]+" .")
else:
    final.append(finalauthors[0]+" .")


publisher = ""
while publisher =="":
    publisher = input("Who are the publishers? ")


publishDate = ""
while publishDate =="":
    publishDate = input("When was it published? ")

link = ""
while link =="":
    link = input("What's the link? ")


date = ""
while date =="":
    date = input("When was it accessed? ")


final.append(" "+str(publishDate)+". "+title.capitalize()+" ["+source+"] "+publisher.capitalize()+". Available at "+link+"\n[Accessed "+date+"].")

print("\n\n\n"+("".join(final))+"\n\n\n")

x = input("Press enter to close")