import pprint
def toColors(rule):
    tokens = rule.replace('.', '').replace('bags', '').replace(
        'bag', '').replace('no other', '').replace('contain', ',').split(',')
    colorsAndSpace = list(map(lambda item: ''.join(filter(lambda c: not c.isdigit(), item)), tokens))
    colors = list(map(lambda x: x.strip(), colorsAndSpace))
    return colors

def findShinyGold(v, directions):
    if 'shiny gold' in v:
        return True
    else:
        # some in v may led to shiny gold
        for some in v:
            vv = directions.get(some)
            if vv and 'shiny gold' in vv:
                return True

if __name__ == "__main__":
    #rule = "faded blue bags contain no other bags"
    #print(toColors(rule))
    directions = {}
    with open('input.txt', 'r') as f:
        for rule in f.read().splitlines():
            colors = toColors(rule)
            directions[colors[0]] = colors[1:]
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(directions)
    count = 0
    for k , v in directions.items():
        if findShinyGold(v, directions):
            count = count + 1
    print(count)