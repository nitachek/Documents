import csv
rows = []
count = 0
if __name__ == '__main__':
    with open("1000-out2.csv") as df:
        reader = csv.reader(df)
        header = next(reader)
        for row in reader:
            rows.append(row)
    while (count <= 999):   
        count = count + 1
        def naive(pat, st):
            M = len(pat)
            N = len(st)
            for i in range(N - M + 1):
                j = 0
                while(j < M):
                    if (st[i + j] != pat[j]):
                        break
                    j += 1
                if (j == M): 
                    print("Virus found at index %d"%i, "of row %d"%count)
                    break
        for row in rows[:count]: 
            st = "".join(row)
        pat = "00110"
        naive(pat, st)