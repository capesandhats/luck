import CoreFunctions
import time



def generateCombinationList(combiList):

    num1, num2, num3, num4, num5, num6, combi_count = 1, 1, 1, 1, 1, 1, 0
    time_init = time.clock()
    time_print_trigger = 0
    print_interval =30
    countlimit = 50

    while (num1 < countlimit):
        num2=1+num1
        while (num2 < countlimit):
            num3=1+num2
            while (num3 < countlimit):
                num4=1+num3
                while (num4 < countlimit):
                    num5=1+num4
                    while (num5 < countlimit):
                        num6=1+num5
                        while (num6 < countlimit):
                            # print("")
                            tempList = [num1, num2, num3, num4, num5, num6]
                            if(len(tempList)==len(set(tempList))):
                                temp_combi = CoreFunctions.Combination(num1,num2,num3,num4,num5,num6)
                                # if not(combiList.__contains__(temp_combi)):
                                if (1):
                                    combiList.append(temp_combi)
                                    combi_count = combi_count  + 1
                                    if((time.clock()- time_init) > (time_print_trigger*print_interval)):
                                        print(" %d,%d,%d,%d,%d,%d count: %d " %(temp_combi.number1,temp_combi.number2,temp_combi.number3,temp_combi.number4,temp_combi.number5,temp_combi.number6,combi_count) )
                                        print(((time.clock()-time_init),(time_print_trigger*print_interval)))
                                        time_print_trigger= time_print_trigger+1

                                    # print(combi_count)
                            num6 = num6 + 1
                        num5 = num5 + 1
                    num4 = num4 + 1
                num3 = num3 + 1
            num2 = num2 + 1
        num1 = num1 + 1

    print("Number of combinations: ", combi_count)

def expectedCombinations(num, combi):
    counter = combi
    numerator = 1
    denominator=1
    while (counter>0):
        numerator= numerator*(num-counter+1)
        denominator = counter*denominator
        counter=counter-1

    print("Expected combinations :", numerator, denominator, numerator/denominator)


    combinations = num*(num-1)*(num-2)*(num-4)

expectedCombinations(49,6)
#expectedCombinations(7,6)
#expectedCombinations(20,6)

# comb1 = CoreFunctions.Combination(20,6,4,5,35,9)

combiList5aus10=[]
generateCombinationList(combiList5aus10)
#
print(len(combiList5aus10))