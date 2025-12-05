def filter_young(people):

    youngPeople = []

    # get young people
    for i,j in people.items():
        if (j[0] < 30):
            youngPeople.append(i)

    # sort them
    youngPeople.sort()

    # make a new list, but only with their name and phone number
    for i in range(0, len(youngPeople)):
        youngPeople[i] = youngPeople[i], people[youngPeople[i]][1]

    return youngPeople