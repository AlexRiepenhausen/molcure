# Molcure Coding Interview
As requested, I did a couple of example exercises on both ROSALIND and Projecteuler.
My username on ROSALIND is *AlexRiepenhausen*. The username on Projecteuler is *alexRiepenhausen*.
The links to both websites are provided down below:

ROSALIND:     [http://rosalind.info/problems/list-view/](http://rosalind.info/problems/list-view/)

Projecteuler: [https://projecteuler.net/](https://projecteuler.net/)

As for ROSALIND, the following problems were solved successfully:
| **Problem Name**                  | **Directory**      | **Link**                                                            |
| --------------------------------- |:------------------:| -------------------------------------------------------------------:|
| Counting DNA Nucleotides          | rosalind/problem01 | [rosalind.info/problems/dna/](http://rosalind.info/problems/dna/)   |
| Transcribing DNA into RNA         | rosalind/problem02 | [rosalind.info/problems/rna/](http://rosalind.info/problems/rna/)   |
| Complementing a Strand of DNA     | rosalind/problem03 | [rosalind.info/problems/revc/](http://rosalind.info/problems/revc/) |
| Mendel's First Law                | rosalind/problem04 | [rosalind.info/problems/iprb/](http://rosalind.info/problems/iprb/) |

All files are executable, stand-alone python scripts.
The solutions to the problems have not been posted on this repository, but can be generated with the python sripts provided. Alternatively, the solutions can be provided upon request.

As for Projecteuler, two problems were attempted, out of which one was solved successfully and a partial solution to the second one was achieved:
| **Problem Name**                    | **Directory**          | **Link**                                                             |
| ----------------------------------- |:----------------------:| --------------------------------------------------------------------:|
| Counting Castles, Problem 502       | projecteuler/problem01 | [projecteuler.net/problem=502](https://projecteuler.net/problem=502) |
| Sub-string divisibility, Problem 43 | projecteuler/problem02 | [projecteuler.net/problem=43](https://projecteuler.net/problem=43)   |

Sub-string divisibility (Problem 43) was solved successfully. With problem 502, only a partial solution was found due to time constraints and the problem's difficulty level.

#### Counting Castles, Problem 502 Partial Solution

The partial solution to the castle problem looks as follows:
We define the width of the castle to be **w** and its height to be **h**
For a castle consisting of only the first and second row, the number of possible castles is **(2^w)+1** if we assume **h=2**. 
The additional number one simply represents the bottom row, which is required to be of width **w**.
If we ignore the given constraints, then the possible number of castles for any given height **h>2** is going to be **((2^w)^h) + 1**.
Thus, it can be said that the total number of castles is smaller than **((2^w)^h) + 1**.

The main reason why the number of possible combinations in any one row are 2^**w** if the row below is occupied by a block of width **w** can be explained relatively easily.
For example, if we define **b** to be a block of width one and **g** to be a gap of width one, then the second row of the castle is going to have the following combinations:

- **(b + e)^2 = b^2 + 2be + e^2**

This means that one can either have two empty spaces, two blocks of width one (effectively a block of width two, so that the constraints are not violated), 
and two possible combinations of an empty block and one block of size one (either left or right). The total number of possibilities is hence **1 + 2 + 1 = 4**.
These numbers are the binomial coefficients of the above formula. For any width **w** the sum of binomial coefficients is defined as **2^w** (a proof can be found [here](https://proofwiki.org/wiki/Sum_of_Entries_in_Row_of_Pascal%27s_Triangle#:~:text=So%20the%20sum%20of%20all,equal%20to%202k%2B1.)). 
Hence the number of possible combinations on the second row is **2^w**.



