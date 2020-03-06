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
        year = 200
        expectedOutput = False
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

    def testIfYearDivisibleBy4ButNot100AreLeapYears(self):
        year = 2004
        expectedOutput = True
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)

    def testIfYearNotDivisibleBy4AreNotLeapYears(self):
        year = 2002
        expectedOutput = False
        self.assertEqual(LeapYear.isLeapYear(year), expectedOutput)


if __name__=="__main__":
    unittest.main()