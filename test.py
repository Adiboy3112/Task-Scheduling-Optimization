data = [['ABC', 12, 3, 100],
        ['DEF', 10, 5, 200],
        ['GHI', 13, 3, 1000]]

data.sort(key=lambda row: (row[2], row[3]), reverse=True)

print(data)