import copy
import utilities as ut

# Problem 41
class SubstringDivisibility():

    def __init__(self, start, end):
        self.numbers      = list(range(0, 10))
        self.primenumbers = ut.getPrimeNumbers(start, end)
        self.candidates   = self.__initialiseCandidates(2)


    # function that kickstarts the process of generating all pandigital sequences with the requried properties
    def generateAllPossiblePandigitalSequences(self):
        for prime in self.primenumbers:
            if prime > 2: # 2 has already been used in the initialisation process
                self.__growCandidates(prime)
        self.candidates = self.appendFirstNumberToCandidates()


    # get the sum of all pandigital number
    def displaySumOfAllSequences(self):
        finalsum = 0
        for candidate in self.candidates:
            finalsum += int(candidate)
        print("The sum of all sequences is {}".format(finalsum))



    # append the first number to the remaining candidate sequences
    def appendFirstNumberToCandidates(self):
        new_sequences = list()
        for candidate in self.candidates:
            old_sequence  = ut.string2intArray(candidate)
            # iterates from 0 to 9 and checks if number can be added at the start of the sequence
            for number in range(0, 10):
                if number not in old_sequence:
                    new_candidate = ut.intArray2String([number] + old_sequence)
                    new_sequences.append(new_candidate)
        return new_sequences


    # iterate over the candidates, grow the integer sequence and discard those numbers that are not eligible
    def __growCandidates(self, current_divisor):
        tempcandidates = copy.deepcopy(self.candidates)
        for candidate in tempcandidates:
            new_sequences      = self.__newSequencesFromOldSequence(candidate)
            eligible_sequences = self.__getEligibleSequences(new_sequences, current_divisor)
            self.candidates.remove(candidate)
            self.__addNewSequences2candidates(eligible_sequences)



    # add the new sequences to the set of candidates
    def __addNewSequences2candidates(self, eligible_sequences):
        for sequence in eligible_sequences:
            self.candidates.add(sequence)



    # Takes the newly estended sequences and checks if they satisfy the given conditions
    # The ones that do are returned as an array
    def __getEligibleSequences(self, new_sequences, current_divisor):
        eligible_sequences = list()
        for sequence in new_sequences:
            sequence_tail = int(sequence[-3:]) # last 3 digits in sequence
            if ut.divisibleBy(sequence_tail, current_divisor):
                eligible_sequences.append(sequence)
        return eligible_sequences



    # take an existing sequence, e.g. "123" and return all possible new sequences,
    # for example "1234", "1230" etc. where the newly added number is not 1,2 or 3
    def __newSequencesFromOldSequence(self, candidate):
        # takes the candidate string and converts it to an integer array
        old_sequence  = ut.string2intArray(candidate)
        new_sequences = set()
        # iterates from 0 to 9 and checks if number can be added at the end of the sequence
        for number in range(0, 10):
            if number not in old_sequence:
                new_candidate = ut.intArray2String(old_sequence + [number])
                new_sequences.add(new_candidate)
        return new_sequences



    # generate sequence of three numbers
    def __initialiseCandidates(self, divisor):
        candidates = set()
        for i in range (0, 999):
            if not ut.containsDuplicateNumbers(i):
                if ut.divisibleBy(i, divisor):
                    candidate = ut.integer2String(i)
                    candidates.add(candidate)
        return candidates


if __name__ == '__main__':

    sd = SubstringDivisibility(0, 17)
    sd.generateAllPossiblePandigitalSequences()
    sd.displaySumOfAllSequences()



