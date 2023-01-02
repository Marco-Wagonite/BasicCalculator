# Phép tính cộng:
def Add(x, y):
    return x + y

# Phép tính trừ:
def Sub(x, y):
    return x - y

# Phép tính nhân:
def Mul(x, y):
    return x * y

# Phép tính chia:
def Div(x, y):
    return x/y

#Phép chia lấy dư:
def Mod(x, y):
    return x%y


while True:
    # Hàm nhập chọn chế độ tính
    print ("---This is just a basic calculator---")
    print ("1. Add")
    print ("2. Sub")
    print ("3. Mul")
    print ("4. Div")
    print ("5. Mod")
    choice = input("Please input your number (1/2/3/4/5): ")
    
    # Ktra xem nếu choice có ở trong sự lựa chọn không
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Input your first number: "))
        num2 = float(input("Input your second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Div(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", Mod(num1, num2))
        
        # Ktra xem nếu người dùng muốn làm thêm phép tính không
        # Người dùng trả lời 'no' thì dừng
        next_calculation = input("Bạn có muốn làm tiếp? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
