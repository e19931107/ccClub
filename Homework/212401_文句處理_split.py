import re
import sys
word = input().split()
patterns = sorted(word, key = len, reverse = True)

while True:
    text = input()
    if text == 'end':
        break
    
    for pattern in patterns:
        text = re.sub(rf'\b{pattern}\b', rf'「{pattern}」', text)

    # Output the result using sys.stdout and UTF-8 encoding
    sys.stdout.buffer.write(text.encode('utf-8'))
    sys.stdout.write('\n')

    # 輸出結果
    print(text)

