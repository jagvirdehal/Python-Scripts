palindrome = 0
word = input()
wordLen = len(word)
wordBack = word[::-1]
s = wordLen
if wordBack == word:
    palindrome = wordLen
elif word[:-1] == wordBack[1:]:
    palindrome = wordLen-1
elif word[1:] == wordBack[:-1]:
    palindrome = wordLen-1
elif word[2:] == wordBack[:-2]:
    palindrome = wordLen-2
elif word[1:-1] == wordBack[1:-1]:
    palindrome = wordLen-2
elif word[:-2] == wordBack[2:]:
    palindrome = wordLen-2
elif word[3:] == wordBack[:-3]:
    palindrome = wordLen-3
elif word[2:-1] == wordBack[1:-2]:
    palindrome = wordLen-3
elif word[1:-2] == wordBack[2:-1]:
    palindrome = wordLen-3
elif word[:-3] == wordBack[3:]:
    palindrome = wordLen-3
elif word[4:] == word[:-4]:
    palindrome = wordLen-4
elif word[:-4] == word[4:]:
    palindrome = wordLen-4
elif word[3:-1] == wordBack[1:-3]:
    palindrome = wordLen-4
elif word[2:-2] == wordBack[2:-2]:
    palindrome = wordLen-4
elif word[1:-3] == wordBack[3:-1]:
    palindrome = wordLen-4
elif word[5:] == wordBack[:-5]:
    palindrome = wordLen-5
elif word[:-5] == wordBack[5:]:
    palindrome = wordLen-5
elif word[4:-1] == wordBack[1:-4]:
    palindrome = wordLen-5
elif word[1:-4] == wordBack[4:-1]:
    palindrome = wordLen-5
elif word[3:-2] == wordBack[2:-3]:
    palindrome = wordLen-5
elif word[2:-3] == wordBack[3:-2]:
    palindrome = wordLen-5
elif word[6:] == wordBack[:-6]:
    palindrome = wordLen-6
elif word[:-6] == wordBack[6:]:
    palindrome = wordLen-6
elif word[5:-1] == wordBack[1:-5]:
    palindrome = wordLen-6
elif word[1:-5] == wordBack[5:-1]:
    palindrome = wordLen-6
elif word[4:-2] == wordBack[2:-4]:
    palindrome = wordLen-6
elif word[2:-4] == wordBack[4:-2]:
    palindrome = wordLen-6
elif word[3:-3] == wordBack[3:-3]:
    palindrome = wordLen-6
elif word[7:] == wordBack[:-7]:
    palindrome = wordLen-7
elif word[:-7] == wordBack[7:]:
    palindrome = wordLen-7
elif word[6:-1] == wordBack[1:-6]:
    palindrome = wordLen-7
elif word[1:-6] == wordBack[6:-1]:
    palindrome = wordLen-7
elif word[5:-2] == wordBack[2:-5]:
    palindrome = wordLen-7
elif word[2:-5] == wordBack[5:-2]:
    palindrome = wordLen-7
elif word[4:-3] == wordBack[3:-4]:
    palindrome = wordLen-7
elif word[3:-4] == wordBack[4:-3]:
    palindrome = wordLen-7
elif word[8:] == wordBack[:-8]:
    palindrome = wordLen-8
elif word[:-8] == wordBack[8:]:
    palindrome = wordLen-8
elif word[7:-1] == wordBack[1:-7]:
    palindrome = wordLen-8
elif word[1:-7] == wordBack[7:-1]:
    palindrome = wordLen-8
elif word[6:-2] == wordBack[2:-6]:
    palindrome = wordLen-8
elif word[2:-6] == wordBack[6:-2]:
    palindrome = wordLen-8
elif word[5:-3] == wordBack[3:-5]:
    palindrome = wordLen-8
elif word[3:-5] == wordBack[5:-3]:
    palindrome = wordLen-8
elif word[4:-4] == wordBack[4:-4]:
    palindrome = wordLen-8
elif word[9:] == wordBack[:-9]:
    palindrome = wordLen-9
elif word[:-9] == wordBack[9:]:
    palindrome = wordLen-9
elif word[8:-1] == wordBack[1:-8]:
    palindrome = wordLen-9
elif word[1:-8] == wordBack[8:-1]:
    palindrome = wordLen-9
elif word[7:-2] == wordBack[2:-7]:
    palindrome = wordLen-9
elif word[2:-7] == wordBack[7:-2]:
    palindrome = wordLen-9
elif word[6:-3] == wordBack[3:-6]:
    palindrome = wordLen-9
elif word[3:-6] == wordBack[6:-3]:
    palindrome = wordLen-9
elif word[5:-4] == wordBack[4:-5]:
    palindrome = wordLen-9
elif word[4:-5] == wordBack[5:-4]:
    palindrome = wordLen-9
elif word[10:] == wordBack[:-10]:
    palindrome = wordLen-10
elif word[:-10] == wordBack[10:]:
    palindrome = wordLen-10
elif word[9:-1] == wordBack[1:-9]:
    palindrome = wordLen-10
elif word[1:-9] == wordBack[9:-1]:
    palindrome = wordLen-10
elif word[8:-2] == wordBack[2:-8]:
    palindrome = wordLen-10
elif word[2:-8] == wordBack[8:-2]:
    palindrome = wordLen-10
elif word[7:-3] == wordBack[3:-7]:
    palindrome = wordLen-10
elif word[3:-7] == wordBack[7:-3]:
    palindrome = wordLen-10
elif word[6:-4] == wordBack[4:-6]:
    palindrome = wordLen-10
elif word[4:-6] == wordBack[6:-4]:
    palindrome = wordLen-10
elif word[5:-5] == wordBack[5:-5]:
    palindrome = wordLen-10
elif word[11:] == wordBack[:-11]:
    palindrome = wordLen-11
elif word[:-11] == wordBack[11:]:
    palindrome = wordLen-11
elif word[10:-1] == wordBack[1:-10]:
    palindrome = wordLen-11
elif word[1:-10] == wordBack[10:-1]:
    palindrome = wordLen-11
elif word[9:-2] == wordBack[2:-9]:
    palindrome = wordLen-11
elif word[2:-9] == wordBack[9:-2]:
    palindrome = wordLen-11
elif word[8:-3] == wordBack[3:-8]:
    palindrome = wordLen-11
elif word[3:-8] == wordBack[8:-3]:
    palindrome = wordLen-11
elif word[7:-4] == wordBack[4:-7]:
    palindrome = wordLen-11
elif word[4:-7] == wordBack[7:-4]:
    palindrome = wordLen-11
elif word[6:-5] == wordBack[5:-6]:
    palindrome = wordLen-11
elif word[5:-6] == wordBack[6:-5]:
    palindrome = wordLen-11
elif word[12:] == wordBack[:-12]:
    palindrome = wordLen-12
elif word[:-12] == wordBack[12:]:
    palindrome = wordLen-12
elif word[11:-1] == wordBack[1:-11]:
    palindrome = wordLen-12
elif word[1:-11] == wordBack[11:-1]:
    palindrome = wordLen-12
elif word[10:-2] == wordBack[2:-10]:
    palindrome = wordLen-12
elif word[2:-10] == wordBack[10:-2]:
    palindrome = wordLen-12
elif word[9:-3] == wordBack[3:-9]:
    palindrome = wordLen-12
elif word[3:-9] == wordBack[9:-3]:
    palindrome = wordLen-12
elif word[8:-4] == wordBack[4:-8]:
    palindrome = wordLen-12
elif word[4:-8] == wordBack[8:-4]:
    palindrome = wordLen-12
elif word[7:-5] == wordBack[5:-7]:
    palindrome = wordLen-12
elif word[5:-7] == wordBack[7:-5]:
    palindrome = wordLen-12
elif word[6:-6] == wordBack[6:-6]:
    palindrome = wordLen-12
print(palindrome)
