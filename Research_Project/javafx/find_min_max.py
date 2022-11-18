import numpy as np

file = input("File to read: ");

f = open(file)

x = []
y = []

for line in f:
  #print(line)
  if " x: " in line:
    x.append(float(line.split("x: ")[1]))
  if " y: " in line:
    y.append(float(line.split("y: ")[1]))


xx = np.array(x);
yy = np.array(y);

print("Minimum x: " + str(np.amin(xx)))
print("Maximum x: " + str(np.amax(xx)))
print("Minimum y: " + str(np.amin(yy)))
print("Maximum y: " + str(np.amax(yy)))
