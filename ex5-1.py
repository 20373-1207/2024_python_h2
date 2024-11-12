break --> 強制停止程式
使用break語句，即使while條件為真，我們也可以停止迴圈：
當 i 為 3 時退出循環：
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

+=:加法和賦值
　　　　將等號左邊指定為等號左邊加上等號右邊，i+=1代表i = i + 1

continue-->持續執行程式
使用continue語句，我們可以停止目前迭代，並繼續下一個迭代：
如果 i 為 3，則繼續下一個迭代：

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


else
使用else語句，我們可以在條件不再為真時執行一次程式碼區塊：
一旦條件為假，列印一則訊息：

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

