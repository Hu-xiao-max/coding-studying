def integer(num):
    if num==0:
        return 0
    else:
        num=str(num)
        #print(len(num))
        #print(num[1])
        list=[]
        for i in range(len(num)):
            list.append(num[i])
        print(list)
        roll_num=0
        for i in range(len(list)):
            roll_num+=int(list[i])*10**i
        return roll_num




if __name__=='__main__':
    integer(234)