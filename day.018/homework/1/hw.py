crew_members =  ['giorgi varadashvili', 'giorgi gelashvili', 'jemuka kaxidze', 'luka kevkhishvili', 'luka tevzadze', 'luka turadze', 'nikoloz gogniashvili', 'nikoloz filishvili']

supersia = []


for i in crew_members:
    if i.lower().count("i") > 2:
        supersia.append(i.capitalize())
for i in supersia:
    print(i)