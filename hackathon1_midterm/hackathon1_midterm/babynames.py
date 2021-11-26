#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Python for Tester - OneMount Class
# Quang Le - quangdle@gmail.com - 09/2021

import sys
import re

"""Baby Names exercise

Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().

Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""

def extract_names(filename):
  """
  Cho một file .html, trả ra list bắt đầu bằng năm, 
  theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  regex_year = r'<h3 align="center">Popularity in (\d+)<\/h3>'
  regex_names = r'<tr align="right"><td>(\d+)<\/td><td>(.+)<\/td><td>(.+)<\/td>'
  try:
    year = None
    names = []
    with open(filename, 'r', encoding='utf-8') as f:
      content = f.read()
      year_search = re.search(regex_year, content)
      if year_search:
        year = year_search.group(1)
      for name_result in re.findall(regex_names, content):
        names.append('{} {}'.format(name_result[1], name_result[0]))
        names.append('{} {}'.format(name_result[2], name_result[0]))
    return [year] + names
  except:
    return None

def main():
  # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  output = ''
  for filename in args:
    data = extract_names(filename)
    if data is None:
      continue
    output += str(data) + '\n'
  if summary:
    with open('summary', 'w', encoding='utf-8') as f:
      f.write(output)
      f.flush()
  else:
    print(output)

if __name__ == '__main__':
  main()
