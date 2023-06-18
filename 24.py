f = open('24_demo.txt').readline()
f = f.replace('Z', ' ').replace('Y', ' ').split()
print(len(max(f)))
