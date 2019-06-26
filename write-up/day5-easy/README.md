## Write-up: FriendSpaceBookPlusAllAccessRedPremium.com

Google CTF 2019: [Beginner’s Quest](https://capturetheflag.withgoogle.com/#beginners/)

![Task](img/task.jpg)

This is a `reversing` challenge about deciphering this kind of program which can be run with `vm.py`, “a simple stack-based VM”:

```
🚛 🥇 0️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 7️⃣ 4️⃣ 8️⃣ 8️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 6️⃣ 7️⃣ 5️⃣ 8️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 6️⃣ 5️⃣ 9️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 6️⃣ 2️⃣ 8️⃣ 5️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 6️⃣ 0️⃣ 9️⃣ 4️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 5️⃣ 5️⃣ 0️⃣ 5️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 5️⃣ 4️⃣ 1️⃣ 7️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 4️⃣ 8️⃣ 3️⃣ 2️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 4️⃣ 4️⃣ 5️⃣ 0️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 3️⃣ 8️⃣ 9️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 3️⃣ 9️⃣ 2️⃣ 6️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 3️⃣ 4️⃣ 3️⃣ 7️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 2️⃣ 8️⃣ 3️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 2️⃣ 7️⃣ 4️⃣ 1️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 2️⃣ 5️⃣ 3️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 1️⃣ 5️⃣ 0️⃣ 4️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 1️⃣ 3️⃣ 4️⃣ 2️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 0️⃣ 5️⃣ 0️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 0️⃣ 5️⃣ 5️⃣ 0️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 0️⃣ 3️⃣ 1️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 9️⃣ 7️⃣ 5️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 0️⃣ 0️⃣ 7️⃣ ✋ 📥 🥇
🚛 🥇 8️⃣ 9️⃣ 2️⃣ ✋ 📥 🥇
🚛 🥇 8️⃣ 9️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 6️⃣ 6️⃣ 0️⃣ ✋ 📥 🥇
🚛 🥇 7️⃣ 4️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 2️⃣ 6️⃣ 7️⃣ ✋ 📥 🥇
🚛 🥇 3️⃣ 4️⃣ 4️⃣ ✋ 📥 🥇
🚛 🥇 2️⃣ 6️⃣ 4️⃣ ✋ 📥 🥇
🚛 🥇 3️⃣ 3️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 2️⃣ 0️⃣ 8️⃣ ✋ 📥 🥇
🚛 🥇 2️⃣ 1️⃣ 6️⃣ ✋ 📥 🥇
🚛 🥇 2️⃣ 4️⃣ 2️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 7️⃣ 2️⃣ ✋ 📥 🥇
🚛 🥇 7️⃣ 4️⃣ ✋ 📥 🥇
🚛 🥇 4️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 1️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 1️⃣ 3️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 1️⃣ 9️⃣ ✋ 📥 🥇
🚛 🥇 1️⃣ 0️⃣ 6️⃣ ✋ 📥 🥇
🚛 🥈 1️⃣ ✋

# ...

🖋🎌🏁💠🔶🚩
🤡 🤡 🚛 🥈 0️⃣ ✋ 📥 🥈
🖋🏁💠🔶🚩🎌 🚛 🥇 1️⃣ 0️⃣ ✋ 📥 🥇
⭐ 🍿 🥈 📥 🥇 📬
📥 🥈 🍡 🍿 🥈 🍿 🥇 🤡 📥 🥈 🔪
😲 📤 🚛 🥈 1️⃣ ✋ 📥 🥈 🏀 💰🎌🏁🚩🔶💠 😐
📤 📥 🥇 🚛 🥇 1️⃣ 0️⃣ ✋ 📥 🥇 📐
😲 🏀 💰🎌🏁🚩🔶💠 😐
🤡 📥 🥈 🏀 💰🏁💠🔶🚩🎌
```

Getting the code to run is not the problem, the amount of time it takes for it to output the URL containing the flag is. The program outputs this URL character by character and it takes and longer and longer for the next character to appear. Guessing the rest of the URL (`http://emoji-t0anaxnr3nacpt4na.web.ctf…` obviously results in http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/) is also not possible, because the complete URL contains a very long directory name.

The first thing we can do is to replace most of the emoji characters with actual commands (see `OPERATIONS` in `vm.py`). The excerpt above could become something like this (see [./less-emoji/program](https://github.com/weibell/ctf-google2019-beginners/blob/master/write-up/day5-easy/less-emoji/program)).

```
load A 0 . push A
load A 1 7 4 8 8 . push A
load A 1 6 7 5 8 . push A
load A 1 6 5 9 9 . push A
load A 1 6 2 8 5 . push A
load A 1 6 0 9 4 . push A
load A 1 5 5 0 5 . push A
load A 1 5 4 1 7 . push A
load A 1 4 8 3 2 . push A
load A 1 4 4 5 0 . push A
load A 1 3 8 9 3 . push A
load A 1 3 9 2 6 . push A
load A 1 3 4 3 7 . push A
load A 1 2 8 3 3 . push A
load A 1 2 7 4 1 . push A
load A 1 2 5 3 3 . push A
load A 1 1 5 0 4 . push A
load A 1 1 3 4 2 . push A
load A 1 0 5 0 3 . push A
load A 1 0 5 5 0 . push A
load A 1 0 3 1 9 . push A
load A 9 7 5 . push A
load A 1 0 0 7 . push A
load A 8 9 2 . push A
load A 8 9 3 . push A
load A 6 6 0 . push A
load A 7 4 3 . push A
load A 2 6 7 . push A
load A 3 4 4 . push A
load A 2 6 4 . push A
load A 3 3 9 . push A
load A 2 0 8 . push A
load A 2 1 6 . push A
load A 2 4 2 . push A
load A 1 7 2 . push A
load A 7 4 . push A
load A 4 9 . push A
load A 1 1 9 . push A
load A 1 1 3 . push A
load A 1 1 9 . push A
load A 1 0 6 . push A
load B 1 .

# ...

MMARKER11
clone clone load B 0 . push B
MMARKER12 load A 1 0 . push A
multiply pop B push A modulo
push B add pop B pop A clone push B sub
if_zero pop_out load B 1 . push B jump_to JMARKER7 X
pop_out push A load A 1 0 . push A divide
if_zero jump_to JMARKER7 X
clone push B jump_to JMARKER12
```

“`.`” indicates the end of a sequence to be loaded in the first accumulator (`A`). `MMARKER11` (beginning with an `M`) is a label which can be jumped to with `JMARKER11`. `X` is placed at the end of an if-condition.

Adding or removing instructions would mess with the `jump_top`, which jump to the absolute address on the top of the stack. Instead, by observing the stack contents in functions such as `print_top`, `xor` and `jump_to`, we can draw conclusions about the behavior of the program.

It turns out that the program loads three blocks of integers onto the stack, XORs each integer with [palindromic primes](https://en.wikipedia.org/wiki/Palindromic_prime) (sequence [A002385](https://oeis.org/A002385) in the OEIS) and then outputs the corresponding ASCII value. The first block (line 1 to 42) begins with the 1st palindromic prime (2) and the number 106 (`chr(106 ^ 2) == "h"`) and then continues with the 2nd and the number 119 (`chr(119 ^ 3) == "t"`), the 3rd and the number 113 (`chr(113 ^ 5) == "t"`) and so on until the stack is empty and the next stack (lines 51 to 65) is processed. Here, a jump occurs to the 99th and later to the 765th palindromic prime numbers, but the procedure remains the same.

## Algorithm

We can reduce the program to this ([algorithm.py](https://github.com/weibell/ctf-google2019-beginners/blob/master/write-up/day5-easy/algorithm.py)):

```python
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
```

## Patching `vm.py`

Another option is to patch `vm.py` and to intercept calls made to the most computationally intensive part of the program (see  [./patched/vm.py](https://github.com/weibell/ctf-google2019-beginners/blob/master/write-up/day5-easy/patched/vm.py) and [./less-emoji/patched.py](https://github.com/weibell/ctf-google2019-beginners/blob/master/write-up/day5-easy/less-emoji/patched.py)):

```python
import sys

from itertools import chain
from sympy import isprime

# ...

 def __init__(self, rom):
    # ...
    self.A002385 = sorted((n for n in chain((int(str(x) + str(x)[::-1]) for x in range(1, 11000)),
                                            (int(str(x) + str(x)[-2::-1]) for x in range(1, 11000))) if isprime(n)))
    # ...
    
  def jump_to(self):
    # ...
    marker = '🖋' + marker[1:]
    if marker == '🖋🏁🚩🎌💠🔶':
      prime_index = self.stack.pop()
      return_address = self.stack.pop()
      self.stack.append(self.A002385[prime_index - 1])
      self.instruction_pointer = return_address
    else:
      self.instruction_pointer = self.rom.index(marker) + 1
```

## Flag

Both programs output the complete URL in a matter of seconds:
<http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/>

The flag flag is just one click away:
<http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/amber.html>

![Flag](/home/gw/git/ctf-google2019-beginners/write-up/day5-easy/emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/out-2.png)

**Flag**: `CTF{Peace_from_Cauli!}`

