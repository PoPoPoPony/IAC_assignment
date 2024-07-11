try:
    c1_x=float(input("請輸入第一個圓的x : "))
    c1_y=float(input("請輸入第一個圓的y : "))
    c1_r=float(input("請輸入第一個圓的r : "))
    c2_x=float(input("請輸入第二個圓的x : "))
    c2_y=float(input("請輸入第二個圓的y : "))
    c2_r=float(input("請輸入第二個圓的r : "))
except ValueError as e:
    raise e

if any(r<=0 for r in (c1_r, c2_r)):
    raise ValueError("半徑應大於0")

distance=((c1_x-c2_x)**2+(c1_y-c2_y)**2)**0.5
if distance>c1_r+c2_r:
    print("無相交")
elif distance==c1_r+c2_r:
    print("重疊")
elif distance<c1_r+c2_r:
    if distance+c2_r<=c1_r:
        print("內部")
    else:
        # 題目的情況分為 第二個圓在第一個圓內部/兩圓重疊/兩圓無相交，
        # 因此，第一個圓在第二個圓內部的情況應屬兩圓重疊
        print("重疊")
