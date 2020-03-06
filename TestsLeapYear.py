import unittest
import LeapYear

class LeapYearTests(unittest.TestCase):
    def testAnyYearIsNotALeapYear(self):
        year = 123
        expectedOutput = False
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

if __name__=="__main__":
    unittest.main()