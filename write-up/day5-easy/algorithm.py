from itertools import chain
from sympy import isprime

# https://oeis.org/A002385
A002385 = sorted((n for n in chain((int(str(x) + str(x)[::-1]) for x in range(1, 11000)),
                                   (int(str(x) + str(x)[-2::-1]) for x in range(1, 11000))) if isprime(n)))

url = ''

# part 1
i = 1
stack = [17488, 16758, 16599, 16285, 16094, 15505, 15417, 14832, 14450, 13893, 13926, 13437, 12833, 12741, 12533,
         11504, 11342, 10503, 10550, 10319, 975, 1007, 892, 893, 660, 743, 267, 344, 264, 339, 208, 216, 242, 172, 74,
         49, 119, 113, 119, 106]
while len(stack) > 0:
    url += chr(stack.pop() ^ A002385[i - 1])
    i += 1

# part 2
i = 99
stack = [98426, 97850, 97604, 97280, 96815, 96443, 96354, 95934, 94865, 94952, 94669, 94440, 93969, 93766]
while len(stack) > 0:
    url += chr(stack.pop() ^ A002385[i - 1])
    i += 1

# part 3
i = 765
stack = [101141058, 101060206, 101030055, 100998966, 100887990, 100767085, 100707036, 100656111, 100404094, 100160922,
         100131019, 100111100, 100059926, 100049982, 100030045, 9989997, 9981858, 9980815, 9978842, 9965794, 9957564,
         9938304, 9935427, 9932289, 9931494, 9927388, 9926376, 9923213, 9921394, 9919154, 9918082, 9916239, ]
while len(stack) > 0:
    url += chr(stack.pop() ^ A002385[i - 1])
    i += 1

print(url)
# http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/
