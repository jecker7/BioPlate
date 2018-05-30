import unittest

from BioPlate.Manipulation import BioPlateManipulation



class TestBioPlateManipulation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        This function is run one time at the beginning of tests
        :return:
        """
        pass


    @classmethod
    def tearDownClass(cls):
        """
        This function is run one time at the end of tests
        :return:
        """
        pass
        

    def setUp(self):
        """
        This function is run every time at the beginning of each test
        :return:
        """
        self.BPM = BioPlateManipulation()
        
    def tearDown(self):
        """
        This function is run every time at the end of each test
        :return:
        """
        pass
        

    def test_add_values(self):
        self.assertEqual(self.BPM._add_values({"A": {3 : 5}}), "{'A': {3: 5}} have a wrong format")
        
        
        
        
        
if __name__ == "__main__":
     unittest.main()
       