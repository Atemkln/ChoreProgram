import random
chores = ['Dishes', 'Sweeping', 'Garbage', 'Dusting', 'Bathrooms', 'Yard-work', 'Windows']
members = ['John', 'Kieran', 'Sammy', 'Titouan', 'Ivan', 'Owen', 'Eric']


def chore_program(chore_list, members_list):
    chore_assignment = random.sample(chore_list, 7)
    for i in range(len(members_list)):
        print(f'{members_list[i]} is on {chore_assignment[i]}')
