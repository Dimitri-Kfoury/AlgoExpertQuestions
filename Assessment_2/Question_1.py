def degreesOfSeparation(friendsLists, personOne, personTwo):
    friends_1 = degrees_of_separation_helper(personOne, friendsLists)

    friends_2 = degrees_of_separation_helper(personTwo, friendsLists)

    if friends_1 == friends_2:
        return ''
    elif friends_1 > friends_2:
        return personTwo
    else:
        return personOne


def degrees_of_separation_helper(person, friends_list):
    queue = []
    num = 0
    visited = {}
    added = {}
    queue.append([person,0])
    added[person] = True
    while len(queue) > 0:
        next_connection = queue.pop(0)
        visited[next_connection[0]] = next_connection[1]
        degree = next_connection[1]
        for friend in friends_list[next_connection[0]]:
            if friend not in visited.keys() and friend not in added:
                queue.append([friend, degree + 1])
                added[friend] = True

    for person in visited:
        if visited[person] > 6:
            num+=1
    for person in friends_list:
        if person not in visited.keys():
            num += 1

    return num


friends_list = {
    "Aaron": ["Eric", "Molly"],
    "Aditya": ["Akshay"],
    "Akshay": ["Aditya", "Ryan"],
    "Alex": ["Saurabh"],
    "Amanda": ["Sam", "Beyonce", "Changpeng"],
    "Antoine": ["Clement"],
    "Ayushi": ["Molly", "Jean"],
    "Beyonce": ["Amanda"],
    "Brandon": [],
    "Changpeng": ["Amanda", "Jon"],
    "Charlie": ["Steve", "Justin", "Ryan"],
    "Clement": ["Antoine", "Sandeep", "Simon"],
    "Eric": ["Aaron"],
    "Hannah": ["Tony"],
    "James": ["Shakira"],
    "Jean": ["Ayushi", "Kelly", "Shakira"],
    "Jon": ["Changpeng"],
    "Justin": ["Charlie", "Kelly", "Molly", "Penny"],
    "Kelly": ["Justin", "Kunal", "Jean"],
    "Kunal": ["Kelly", "Tony"],
    "Lee": ["Saurabh", "Mei"],
    "Lexi": ["Xi"],
    "Mei": ["Lee", "Penny", "Xi"],
    "Molly": ["Aaron", "Justin", "Shakira", "Ayushi", "Simon"],
    "Muhammad": [],
    "Nirali": [],
    "Pedro": ["Saurabh", "Steve"],
    "Penny": ["Justin", "Saurabh", "Mei"],
    "Ryan": ["Charlie", "Akshay"],
    "Sam": ["Amanda"],
    "Sandeep": ["Clement"],
    "Saurabh": ["Pedro", "Alex", "Lee", "Penny"],
    "Shakira": ["Jean", "James", "Molly", "Simon"],
    "Simon": ["Clement", "Molly", "Shakira", "Steve"],
    "Steve": ["Pedro", "Charlie", "Simon"],
    "Tony": ["Hannah", "Kunal"],
    "Xi": ["Lexi", "Mei"]
}
person_one = "Kunal"
person_two = "Charlie"
print(degreesOfSeparation(friends_list, person_one, person_two))
