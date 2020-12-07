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
                   bags[outerBag].append((int(quantity), bag))
    return bags

def containGold(outerBag, bags):
    innerBags = bags[outerBag]
    # directly or indirectly
    return any(filter(lambda info: info[1] == 'shiny gold', innerBags)) or any(
        map(lambda bag: containGold(bag[1], bags), innerBags))

def countContainedBags(outerBag, bags):
    innerBags = bags[outerBag]
    return sum(map(
        lambda bagInfo: bagInfo[0] + bagInfo[0] * countContainedBags(
            bagInfo[1], bags), innerBags))

if __name__ == "__main__":
    bags = buildBags()
    count = 0
    for outerBag in bags.keys():
        # PartOne
        if containGold(outerBag, bags):
            count = count + 1
    # PartTwo
    aa = countContainedBags('shiny gold', bags)
    
    print("PartOne : {}".format(count))
    print("PartTwo : {}".format(aa))