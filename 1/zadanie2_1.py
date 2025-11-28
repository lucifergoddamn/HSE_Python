boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    print("Идеальные пары:")
    for boy, girl in zip(sorted_boys, sorted_girls):
        print(f"{boy} и {girl}")