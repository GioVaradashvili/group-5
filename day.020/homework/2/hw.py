crew_members = ['dachi sazandrishvili', 'gio varadashvili', 'giorgi gelashvili', 'jemuka kaxidze', 'luka kevkhishvili', 'luka tevzadze', 'luka turadze', 'nikoloz gogniashvili', 'nikoloz filishvili']

long_names = []

for i in crew_members:
    if len(i) >= 18:
        long_names.append(i)

print(long_names)