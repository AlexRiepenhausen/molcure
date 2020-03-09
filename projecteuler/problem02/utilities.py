# helper function to convert integer number to string representation
def integer2String(integernumber):
    return str(integernumber).zfill(3)


# make sure that the number (sequence of three integers) can be divided by the sequence
def divisibleBy(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False


# check for duplicate number in sequence (numbers like 1 are represented as "001")
def containsDuplicateNumbers(integernumber):
    numberstr = str(integernumber).zfill(3)
    strset    = set(numberstr)
    if len(strset) < 3:
        return True
    else:
        return False


# convert array to single string
def arr2string(arr):
    return ''.join(arr)


# convert number to array of integers
def number2intArr(number):
    numberstr = str(number).zfill(3)
    strset    = list(numberstr)
    return list(map(int, strset))


# convert a string representation of an integer to an array of integers
def string2intArray(stringnumber):
    intarr = list()
    for character in stringnumber:
        intarr.append(int(character))
    return intarr


# convert a string representation of an integer to an array of integers
def intArray2String(intarr):
    sequence_string = ""
    for integer in intarr:
        sequence_string += str(integer)
    return sequence_string


# provides a list of prime numbers given a specific range
def getPrimeNumbers(start, end):
    primenumbers = list()
    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                primenumbers.append(number)
    return primenumbers
