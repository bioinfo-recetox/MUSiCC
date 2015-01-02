
"""
This is the testing unit for MUSiCC
"""
# to comply with both Py2 and Py3
from __future__ import absolute_import, division, print_function

import unittest
import musicc
import os
import pandas as pd


class MUSiCCTestCase(unittest.TestCase):
    """Tests for `musicc.py`."""

    def test_is_output_correct_for_normalization_only(self):
        """Does MUSiCC produce the correct output for normalization of the example case?"""
        print(os.path.dirname(musicc.__file__))
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test1.tab', 'input_format': 'tab', 'output_format': 'tab', 'musicc_inter': True,
                       'musicc_intra': 'None', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        musicc.main(musicc_args)
        # assert that the result is equal to the example (up to small difference due to OS/Other)
        example = pd.read_table('examples/simulated_ko_MUSiCC_Normalized.tab', index_col=0)
        output = pd.read_table('examples/test1.tab', index_col=0)
        example_vals = example.values
        output_vals = output.values
        self.assertTrue(example_vals.shape[0] == output_vals.shape[0])
        self.assertTrue(example_vals.shape[1] == output_vals.shape[1])
        for i in range(example_vals.shape[0]):
            for j in range(example_vals.shape[1]):
                self.assertTrue(abs(example_vals[i, j] - output_vals[i, j]) < 1)

        os.remove('examples/test1.tab')

    def test_is_output_correct_for_normalization_correction_use_generic(self):
        """Does MUSiCC produce the correct output for normalization and correction of the example case?"""
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test2.tab', 'input_format': 'tab', 'output_format': 'tab', 'musicc_inter': True,
                       'musicc_intra': 'use_generic', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        musicc.main(musicc_args)
        # assert that the result is equal to the example (up to small difference due to OS/Other)
        example = pd.read_table('examples/simulated_ko_MUSiCC_Normalized_Corrected_use_generic.tab', index_col=0)
        output = pd.read_table('examples/test2.tab', index_col=0)
        example_vals = example.values
        output_vals = output.values
        self.assertTrue(example_vals.shape[0] == output_vals.shape[0])
        self.assertTrue(example_vals.shape[1] == output_vals.shape[1])
        for i in range(example_vals.shape[0]):
            for j in range(example_vals.shape[1]):
                self.assertTrue(abs(example_vals[i, j] - output_vals[i, j]) < 1)

        os.remove('examples/test2.tab')

    def test_is_output_correct_for_normalization_correction_learn_model(self):
        """Does MUSiCC produce the correct output for normalization and correction of the example case?"""
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test3.tab', 'input_format': 'tab', 'output_format': 'tab', 'musicc_inter': True,
                       'musicc_intra': 'learn_model', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        musicc.main(musicc_args)
        # assert that the result is equal to the example (up to small difference due to de novo learning)
        example = pd.read_table('examples/simulated_ko_MUSiCC_Normalized_Corrected_learn_model.tab', index_col=0)
        output = pd.read_table('examples/test3.tab', index_col=0)
        example_vals = example.values
        output_vals = output.values
        self.assertTrue(example_vals.shape[0] == output_vals.shape[0])
        self.assertTrue(example_vals.shape[1] == output_vals.shape[1])
        for i in range(example_vals.shape[0]):
            for j in range(example_vals.shape[1]):
                self.assertTrue(abs(example_vals[i, j] - output_vals[i, j]) < 1)

        os.remove('examples/test3.tab')

################################################

if __name__ == '__main__':
    unittest.main()


