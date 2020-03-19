
from vectorTasks import list2vec
rowlist = [
    list2vec([0, 2, 3, 4, 5]),
    list2vec([0, 0, 0, 3, 2]),
    list2vec([1, 2, 3, 4, 5]),
    list2vec([0, 0, 0, 6, 7]),
    list2vec([0, 0, 0, 9, 9])
]
col_label_list = sorted(rowlist[0].D, key=hash)
new_rowlist = []
rows_left = set(range(len(rowlist)))

for c in col_label_list:
    rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
    if rows_with_nonzero != []: 
        pivot = rows_with_nonzero[0]
        rows_left.remove(pivot)
        new_rowlist.append(rowlist[pivot])
        for r in rows_with_nonzero[1:]:
            multiplier = rowlist[r][c]/rowlist[pivot][c] 
            rowlist[r] = rowlist[r] - multiplier*rowlist[pivot]

[print(vec) for vec in new_rowlist]