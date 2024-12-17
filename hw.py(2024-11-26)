5、編寫一個程式,從4個整數中找出最小的數,並顯示此數。
num1 = int(input("請輸入第一個整數: "))
num2 = int(input("請輸入第二個整數: "))
num3 = int(input("請輸入第三個整數: "))
num4 = int(input("請輸入第四個整數: "))
min_num = min(num1, num2, num3, num4)
print(f"四個數中最小的數是: {min_num}")

10. 從鍵盤輸入10個整數，統計其中正數、負數和零的個數，並在螢幕上輸出
# 初始化計數器
positive_count = 0
negative_count = 0
zero_count = 0

# 循環輸入10個整數
print("請輸入10個整數:")
for i in range(10):
    num = int(input(f"請輸入第 {i+1} 個整數: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# 輸出結果
print("\n輸入結果統計:")
print(f"正數的個數: {positive_count}")
print(f"負數的個數: {negative_count}")
print(f"零的個數: {zero_count}")

6．有一函式當x< 0 時 y=1，當 x>0 時，y=3，當 x=0 時 y=5，程式設計，從鍵盤輸入一個x值，輸出y值。
# 定義函式
def calculate_y(x):
    if x < 0:
        return 1
    elif x > 0:
        return 3
    else:  # x == 0
        return 5

# 從鍵盤輸入 x 值
x = float(input("請輸入 x 的值: "))

# 計算 y 的值
y = calculate_y(x)

# 輸出結果
print(f"當 x = {x} 時，y = {y}")

7．從鍵盤輸入兩個數，求出其最大值（要求使用函式完成求最大值，並在主函式中呼叫該函式）
# 定義求最大值的函式
def find_max(a, b):
    return a if a > b else b

# 主函式
def main():
    # 從鍵盤輸入兩個數
    num1 = float(input("請輸入第一個數: "))
    num2 = float(input("請輸入第二個數: "))
    
    # 呼叫函式求最大值
    max_value = find_max(num1, num2)
    
    # 輸出結果
    print(f"兩個數中最大值是: {max_value}")

# 呼叫主函式
if __name__ == "__main__":
    main()

12. 從鍵盤上輸入10個數，求其平均值。
# 主函式
def main():
    # 初始化總和變數
    total = 0
    
    print("請輸入10個數:")
    
    # 循環輸入10個數
    for i in range(10):
        num = float(input(f"請輸入第 {i+1} 個數: "))
        total += num  # 累加到總和

    # 計算平均值
    average = total / 10
    
    # 輸出平均值
    print(f"這10個數的平均值是: {average}")

# 呼叫主函式
if __name__ == "__main__":
    main()

#13、程式設計序實現求1-1000之間的所有奇數的和並輸出。
def main():
    # 計算 1 到 1000 之間所有奇數的和
    odd_sum = sum(i for i in range(1, 1001) if i % 2 != 0)
    
    # 輸出結果
    print(f"1 到 1000 之間所有奇數的和是: {odd_sum}")

# 呼叫主函式
if __name__ == "__main__":
    main()
