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
    print ("---Đây là máy tính cơ bản---")
    print ("1. Phép tính cộng")
    print ("2. Phép tính trừ")
    print ("3. Phép tính nhân")
    print ("4. Phép tính chia")
    print ("5. Phép tính chia có dư")
    choice = input("Hãy nhập chế độ tính (1/2/3/4/5): ")
    
    # Ktra xem nếu choice có ở trong sự lựa chọn không
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Mời nhập số đầu tiên: "))
        num2 = float(input("Mời nhập số thứ hai: "))

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