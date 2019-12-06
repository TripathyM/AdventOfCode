import unittest
import puzzle2


class TestBasic(unittest.TestCase):
  def test_basic_parse(self):
    data = puzzle2.parse('''12
    14
    15'''.split())
    self.assertEqual([12, 14, 15], data)

  def test_basic_solve(self):
    data = [14, 1969, 100756]
    self.assertEqual(2 + 966 + 50346, puzzle2.solve(data))

  def test_pass(self):
    f = open("input.txt", "r")
    data = puzzle2.parse(f.readlines())
    answer = puzzle2.solve(data)
    self.assertEqual(0, answer)


if __name__ == '__main__':
  unittest.main()
