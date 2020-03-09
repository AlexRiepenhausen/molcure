
# class for solving the problem of converting DNA to its reverse complement
class ComplementingDNA():

    def __init__(self, path, complements):
        self.__complements = complements
        self.__dnastring   = self.__readDNAStringFromFile(path)
        self.__revcomp     = self.__convertDNA2RevComp()


    # prints both DNA and its reverse complement - a limit concerning the print length can be provided (optional)
    def printDNAandReverseComplement(self, limit=None):
        if not limit:
            print("DNA:                " + self.__dnastring)
            print("Reverse Complement: " + self.__revcomp)
        else:
            print("DNA:                " + self.__dnastring[0:limit])
            print("Reverse Complement: " + self.__revcomp[0:limit])


    # return the entire reverse complement of the DNA strand for further processing if necessary
    def getReverseComplement(self):
        return self.__revcomp


    # return the entire DNA strand for further processing if necessary
    def getDNAStrand(self):
        return self.__dnastring


    # reads a single dna string from any given file
    def __readDNAStringFromFile(self, filepath):
        with open(filepath) as file:
            line = file.readline()
            return line.replace("\n","")



    # converts the dna string of this class to its reverse complement
    def __convertDNA2RevComp(self):
        revcomp  = ""
        for nucleotide in self.__dnastring[::-1]:
            revcomp += self.__complements[nucleotide]
        return revcomp



if __name__ == '__main__':

    # dictionary of complements and the file path
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    path        = "../data/rosalind_revc.txt"

    # solution
    dna2rna = ComplementingDNA(path, complements)
    dna2rna.printDNAandReverseComplement()


