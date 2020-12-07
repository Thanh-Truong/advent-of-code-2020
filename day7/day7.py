import pprint
def buildBags():
    bags = {}
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            cleanedLine = line.replace('.', '').replace('bags', '').replace('bag','').replace('contain',',')
            parts = cleanedLine.split(',')
            outerBag = parts[0].strip()
            otherBags = parts[1:]
            bags[outerBag] = []
            for i in otherBags:
               elements = i.strip().split(" ")
               if elements[0] != "no":
                   quantity = elements[0]
                   bag = " ".join(elements[1:])
                   bags[outerBag].append((quantity, bag))
    return bags

def containGold(outerBag, bags):
    innerBags = bags[outerBag]
    directlyFound = any(filter(lambda info: info[1] == 'shiny gold', innerBags))
    if directlyFound:
        return True
    else:
        return any(map(lambda bag: containGold(bag[1], bags), innerBags))
if __name__ == "__main__":
    #rule = "light red bags contain 3 wavy teal bags, 3 plaid aqua bags, 4 drab lavender bags, 2 bright coral bags."
    bags = buildBags()
    count = 0
    for outerBag in bags.keys():
        if containGold(outerBag, bags):
            count = count + 1
    pprint.pprint(count)