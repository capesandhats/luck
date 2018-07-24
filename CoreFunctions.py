import sys
import random
import time

class Combination:
    abc = 0
    # number1 = -1
    # number2 = -1
    # number3 = -1
    # number4 = -1
    # number5 = -1
    # number6 = -1

    def __init__(self, number1, number2, number3, number4, number5, number6):
        assert (number1 >= 1) & (number1 <= 50)
        assert (number2 >= 1) & (number2 <= 50)
        assert (number3 >= 1) & (number3 <= 50)
        assert (number4 >= 1) & (number4 <= 50)
        assert (number5 >= 1) & (number5 <= 50)
        assert (number6 >= 1) & (number6 <= 50)

        templist =[number1,number2,number3,number4,number5,number6]
        templist.sort()
        self.number1=int (templist[0])
        self.number2=int (templist[1])
        self.number3=int (templist[2])
        self.number4=int (templist[3])
        self.number5=int (templist[4])
        self.number6=int (templist[5])
        self.list=templist

    def __eq__(self, other):
        if isinstance(other,Combination):
            val = ((self.number1 == other.number1) & (self.number2 == other.number2) & (self.number3 == other.number3 ) & (self.number4 == other.number4)
                    & (self.number5 == other.number5) & (self.number6 == other.number6))
            return val
        return False

comb1 = Combination(20,6,4,5,35,9)
# comb2 = Combination(20,6,4,5,35,10)
# comb3 = Combination(20,6,4,9,35,8)
#
# comb4 = Combination(20,6,4,9,35,5)
#
# comb5 = Combination(20,6,4,9,35,1)
# combiList = [comb1,comb2,comb3]
#
# print (combiList.__contains__(comb4))
# print (combiList.__contains__(comb5))




# print(combiList5aus10.count())
# listOfCombinations=[[2,6,4,5,3,8],[1,4,3,2,5,6],[2,6,4,5,3,7]]
# print(listOfCombinations)
# # for var in listOfCombinations:
# #     print(var)
# #
# #     var=var.sort()
#
#
# def valueExists(mainLIST,listTOCheck):
#     # mainLIST =listOfCombinations
#     listTOCheck=listTOCheck.sort()
#     for var in mainLIST:
#
#         if var.__contains__(listTOCheck):
#             print("yes")
#             return True
#         else:
#             print("no")
#             return False
#
#
# # print(valueExists(listOfCombinations,[3,4,5,6,7,8]))
# # print(valueExists(listOfCombinations,[1,4,3,2,5,6]))
# print(listOfCombinations)
#
# sorted(listOfCombinations)




