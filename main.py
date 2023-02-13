import sys
input= sys.stdin.readline
n = int(input())
time = 0
ls = list(map(int,input().split(' ')))
ls.sort()
for i in range(len(ls)):
  time += ls[i]*(len(ls)-i)
print(time)




