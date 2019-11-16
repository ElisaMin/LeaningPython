import random;

line="\t--------------------------\t"
print("\t----------猜数字----------\t");
print("请选择模式：\n"+line+"\nA.初级 0-10 \nB.高级 0-100 \nC.自定义")
mode=input()
print(line)
if mode=="A" :
    rn = random.randint(0, 9)
elif mode=="B":
    rn = random.randint(0, 100)
else:
    print("已选择自定义模式，请输入最大值：",end="")
    cn=int(input())
    rn=random.randint(0,cn)
print(line)

print("请输入数字: ",end="")
gn=int(input())
while rn!=gn:
    if gn>rn:
        print("猜大了,请重新输入数字: ",end="")
    elif gn<rn:
        print("猜小了,请重新输入数字: ",end="")
    else:
        print("错误")
    gn=int(input());
rn=str(rn)
print(line)
print("恭喜你答对了,答案是"+rn+"!")

# 完成
