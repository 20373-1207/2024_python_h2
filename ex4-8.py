else關鍵字捕獲前面的條件未捕獲的任何內容:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  在這個例子中a大於b，所以第一個條件不成立，elif條件也不成立，所以我們轉到else條件並在螢幕上列印「a 大於 b」。
  
也可以else不帶 elif：
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

簡寫:
if a > b: print("a is greater than b")
