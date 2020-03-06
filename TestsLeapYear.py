import unittest
import LeapYear

class LeapYearTests(unittest.TestCase):
    def testIfNotALeapYearReturnFalse(self):
        year = 123
        expectedOutput = False
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

    def testIfYearDivisibleBy400ReturnTrue(self):
        year = 400
        expectedOutput = True
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

    def testIfYearDivisibleBy100ButNot400ReturnFalse(self):
        year = 300
        expectedOutput = False
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

if __name__=="__main__":
    unittest.main()