import  random

for i in range(3):
    print(random.randint(0,10))


members = ['John', 'Mart', 'Gleb', 'Sofia']
leader: str = random.choice(members)
print(leader)
