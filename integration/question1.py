

input_str=input()
if input_str.isdigit():
    input_num=eval(input_str)
    total=0
    denominator=1
    while input_num>0:
        result=input_num/denominator
        if result==0 or result%2==1:
            input_num-=denominator
            total+=1
        denominator*=2
    print(total)
else:
    raise ValueError
