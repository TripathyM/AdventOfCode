def parse(lines):
  ans = []
  for line in lines:
    if line:
      ans.append(int(line))
  return ans

def solve(data):
  total=0
  for line in data:
    mass = int(line)
    while mass >= 6:
      fuel = mass // 3 - 2
      total += fuel
      mass = fuel

  return total