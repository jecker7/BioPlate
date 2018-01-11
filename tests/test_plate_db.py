import unittest
from BioPlate.database.plate_db import PlateDB
import contextlib
import os


class TestPlateDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This function is run one time at the beginning of tests
        :return:
        """
        cls.pdb = PlateDB(db_name='test_plate.db')
        cls.pdb.add_plate(numWell=96,
              numColumns=12,
              numRows=8,
              surfWell=0.29,
              maxVolWell=200,
              workVolWell=200,
              refURL='https://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf')


    @classmethod
    def tearDownClass(cls):
        """
        This function is run one time at the end of tests
        :return:
        """
        with contextlib.suppress(FileNotFoundError):
            os.remove(os.path.abspath(os.path.join(os.pardir, os.path.join('BioPlate/database/DBFiles', 'test_plate.db'))))

    def setUp(self):
        """
        This function is run every time at the beginning of each test
        :return:
        """
        self.plate_list = self.pdb.get_plate(96)
        self.plate = self.plate_list[0]

    def tearDown(self):
        """
        This function is run every time at the end of each test
        :return:
        """
        pass

    def test_get_plate(self):
        self.assertIsInstance(self.plate_list, list, "plate_db.get_plate don't return a list")
        self.assertEquals('<plate N°1 : 96-12-8>', str(self.plate),
                          "plate_db.get_plate don't return the appropriate format")
        self.assertTrue(str(type(self.plate)) == "<class 'BioPlate.database.plate_db.PlateDB.PlateDatabase'>",
                        f"plate_db.get_plate don't return the right class : {str(type(self.plate))}")

    def test_plate_class(self):
        self.assertEqual(self.plate.numWell, 96, "Error numWell association fail")
        self.assertEqual(self.plate.numColumns, 12, "Error numColumns association fail")
        self.assertEqual(self.plate.numRows, 8, "Error numRows association fail")
        self.assertEqual(self.plate.surfWell, 0.29, "Error numRows association fail")
        self.assertEqual(self.plate.maxVolWell, 200, "Error numRows association fail")
        self.assertEqual(self.plate.workVolWell, 200, "Error numRows association fail")
        self.assertEqual(self.plate.refURL, "https://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf",
                         "Error refURL association fail")

    def test_add_plate(self):
        add_plate_1 = self.pdb.add_plate(numWell=6,
                      numColumns=3,
                      numRows=2,
                      surfWell=9.5,
                      maxVolWell=2000,
                      workVolWell=2000,
                      refURL='https://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf')
        self.assertEqual(add_plate_1,
        	                "plate with 6 added to the database")
        add_plate_2 = self.pdb.add_plate(numWell=6,
                      numColumns=3,
                      numRows=2,
                      surfWell=9.5,
                      maxVolWell=2000,
                      workVolWell=2000,
                      refURL='https://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf')
        self.assertEqual(add_plate_2, None)
        self.assertEquals('<plate N°2 : 6-3-2>', str(self.pdb.get_plate(6)[0]))
        self.assertEquals(6, self.pdb.get_plate(6)[0].numWell)

    def test_delete_plate(self):
        self.pdb.add_plate(numWell=24,
              numColumns=6,
              numRows=4,
              surfWell=0.33,
              maxVolWell=400,
              workVolWell=400,
              refURL='https://csmedia2.corning.com/LifeSciences/Media/pdf/cc_surface_areas.pdf')
        self.assertEqual(self.pdb.delete_plate(24), "plate with 24 numWell deleted")
        self.assertEqual(self.pdb.get_plate(24), [])

if __name__ == '__main__':
    unittest.main()