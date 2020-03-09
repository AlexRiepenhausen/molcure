
# class for solving the problem of transcribing DNA to RNA
class TranscribingDNA2RNA():

    def __init__(self, path):
        self.__dnastring = self.__readDNAStringFromFile(path)
        self.__rnastring = self.__convert2RNAString()


    # prints both DNA and RNA - a limit concerning the print length can be provided (optional)
    def printDNAandRNA(self, limit=None):
        if not limit:
            print("DNA: " + self.__dnastring)
            print("RNA: " + self.__rnastring)
        else:
            print("DNA: " + self.__dnastring[0:limit])
            print("RNA: " + self.__rnastring[0:limit])


    # return the entire RNA strand for further processing if necessary
    def getRNAStrand(self):
        return self.__rnastring


    # return the entire RNA strand for further processing if necessary
    def getDNAStrand(self):
        return self.__dnastring


    # reads a single dna string from any given file
    def __readDNAStringFromFile(self, filepath):
        with open(filepath) as file:
            line = file.readline()
            return line.replace("\n","")


    # converts the dna string of this class to its corresponding RNA string
    def __convert2RNAString(self):
        rnastring = ""
        for nucleotide in self.__dnastring:
            if nucleotide == "T":
                rnastring += "U"
            else:
                rnastring += nucleotide
        return rnastring



if __name__ == '__main__':

    path = "../data/rosalind_rna.txt"
    dna2rna = TranscribingDNA2RNA(path)
    dna2rna.printDNAandRNA()


