#萃取百分率計算機
k=float(input("輸入分配常數:"))
solution=float(input("輸入溶液體積:"))
extra=float(input("輸入每次使用萃取液的體積:"))
times=int(input("萃取次數:"))
remain=1
remain_list=[1]
proportion=k/(solution/extra+k)
def one_time(v_remain):
    v_out=proportion*v_remain
    v_remain=v_remain-v_out
    return v_remain
for i in range(times):
    remain=one_time(remain)
    remain_list.append(remain)
for i in range(1,times+1):
    print(f"第{i}次萃取後萃取百分率"
          f"{round((1-remain_list[i])*100,1)}%")
