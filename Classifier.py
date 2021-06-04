from statistics import *
from math import sqrt

debug = True

class Classifier():

    def __init__(self):
        self.data = []

    def Train(self, file):
        with open(file, "r") as file1:
            for line in file1.readlines():
                self.data.append([float(i) for i in line.split(' ') if i.strip()])
        
        # if debug:
        #     print("------------------ NOT NORMALIZED")
        #     for i in self.data:
        #         for j in i:
        #             print(str(j), end='     ')
        #         print('\n')

        # next we normalize
        avg = []
        std = []

        for j in range(len(self.data[0])):
            col = []
            for i in range(len(self.data)):
                col.append(self.data[i][j])
            avg.append(mean(col))
            std.append(stdev(col))

        for i in range(len(self.data)):

            for j in range(1, len(self.data[i])):
                self.data[i][j] -= avg[j]
                self.data[i][j] /= std[j]

        if debug:
            # print("------------------ NORMALIZED")
            with open("norm.txt", "w") as f:
                for i in self.data:
                    for j in i:
                        # print(str(j), end='     ')
                        f.write(str(j) + ',')
                    # print('\n')
                    f.write('\n')

    def Test(self, instance):
        trainData = []
        inst = []
        for i in instance:
            inst.append(i)
        for i in self.data:
            tmp = []
            if not i == inst:
                for j in i:
                    tmp.append(j)
                trainData.append(tmp)
                #print(str(tmp))
        #normalize your data for some reason ?
        # avg = mean(inst)
        # std = pstdev(inst)
        # for i in range(1, len(inst)):
        #     inst[i] -= avg
        #     inst[i] /= std

        min = 10000000
        classif = None
        for i in range(len(trainData)):
            dist = 0
            for j in range(1, len(trainData[i])):
                dist += pow(trainData[i][j] - inst[j], 2)
            if sqrt(dist) < min and not dist == 0:
                min = sqrt(dist)
                classif = trainData[i][0]
        
        return classif

    def getData(self):
        return self.data

    def getInstance(self, i):
        return self.data[i]

    def setData(self, data):
        self.data = data