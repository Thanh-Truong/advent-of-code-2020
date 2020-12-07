def toColors(rule):
    tokens = rule.replace('.', '').replace('bags', '').replace(
        'bag', '').replace('contain', ',').split(',')
    colorsAndSpace = list(map(lambda item: ''.join(filter(lambda c: not c.isdigit(), item)), tokens))
    colors = list(map(lambda x: x.strip(), colorsAndSpace))
    return colors

if __name__ == "__main__":
    #rule = "pale cyan bags contain 2 posh black bags, 4 wavy gold bags, 2 vibrant brown bags."
    with open('input.txt', 'r') as f:
        for rule in f.read().splitlines():
            print(toColors(rule))
        
    