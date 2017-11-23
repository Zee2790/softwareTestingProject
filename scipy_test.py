"""
Software Testing Project - Scipy TestUnit

Participant:

- Charbel Kisso
- add you names here

"""

"""
importing important libraries for testing
"""
import unittest
import numpy as np
"""
built-in assert function works with arrays and ndArrays 
"""
from numpy.testing import assert_equal
"""
functions to test:

ToDo: add function here to build test cases for it  
"""
from scipy import misc, linalg, imag, signal
from scipy.linalg import hadamard, subspace_angles
import scipy


class Scipy_Test(unittest.TestCase):


    def setUp(self):
        """

        :return:
        """

        return


    def test_convolve(self):
        """
        this test unit meant to test convolve function from scypi.signal

        function description:
        ---------------------
        Todo: add function description

        :return: this function has no return is meant to be a test case for
        the convolve function.
        """
        x = np.array([1.0, 2.0, 3.0])
        h = np.array([0.0, 1.0, 0.0, 0.0, 0.0])

        assert_equal(signal.convolve(x, h),
                          [0.0, 1.0, 2.0, 3.0, 0.0, 0.0, 0.0])


    def test_subspace_angle(self):

        H = hadamard(4)

        deg = np.rad2deg(subspace_angles(H[:, :2], H[:, 2:]))

        assert_equal(deg, [90, 90])

"""
    def test_full(self):

        scipy.test('full')
"""

if __name__ == '__main__':

    unittest.main()

