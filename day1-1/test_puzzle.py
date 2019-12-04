import unittest
import puzzle


class TestBasic(unittest.TestCase):
  def test_basic_parse(self):
    data = puzzle.parse('''12
    14
    15'''.split())
    self.assertEqual([12, 14, 15], data)

  def test_basic_solve(self):
    data = [12, 14, 1969, 100756]
    self.assertEqual(34241, puzzle.solve(data))

  def test_pass(self):
    f = open("input.txt", "r")
    data = puzzle.parse(f.readlines())
    answer = puzzle.solve(data)
    self.assertEqual(0, answer)


if __name__ == '__main__':
  unittest.main()
