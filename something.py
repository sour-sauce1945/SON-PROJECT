import math as mt
from matplotlib import pyplot as plt
plt.style.use("bmh")

ans = input("Choose base or acid as a titrant or add make a acid/base mixture ")
if ans.lower() in ["base", "b"]:
    volume1 = float(input("Enter volume of acid taken: "))
    conc1 = float(input("Enter concentration of acid taken: "))
    milimoles1 = volume1 * conc1

    volume_list = []
    pH_list = []

    while True:
        volume2 = float(input("Enter volume of base taken: "))
        conc2 = float(input("Enter concentration of base taken: "))
        milimoles2 = volume2 * conc2

        if milimoles2 < milimoles1:
            H = (milimoles1 - milimoles2) / (volume1 + volume2)
            pH = -(mt.log10(H))
            print("Titration is before the equivalence point. The pH is ", round(pH, 2))
        elif milimoles1 == milimoles2:
            print("The titration has reached the equivalence point. The pH is 7")
        else:
            OH = (milimoles2 - milimoles1) / (volume1 + volume2)
            pOH = -(mt.log10(OH))
            pH = 14 - pOH
            print("Titration is after the equivalence point. The pH is ", round(pH, 2))

        volume_list.append(volume2)  # Append the volume value to the list
        pH_list.append(pH)  # Append the pH value to the list

        A = input("Do you want to continue adding more base? (Yes/No): ")
        if A.lower() in ["no", "n"]:
            break

    plt.plot(volume_list, pH_list, marker='o')
    plt.xlabel("Volume of Base")
    plt.ylabel("pH")
    plt.title("Gradual pH Change")
    plt.grid(True)
    plt.show()

elif ans.lower() in ["acid", "a"]:
    volume1 = float(input("Enter volume of base taken: "))
    conc1 = float(input("Enter concentration of base taken: "))
    milimoles1 = volume1 * conc1

    volume_list = []  # List to store the volume values
    pH_list = []  # List to store the pH values

    while True:
        volume2 = float(input("Enter volume of acid taken: "))
        conc2 = float(input("Enter concentration of acid taken: "))
        milimoles2 = volume2 * conc2

        if milimoles2 < milimoles1:
            OH = (milimoles1 - milimoles2) / (volume1 + volume2)
            pOH = -(mt.log10(OH))
            pH = 14 - pOH
            print("The titration is before the equivalence point. The pH is ", round(pH, 2))
        elif milimoles1 == milimoles2:
            print("Titration has reached the equivalence point. The pH is 7")
        else:
            pH = (milimoles2 - milimoles1) / (volume1 + volume2)
            pH = -(mt.log10(pH))
            print("Titration is after the equivalence point. The pH is ", round(pH, 2))

        volume_list.append(volume2)  # Append the volume value to the list
        pH_list.append(pH)  # Append the pH value to the list

        A = input("Do you want to continue adding more base? (Yes/No): ")
        if A.lower() in ["no", "n"]:
            break

    plt.plot(volume_list, pH_list, marker='o')
    plt.xlabel("Volume of Acid")
    plt.ylabel("pH")
    plt.title("Gradual pH Change")
    plt.grid(True)
    plt.show()

elif ans.lower() in ["amix" ,"am" , "acid mixture"] :
    volume1 = float(input("Enter volume of Acid 1 taken: "))
    conc1 = float(input("Enter concentration of Acid 1 taken: "))
    milimoles1 = volume1 * conc1

    volume2 = float(input("Enter volume of acid 2 taken: "))
    conc2 = float(input("Enter concentration of acid 2 taken: "))
    milimoles2 = volume2 * conc2

    H= (milimoles1 + milimoles2)/ volume1 + volume2
    pH= -(mt.log10(H))
    print("The pH of this acid mixture is " , pH)

elif ans.lower() in ["bmix" , "bm" , "base mixture"] :
    volume1 = float(input("Enter volume of base 1 taken: "))
    conc1 = float(input("Enter concentration of base 1 taken: "))
    milimoles1 = volume1 * conc1

    volume2 = float(input("Enter volume of base 2 taken: "))
    conc2 = float(input("Enter concentration of base 2 taken: "))
    milimoles2 = volume2 * conc2

    OH1 = (milimoles1 + milimoles2) / volume1 + volume2
    OH2 = -(mt.log10(OH1))
    pH = 14 - OH2
    print("The pH of the base mixture is ",pH)

