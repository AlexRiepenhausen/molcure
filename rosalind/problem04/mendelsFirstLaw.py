import copy
from enum import Enum

# Create an Allele class where recessive is 0 and dominant is 1
# This is intended to enhance code legibility
class Allele(Enum):
    REC = 0
    DOM = 1


# This class provides the solution to the problem Mendel's First Law
class MendelsFirstLaw():

    def __init__(self, population, pop_traits):
        self.__population        = population
        self.__pop_traits        = pop_traits
        self.__pairprobabilities = self.__initPairSelectionProbabilities()
        self.__dom_trait_prob    = self.__initDominantTraitProbabilities()


    # get the probability of getting an offspring with a dominant trait
    def probabilityOffspringWithDominantTrait(self):
        cumulative_prob = 0.0
        pairs = list(self.__pairprobabilities.keys())
        for pair in pairs:
            cumulative_prob += self.__pairprobabilities[pair] * self.__dom_trait_prob[pair]
        return round(cumulative_prob, 5)



    # for every pair, get the probabiliy of dominant trait expression and return it as a dictionary
    def __initDominantTraitProbabilities(self):
        if self.__pairProbabilitiesValid():
            probabilities = dict()
            pairs         = list(self.__pairprobabilities.keys())
            for pair in pairs:
                probabilities[pair] = self.__pairDominantAlleleProbability(pair)
            return probabilities



    # given a pair, get the probability of it expressing the dominant trait
    def __pairDominantAlleleProbability(self, pair):
        # get both organisms and their allele traits (dominant and recessive)
        organism_x, organism_y = self.__getOrganismsFromPairs(pair)
        x_traits = list(self.__pop_traits[organism_x])
        y_traits = list(self.__pop_traits[organism_y])
        # iterate over the allele traits of the two organisms and count how often two recessive traits get together
        recessive = 0.0
        for trait_x in x_traits:
            for trait_y in y_traits:
                if trait_x == Allele.REC and trait_y == Allele.REC:
                    recessive += 1.0
        # use the total number of recessive combinations to calculate the probability of a dominant trait
        return (4.0-recessive)/4.0



    # check that all pair probabilities add up to one
    def __pairProbabilitiesValid(self):
        probability_sum = sum(self.__pairprobabilities.values())
        # Given that these numbers are floats, round to an integer value
        if round(probability_sum) != 1:
            print("Sum of pair probabilities is not equal to 1. Stop")
            return False
        else:
            return True



    # assigns probabilities for selecting any possible combination of pairs
    def __initPairSelectionProbabilities(self):
        # get the organism types and generate a set of possible pairs (with duplicates)
        organismtypes  = list(self.__population.keys())
        organismpairs  = self.__initOrganismPair2ProbDictionary(organismtypes)
        # assign probabilities for every pair
        for pair in organismpairs:
            first_organism_select_prob  = self.__getFirstOrganismSelectProb(pair)
            second_organism_select_prob = self.__getSecondOrganismSelectProb(pair)
            organismpairs[pair] = first_organism_select_prob * second_organism_select_prob
        return organismpairs



    # calculate the probability for selecting any organism from the entire set
    def __getFirstOrganismSelectProb(self, pair):
        # get the first organism
        organism_x, _ = self.__getOrganismsFromPairs(pair)
        organism_x_freq = float(self.__population[organism_x])
        # get the probability of selecting the first organism
        total           = float(sum(self.__population.values()))
        return organism_x_freq/total



    # calculate the probability for selecting the second organism as a partner
    def __getSecondOrganismSelectProb(self, pair):
        # get the first and second organism as well as the population dictionary
        organism_x, organism_y = self.__getOrganismsFromPairs(pair)
        temp_population        = copy.deepcopy(self.__population)
        # reduce the population by one for the first organism
        temp_population[organism_x] -= 1
        # get the probability of selecting the second organism given the now smaller population
        organism_y_freq = float(temp_population[organism_y])
        total           = float(sum(temp_population.values()))
        return organism_y_freq/total



    # returns a dictionary of possible organism combinations, with the values being 0.0 probabilities
    def __initOrganismPair2ProbDictionary(self, organismtypes):
        organismpairs = dict()
        for organism_x in organismtypes:
            for organism_y in organismtypes:
                combination = self.__organisms2Pair(organism_x, organism_y)
                organismpairs[combination] = 0.0
        return organismpairs



    # takes two organisms and concatenates them to a string: "x,y"
    def __organisms2Pair(self, organism_x, organism_y):
        return organism_x + "," + organism_y


    # takes a combination "x,y" and returns x and y as separate strings
    def __getOrganismsFromPairs(self, combination):
        organism_x = combination.split(",")[0]
        organism_y = combination.split(",")[1]
        return organism_x, organism_y


if __name__ == '__main__':

    # two dictionaries describing the properties of the population (types, number of members and allele information)
    population = {"k": 16, "m": 22, "n": 17}
    pop_traits = {"k": (Allele.DOM, Allele.DOM), "m": (Allele.DOM, Allele.REC), "n": (Allele.REC, Allele.REC)}

    # calculate the required probabilities for this task
    mfl       = MendelsFirstLaw(population, pop_traits)
    dominant  = mfl.probabilityOffspringWithDominantTrait()
    recessive = round(1.0-dominant,5)

    # print results to console
    print("The probability of getting an offspring with a dominant trait is : {}".format(dominant))
    print("The probability of getting an offspring with a recessive trait is: {}".format(recessive))


