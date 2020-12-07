def groups():
    with open('input.txt', 'r') as f:
        group = []
        for line in f.read().splitlines():
            if line == "":
                yield group
                group.clear()
            else:
                group.append(line)
        yield group

def countNumberAnswers(group):
    answers = [0] * 26
    for person in group:
        for c in person:
            i = ord(c) - ord('a')
            answers[i] = answers[i] +  1 # one more 'person' answered c
    return answers

def countQuestionsAnyOneAnswerYes(group):
    answers = countNumberAnswers(group)
    return sum([1 for i in answers if i > 0]) # anyone answered so i > 0

def countQuestionsEveryOneAnswerYes(group):
    answers = countNumberAnswers(group)
    return  sum([1 for i in answers if i == len(group)]) # everyone answered so i == len(group)

if __name__ == "__main__":
    print(sum(map(lambda group: countQuestionsAnyOneAnswerYes(group), groups())))
    print(sum(map(lambda group: countQuestionsEveryOneAnswerYes(group), groups())))
    