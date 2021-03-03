class initvalues:
    Epsilon = 0
    Beta = 0
    Lamdba = 0
    vectorW = []
    vectorV = []
    vectorU = []
    vectorS = []

    def __init__(self, file):
        archivo = open(f"../../output/DM{file}_config.txt", "r")
        cont = 0

        for line in archivo:
            values = line.split()

            for index in range(len(values)):
                if cont == 0:
                    self.Epsilon = float(values[index])
                
                if cont == 1:
                    self.Beta = float(values[index])
                
                if cont == 2:
                    self.Lamdba = float(values[index])
                
                if cont == 3:
                    self.vectorW.append(float(values[index]))
                
                if cont == 4:
                    self.vectorV.append(float(values[index]))
                
                if cont == 5:
                    self.vectorU.append(float(values[index]))
                
                if cont == 6:
                    self.vectorS.append(float(values[index]))
                
            cont += 1
        archivo.close()

    def printValues(self):
        print(self.Epsilon)
        print(self.Beta)
        print(self.Lamdba)
        print(self.vectorW)
        print(self.vectorV)
        print(self.vectorU)
        print(self.vectorS)



