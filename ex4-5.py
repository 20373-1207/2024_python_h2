
轉義字符
若要在字串中插入非法字符，請使用轉義字符。
轉義字元是一個反斜杠\，後面跟著要插入的字元。
非法字元的一個例子是由雙引號括起來的字串內的雙引號：
轉義字元可讓您在通常不允許的情況下使用雙引號：
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "We are the so-called \"Vikings\" from the\' north.\'"
print(txt)

例子:
如果在雙引號包圍的字串中使用雙引號，則會出現錯誤：
txt = "We are the so-called "Vikings" from the north."
