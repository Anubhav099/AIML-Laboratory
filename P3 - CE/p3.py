import csv

with open('D:\\GitHUB\\AIML-Laboratory\\P3 - CE\\enjoy_sport.csv') as f:
    data = list(csv.reader(f))
    specific = data[1][:-1]
    print("specific",specific)
    general = []
    n = len(specific)

    for ind in range(n):
        general.append([])
        for _ in range(n):
            general[ind].append('?')

    print("general", general)
    index = 1
    for row in data[1:]:
        print("\nrow",index, row)
        if row[-1] in ("1", "Yes"):
            for ind in range(n):
                if row[ind] != specific[ind]:
                    specific[ind] = "?"
                    general[ind][ind] = "?"
        elif row[-1] in ("0", "No"):
            for ind in range(n):
                if row[ind] == specific[ind]:
                    general[ind][ind] = "?"
                else:
                    general[ind][ind] = specific[ind]

        print("\nStep " + str(index) + " of Candidate Elimination Algorithm: ")
        print(specific)
        print(general)
        index += 1

    gh = [] # gh = general Hypothesis
    for hypo in general:
        for att in hypo:
            if att != '?':
                gh.append(hypo)
                break
    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", gh)