if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        counts = []
        dic = {}
        for line in lines:
            if line == "":
                counts.append(sum(1 for i in dic.keys()))
                dic = {}
            else:
                for c in line:
                    dic[c] = 'None'
        counts.append(sum(1 for i in dic.keys()))
        #print(counts)
        print(sum(counts))