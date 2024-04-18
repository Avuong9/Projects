#Dannis Ngo
#1291654
#credit card verification 

def isValidNumber (cardNumber):
    '''passes card num to 'sumOfOddPlaces()' and 'sumOfDoubleEvenNum()', sums the return values, determines valid or not valid '''
    #check if length is 13-16 else return false
    if len(cardNumber) >12 and len(cardNumber) < 17 :
    #checks if num starts with 4, 5,or 6, or 37 if so call sumofodd and sumofdoubleeven. returns false or true
        if cardNumber[0] == '4' or cardNumber[0] == '5' or cardNumber[0] == '6': 
            sumOfOdd = sumOfOddPlaces(cardNumber)
            sumOfDoubleEven = sumOfDoubleEvenNum(cardNumber)
            sumOfBoth = (sumOfDoubleEven + sumOfOdd) % 10
            if sumOfBoth != 0:
                return False
            elif sumOfBoth == 0:
                return True
        elif cardNumber[0] == '3' or cardNumber[1] == '7':
            sumOfOdd = sumOfOddPlaces(cardNumber)
            sumOfDoubleEven = sumOfDoubleEvenNum(cardNumber)
            sumOfBoth = (sumOfDoubleEven + sumOfOdd) % 10
            if sumOfBoth != 0:
                return False
            elif sumOfBoth == 0:
                return True
    else:
        return False


def sumOfOddPlaces(cardNumber):
    '''makes a list of the odd numbers and sums them, returns sum of odd nums'''
    #reverses nums
    reverseNums = cardNumber [::-1]
    oddReverseNums = []
    index = 0
    #looks at number in reverseNums if it is odd index it appends to the next list, sums oddreverseNums and returns it
    for number in reverseNums: 
        if index % 2 == 0:
            oddReverseNums.append(int(number))
        index = index + 1
    sumOfOdd = sum(oddReverseNums)
    return sumOfOdd
    
    
def sumOfDoubleEvenNum(cardNumber):
    '''gives string to getDigits, gets usable digits, adds them, returns sum.'''
    digits = getDigits(cardNumber)
    sumOfEven = sum(digits)
    return sumOfEven

def getDigits(number):
    '''makes a new list for the string of nums then multiplies by two, if 10 or higher it subs 9 and returns, elif it returns the num to double even num'''
    numberList =[]
    numX2 = []
    for digit in number:
        numberList.append(int(digit))
    reverseNums = numberList[::-1]
    index = 0
    for digit in reverseNums:
        if index % 2 != 0 : 
            if digit *2 > 9: 
                numX2.append((digit * 2 )-9)
            elif digit * 2 <= 9:
                numX2.append(digit*2)
        index = index + 1

    return numX2


def main():
    '''gets num of how many times the user wants to check card,runs that num of times. calls isValidNumber, gets bool valid or not, print is valid, or is not'''
    checkNum = int(input('How many credit card numbers do you want to check? '))
    for i in range (checkNum):
        cardNumber = input("Enter a credit card number: ")
        trueOrFalse = isValidNumber(cardNumber)
        if trueOrFalse == True:
            print(cardNumber,' is valid')
        else:
            print(cardNumber,'is invalid')

if __name__=="__main__":
    main()

#test1
# How many credit card numbers do you want to check? 2
# Enter a credit card number: 4388576018402626
# 4388576018402626 is invalid
# Enter a credit card number: 4388576018410707
# 4388576018410707  is valid
#test2
#How many credit card numbers do you want to check? 0
#test 3
# How many credit card numbers do you want to check? 3      
# Enter a credit card number: 12345678
# 12345678 is invalid
# Enter a credit card number: 5169769005222217
# 5169769005222217  is valid
# Enter a credit card number: 6011655276746808
# 6011655276746808 is invalid
# test 4
# How many credit card numbers do you want to check? 4
# Enter a credit card number: 37200545150503
# 37200545150503  is valid
# Enter a credit card number: 372005451505039
# 372005451505039 is invalid
# Enter a credit card number: 507050545451503
# 507050545451503 is invalid
# Enter a credit card number: 50705054545150 
# 50705054545150  is valid
# test5
# How many credit card numbers do you want to check? 2
# Enter a credit card number: 602551564430201
# 602551564430201 is invalid
# Enter a credit card number: 60251564430201  
# 60251564430201  is valid