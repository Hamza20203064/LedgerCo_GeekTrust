# Drive
import unittest
import sys
sys.path.append(
    'C:\\hamzaPrograming\\LLD\\LedgerCo_GeekTrust\\python-pip-starter-kit\\')
from src.main import Main


class PaymentBalanceLoanTest(unittest.TestCase):

    def setUp(self):
        self.driver = Main()

    def test_test1(self):

        # a = open('path', 'r')
        # b = a.readlines()
        # a.close()
        inputFile = open('tests/resources/input/input1.txt', 'r')
        readInput = inputFile.readlines()
        inputFile.close()
        outputFile = open(
            'tests/resources/output/output1.txt', 'r')
        readOutputFile = outputFile.readlines()
        outputFile.close()
        expected_output = [line.split() for line in readOutputFile]
        output = self.driver.app(readInput)
        print("Expected output")
        print(expected_output)
        print("Output")
        print(output)
        self.assertEqual(output, expected_output)

    def test_test2(self):
        inputFile = open('tests/resources/input/input2.txt', 'r')
        readInput = inputFile.readlines()
        inputFile.close()
        outputFile = open(
            'tests/resources/output/output2.txt', 'r')
        readOutputFile = outputFile.readlines()
        outputFile.close()
        expected_output = [line.split() for line in readOutputFile]
        output = self.driver.app(readInput)
        print("Expected output")
        print(expected_output)
        print("Output")
        print(output)
        self.assertEqual(output, expected_output)
    def test_test4(self):
        inputFile = open('tests/resources/input/input4.txt', 'r')
        readInput = inputFile.readlines()
        inputFile.close()
        outputFile = open(
            'tests/resources/output/output4.txt', 'r')
        readOutputFile = outputFile.readlines()
        outputFile.close()
        expected_output = [line.split() for line in readOutputFile]
        output = self.driver.app(readInput)
        print("Expected output")
        print(expected_output)
        print("Output")
        print(output)
        self.assertEqual(output, expected_output)
    def test_test5(self):
        inputFile = open('tests/resources/input/input5.txt', 'r')
        readInput = inputFile.readlines()
        inputFile.close()
        outputFile = open(
            'tests/resources/output/output5.txt', 'r')
        readOutputFile = outputFile.readlines()
        outputFile.close()
        expected_output = [line.split() for line in readOutputFile]
        output = self.driver.app(readInput)
        print("Expected output")
        print(expected_output)
        print("Output")
        print(output)
        self.assertEqual(output, expected_output)
    

    # def test_test2(self):
    #     input = open('tests/resources/input/input1.txt', 'r').readlines()
    #     outputFile = open(
    #         'tests/resources/output/output1.txt', 'r').readlines()
    #     output = [line.split() for line in outputFile]
    #     self.assertEqual(self.driver.app(input), output)

    # def test_test2(self):
    #     """Whether output is correct generated with only loan statements"""
    #     input = open('tests/resources/input/loan_only.txt', 'r').readlines()
    #     output = []
    #     self.assertEqual(self.driver.runApp(input), output)


if __name__ == '__main__':
    unittest.main()
