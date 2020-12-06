def groups():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        group = []
        for line in lines:
            if line == "":
                yield group
                group.clear()
            else:
                group.append(line)
        if len(group) > 0:
            yield group

def countQuestionsAnyOneAnswerYes(group):
    d = {}
    for person in group:
        for c in person:
            d[c] = 'None'
    return  sum([1 for i in d.keys()])

def countQuestionsEveryOneAnswerYes(group):
    firstPerson = group[0]
    count = 0
    for question in firstPerson:
        # question was answered by all others ?
        s = sum(map(lambda other: 1 if question in other else 0, group[1:]))
        if s == len(group) - 1: # every other
            count = count +  1
    return  count

if __name__ == "__main__":
    print(sum(map(lambda group: countQuestionsAnyOneAnswerYes(group), groups())))
    print(sum(map(lambda group: countQuestionsEveryOneAnswerYes(group), groups())))
        
