from initValues import initvalues

def xdominatey(index1, index2):
    atleastone = 0
    minlimit = 0

    for x in range(len(sigmas)):
        if sigmas[index1][x] > sigmas[index2][x]:
            minlimit += 1 

        if sigmas[index1][x] < sigmas[index2][x]:
            atleastone += 1

    if minlimit == 0 and atleastone > 0:
        return True
    else:
        return False

def preferenceIdentifier(sigma_x, sigma_y, xdominatey):
    result = 0

    if xdominatey or ((sigma_x >= values.Lamdba) and (sigma_y < 0.5)) or ((sigma_x >= values.Lamdba) and ((0.5 <= sigma_y) and (sigma_y < values.Lamdba)) and (sigma_x - sigma_y >= values.Beta)):
        result = 1
        xPy = True
    else:
        xPy = False

    if (sigma_x >= values.Lamdba) and (sigma_y >= values.Lamdba) and (abs(sigma_x - sigma_y) <= values.Epsilon):
        result = 2
        xIy = True
    else:
        xIy = False

    if (sigma_x >= values.Lamdba) and (sigma_x >= sigma_y) and not(xPy) and not(xIy):
        result = 3

    if (sigma_x < 0.5) and (sigma_y < 0.5):
        result = 4

    if ((0.5 <= sigma_x) and (sigma_x <= values.Lamdba)) and (sigma_y < 0.5) and ((sigma_x - sigma_y) > (values.Beta / 2)):
        result = 5

    return result

run = 1

values = initvalues(run)

values.printValues()

archivo = open("../../output/Globalwithoutduplicates.txt", "r")

sigmas = []

number_of_iteration = 1

for line in archivo:
    print(f"Start: {number_of_iteration} ")
    weights = line.split()
    sigma = []

    archivo2 = open("../../output/Globalwithoutduplicates.txt", "r")

    for line2 in archivo2:
        weights2 = line2.split()

        concordanse = 0

        for index in range(0,len(weights)):

            xIky = abs(float(weights[index]) - float(weights2[index])) <= values.vectorU[index]

            xPky = float(weights[index]) < float(weights2[index]) and not(xIky)

            if xPky or xIky:
                concordanse += values.vectorW[index]

        discordance_min_value = 1

        for index in range(0,len(weights)):
            discordanse = 0

            dis = float(weights[index]) - float(weights2[index])

            if dis < values.vectorS[index]:
                discordanse = 0

            if (values.vectorS[index] <= dis) and (dis < values.vectorV[index]):
                discordanse = (dis - values.vectorU[index]) / (values.vectorV[index] - values.vectorU[index])

            if dis >= values.vectorV[index]:
                discordanse = 1

            if (1 - discordanse) < discordance_min_value:
                discordance_min_value = 1 - discordanse
            
        sigma_value = concordanse * discordance_min_value

        sigma.append(sigma_value)
    sigmas.append(sigma)
    print(f"End: {number_of_iteration}")
    number_of_iteration += 1

netscore_array = []

for x in range(len(sigmas)):
    netscore = 0
    for y in range(len(sigmas[x])):
        netscore += (sigmas[x][y] - sigmas[y][x])
    netscore_array.append(netscore)

frontierArray = []
preferencesArray = []

for x in range(len(sigmas)):
    frontier1 = 0
    frontier2 = 0
    frontier3 = 0
    fronts = []
    for y in range(len(sigmas[x])):
        if x != y:
            preference = preferenceIdentifier(sigmas[x][y], sigmas[y][x], xdominatey(x, y))

            # // Estrictamente dominada
            if preference == 1:
                frontier1 += 1

            # // Debilmente dominadas / k-preferencia
            if preference == 3 or preference == 5:
                frontier2 += 1

            # //Flujo neto
            if netscore_array[y] > netscore_array[x]:
                frontier3 += 1
            
        else:
            preference = 0

    fronts.append(frontier1)
    fronts.append(frontier2)
    fronts.append(frontier3)
    frontierArray.append(fronts)
    preferencesArray.append(preference)

output_file = open(f"results{run}.txt", "w")

for x in range(len(frontierArray)):
    for y in range(len(frontierArray[x])):
        output_file.write(f"{str(frontierArray[x][y])} ")
    output_file.write("\n")
output_file.close()

    

