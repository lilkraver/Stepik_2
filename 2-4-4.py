lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))
    
    
    
    with open('dataset.txt') as f, open('dataset_copy.txt', 'w') as w:
    for i in f.readlines()[::-1]:
        w.write(i)
