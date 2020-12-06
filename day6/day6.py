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

def countQuestionsAnyOneAnswerYes_2(group):
    answers = [0] * 26
    for person in group:
        for c in person:
            answers[ord(c) - ord('a')] = 1 # there was an answer
    return  sum(answers)

def countQuestionsEveryOneAnswerYes_2(group):
    answers = [0] * 26
    size = len(group)
    for person in group:
        for c in person:
            pos = ord(c) - ord('a')
            answers[pos] = answers[pos] +  1 # this person answered
    return  sum([1 for i in answers if i == size])

if __name__ == "__main__":
    print(sum(map(lambda group: countQuestionsAnyOneAnswerYes_2(group), groups())))
    print(sum(map(lambda group: countQuestionsEveryOneAnswerYes_2(group), groups())))
    