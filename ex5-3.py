range() 函數
要循環一組程式碼指定的次數，我們可以使用range()函數，
range ()函數傳回數字序列，預設從 0 開始，以 1 遞增（預設），並以指定數字結束。
for i in range(3):
  for j in range(3):
    print(i,'','',j)
range(6)不是 0 到 6 的值，而是 0 到 5 的值。

for i in range(1,10):
  fro j in range(1,10):
  print(i,"*",j,"=","i*j")
