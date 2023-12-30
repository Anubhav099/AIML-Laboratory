import csv

with open('D:\\GitHUB\\AIML-Laboratory\\P3 - CE\\enjoy_sport.csv') as f:
    data = list(csv.reader(f))
    specific = data[1][:-1]
    general = []
    for ind in range(len(specific)):
        general.append([])
        for _ in range(len(specific)):
            general[ind].append('?')

    for row in data:
        if row[-1] in ("1", "Yes"):
            for ind in range(len(specific)):
                if row[ind] != specific[ind]:
                    specific[ind] = "?"
                    general[ind][ind] = "?"

        elif row[-1] in ("0", "No"):
            for ind in range(len(specific)):
                if row[ind] != specific[ind]:
                    general[ind][ind] = specific[ind]
                else:
                    general[ind][ind] = "?"

        print("\nStep " + str(data.index(row) + 1) + " of Candidate Elimination Algorithm: ")
        print(specific)
        print(general)

    gh = [] # gh = general Hypothesis
    for hypo in general:
        for att in hypo:
            if att != '?':
                gh.append(hypo)
                break
    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", gh)