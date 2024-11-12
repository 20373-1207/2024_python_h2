Python For 循環
for迴圈用於迭代序列（即列表、元組、字典、集合或字串）。
這不太像其他程式語言中的for關鍵字，而更像其他物件導向程式語言中的迭代器方法。
使用for迴圈，我們可以執行一組語句，對清單、元組、集合等中的每個項目執行一次。

列印水果清單中的每個水果：

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

Looping Through a String
循環遍歷字串:
即使字串也是可迭代對象，它們也包含一系列字元：
循環遍歷單字“banana”中的字母：

for x in "banana":
  print(x)

The break Statement
中斷語句
使用break語句，我們可以在循環完所有項目之前停止循環：
當為“banana”時退出循環x：
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

當 為「banana」時退出循環x，但這次中斷出現在列印之前：

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
