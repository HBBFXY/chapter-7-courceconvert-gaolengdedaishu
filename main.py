# 在这个文件中编写代码实现题目要求的功能

import keyword

with open("D:\\code\\python\\random_int.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

processed_lines = []
for line in lines:
    parts = line.split()
    processed_parts = []
    for part in parts:
        if keyword.iskeyword(part):
            processed_parts.append(part)
        else:
            processed_parts.append(part.upper())
    processed_line = " ".join(processed_parts) + "\n"
    processed_lines.append(processed_line)

with open("D:\\code\\python\\converted_random_int.py", "w", encoding="utf-8") as f:
    f.writelines(processed_lines)

# 以下内容自行完成
