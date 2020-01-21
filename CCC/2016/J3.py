def pal(text):
    text = text.lower()
    output = []
    if text == text[::-1]:
        return len(text)
    else:
        for i in range(len(text)):
            for j in range(0, i):
                chunk = text[j:i +1]

                if chunk == chunk[::-1]:
                    output.append(chunk)
        return len(max(output, key=len))
while True:
    st = input()
    print(pal(st))
