# Meta Production Engineer Tech Interview Coding Test Question (6/2022)
# prob5 - Create 2 dict. one for leg length and other for stride length. Look up these values to calculate speed. Note that while storing stride length, speed can be calculated and added to result list. I have separated it for readability
import math

dino_stride_length = {}
dino_leg_length = {}
dino_type = {}

with open("dataset1.csv","r") as data1:
    # data1.readline()
    for line in data1:
        dino_leg_length[line.split(",")[0].strip()]=line.split(",")[1].strip()

with open("dataset2.csv", "r") as data2:
    # data2.readline()
    for line in data2:
        dino_stride_length[line.split(",")[0].strip()]=line.split(",")[1].strip()
        dino_type[line.split(",")[0].strip()] = line.split(",")[2].strip()


def get_speed(dino):
    stride_length = float(dino_stride_length[dino])
    leg_length = float(dino_leg_length[dino])
    speed = (((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8))
    return speed

print(dino_stride_length)
print(dino_leg_length)
result = []
for x in dino_type.keys():
    print("dino_type = " + str(x))
    if dino_type[x] == 'bipedal':
        result.append([x, get_speed(x)])

print("Dino speed from fastest to slowest - ")
for x in sorted(result, key=lambda x:x[1], reverse=True):
    print(x[0] + " " + str(x[1]))
