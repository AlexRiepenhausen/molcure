
# class for solving the problem of counting the frequency of DNA nucleotides
class CountingDNANucleotides():

    def __init__(self, path, nucleotide_array):
        self.__nucleotides = nucleotide_array
        self.__dnastring   = self.__readDNAStringFromFile(path)
        self.__histogram   = self.__populateHistogram(nucleotide_array)


    # return the entire histogram as a variable if desired for further processing
    def getHistogram(self):
        return self.__histogram


    # return the entire RNA strand for further processing if necessary
    def getDNAStrand(self):
        return self.__dnastring


    # present the histogram in a human readable form
    def printHistogram(self):
        outputstring = ""
        print("Nucleotides: ")
        for nucleotide, count in self.__histogram.items():
            outputstring += str(count) + " "
            print("- {} ({})".format(nucleotide, count))
        print("\nRequired output format:\n" + outputstring)


    # reads a single dna string from any given file
    def __readDNAStringFromFile(self, filepath):
        with open(filepath) as file:
            line = file.readline()
            return line.replace("\n","")


    # initialises and returns dictionary with the keys being provided as a parameter
    def __initNucleotideHistogram(self, nucleotides):
        histogram = dict()
        for nucleotides in nucleotides:
            histogram[nucleotides] = 0
        return histogram


    # populate the histogram with information from the DNA data
    def __populateHistogram(self, nucleotide_array):
        histogram = self.__initNucleotideHistogram(nucleotide_array)
        for nucleotide in self.__dnastring:
            histogram[nucleotide] += 1
        return histogram


if __name__ == '__main__':

    path        = "../data/rosalind_dna.txt"
    nucleotides = ["A","C","G","T"]

    cdn = CountingDNANucleotides(path, nucleotides)
    cdn.printHistogram()


