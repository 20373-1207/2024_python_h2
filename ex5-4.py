主函式輸入，高與寬，編寫程式，算矩形面積
h=int(input("please input h "))
w=int(input("please input w "))
print("h=",h,"w=",w)
print("area=", h*w)

輸出當月天數
輸入年 月, 輸出當月天數
year=int(input("please input year"))
month=int(input("please input month"))
print("year=",year,"month=",month)
if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
  print("there are 31 days in",year,",month",month)
elif month==4 or 6 or 9 or 11:
  print("there are 30 days in year",year,",month",month)
else :
    print("there are 29 days in",year,",month",month)
