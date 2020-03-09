import math
import numpy as np

class Castles():

    """ This class contains the code for solving Problem 502, Counting Castles. It uses Dynamic Programming.
    """

    def __init__(self, castle_width, castle_height):
        """
        Parameters
        ----------
        castle_width : int
            The required width for any possible type of castle
        castle_height : int
            The required height for any possible type of castle
        """

        self._castle_width   = castle_width
        self._castle_height  = castle_height

        #: obj:`numpy. array` of :obj:`numpy. array`: matrix containing intermediate
        # results for the number of possible configurations given any width and the possible max number of blocks
        self._config_matrix  = self.initConfigMatrix(castle_width)



    def populateConfigMatrix(self, load=False):
        for width in range(1, self._castle_width + 1):
            max_num_blocks = self._getMaxNumberOfBlocks(width)
            for num_blocks in range(1, max_num_blocks + 1):
                self.calculateItemInConfigMatrix(num_blocks, width)



    def calculateItemInConfigMatrix(self, num_blocks, width):
        result = 0
        self.editItemInConfigMatrix(num_blocks, width, result)



    def accessItemInConfigMatrix(self, num_blocks, width):
        number_possible_configurations = self._config_matrix[num_blocks-1][width-1]
        return number_possible_configurations



    def editItemInConfigMatrix(self, num_blocks, width, result):
        self._config_matrix[num_blocks-1][width-1] = result



    def _getMaxNumberOfBlocks(self, width):
        """ Returns the highest possible number of blocks given a certain width
        Parameters
        ----------
        width: int
            Any width smaller than the width of the castle
        Returns
        -------
        max_num_blocks: int
            Highest possible number of blocks given the width
        """
        max_num_blocks = int(math.ceil(float(width)/2.0))
        return max_num_blocks



    def _getMaxBlockWidth(self, width, num_blocks):
        """ Returns maximum possible width of a block in a row given a certain width limit
            and the required number of blocks in said row.
            The method takes the required number of spaces into account
        Parameters
        ----------
        width: int
            Any width smaller or equal the width of the castle
        num_blocks: int
            The number of blocks required in a row
        Returns
        -------
        max_block_width: int
            The largest possible width for any block in a castle row
        """
        max_block_width = width - 2 * num_blocks + 2
        return max_block_width



    def initConfigMatrix(self, castle_width):
        max_num_blocks = self._getMaxNumberOfBlocks(castle_width)
        config_matrix  = np.zeros((self._getMaxNumberOfBlocks(castle_width), castle_width))
        return config_matrix



    def getCastleWidth(self):
        # return the innate width of the castle
        return self._castle_width



    def getCastleHeight(self):
        # return the innate height of the castle
        return self._castle_height


if __name__ == '__main__':

    # A partial solution to this problem had been achieved
    # The description to the partial solution can be found within the Readme
    # Given the difficulty level of this problem, solving it within the given time frame was not possible

    exit(0)