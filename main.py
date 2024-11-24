# minn = 999999999999999999999
# def f_in(x):
#     y = ''
#     while x >= 3:
#         y+=str(x%3)
#         x//=3
#     if x>0:
#         # print("hjjkh",x)
#         y += str(x % 3)
#     return y[::-1]
#
# print("123"[-2:])
# # print(f_in(4))
# for n in range(1,1_000_000):
#     y = f_in(n)
#     # print("--->",y)
#     if n % 3 == 0:
#         y+=y[-2:]
#     else:
#         y+=f_in((n%3)*5)
#     if int(y,base=3)>133:
#         minn = min(int(y,base=3),minn)
# print(minn)
# # print(int("0122",base=3))

# import itertools
# import re
# k = 0
# t = 0
# # print(''.join(["4535",'123','123']))
# for i in itertools.product("ГЕПАРД",repeat=5):
#     # print(i)
#     s = ''.join(i)
#
#     if s[0]!="А" and s[-1]=="Е" and s.count("Г")==1:
#         print(s,s[0]!="A", re.fullmatch(r"[^А]...Е",s)!=None)
#         t+=1
#     if re.fullmatch(r"[^А]...Е",s)!=None and s.count("Г")==1:
#         # print(s)
#         k+=1
# print(k,t)

# print("0123"[1:-1])
#
# f = open(r"Копия 09.txt","rt").readlines()
# k = 0
# for i in f:
#     arr = list(map(int,i.split()))
#     arr.sort()
#     if len(set(arr))==len(arr) and 2*(arr[0]+arr[-1])<= 3*(sum(arr[1:-1])):
#         print(arr)
#         k+=1
# print(k)

# for n in range(50, 0, -1):
#     s = '6' * n
#     while "66" in s:
#         s = s.replace("66", '1',1)
#         s = s.replace("11", '2',1)
#         s = s.replace("22", '6',1)
#     # print(n)
#     if s == "21":
#         print(s,n)
# import itertools
# def f(x):
#     return bin(x)[2:].zfill(8)
# print((f(192)+f(168)+f(32)+f(160)).count("1"))
# print(f(255),f(255),f(255),f(240))
# k = 8
# u = 0
# for i in itertools.product([0,1],repeat=4):
#     if (k+sum(i)) % 2==0:
#         print(i)
#         u+=1
# print(u)

g_a = [5]*1600
# f_a = [1]*1300
# for i in range(1500,-1,-1):
#     g_a[i] = g_a[i+1] + g_a[i+2]+1
# print(g_a)
# for i in range(5, 1201):
#     f_a[i] = f_a[i - 1] + f_a[i - 3] + g_a[i - 2]
# print((f_a[1200]+g_a[100])%10_000)
f = open(r"17.txt", "rt").readlines()
k = 0
summ = 0
for i in range(3, len(f)):
    s = list(map(int,sorted(f[i - 3:i])))
    # input()
    if (s[0] ** 2) + (s[1] ** 2) == (s[2] ** 2):
        print(s)
        k += 1
        summ += s[2]
print(summ,k)

# arr = [0]*18
# for i in range(16,-1,-1):
#     arr[i] = arr[i+1]+arr[i+2]+arr[i*2]
# print(arr)
# maxx = -1
# f = open(r"24.txt", "rt").read()
# for i in range(2, len(f)):
#     for j in range(i, 0, -1):
#         if i + j + 2 - (i - j) < maxx:
#             break
#         if f[i - j:i] == f[i + j:i:-1]:
#             print("1",f[i - j:i + j+1],f[i - j:i], f[i + j:i:-1])
#             maxx = max(i + j + 1 - (i - j), maxx)
#         if f[i - j:i + 1] == f[i + j + 1:i:-1]:
#             print("2",f[i - j:i + j + 1+1],f[i - j:i + 1], f[i + j + 1:i:-1])
#             maxx = max(i + j + 2 - (i - j), maxx)
# print(maxx)
# import fnmatch
# for n in range(1_000_000_000-1,100_000_000-1,-1):
#     if fnmatch.fnmatch(str(n),"1*1*1?") and n % 19 == 0 and n % 6 == 0 and n % 2023 == 0:
#         print(n)
# import math
#
#
# def center(klaster):
#     minn = 99999999999999999999999999999999999999999999
#     for star in klaster:
#         summ = 0
#         for star2 in klaster:
#             summ += (((star2[0] - star[0]) ** 2 + (star2[1] - star[1]) ** 2) ** 0.5 * math.fabs(star2[2] - star[2]))
#         if minn > summ:
#             minn = summ
#             xy = star
#     return xy
#
#
# f = open("27_B.txt", 'rt').readlines()[1:]
# arr = [[] for i in range(3)]
# for i in f:
#     xyg = list(map(float, i.replace(',','.').split()))
#     if xyg[0] > 10:
#         arr[0].append(xyg)
#     elif xyg[1] < 6:
#         arr[1].append(xyg)
#     else:
#         arr[2].append(xyg)
# print(arr)
# centroid_arr = []
# for n in arr:
#     centroid_arr.append(center(n))
# maxx = max(centroid_arr,key=lambda x:x[2])
# print(centroid_arr)
# print(maxx)
# print(maxx[0]*1000,maxx[1]*1000)

# import math
#
#
# def center(klaster):
#     minn = 99999999999999999999999999999999999999999999
#     for star in klaster:
#         summ = 0
#         for star2 in klaster:
#             summ += (((star2[0] - star[0]) ** 2 + (star2[1] - star[1]) ** 2) ** 0.5 * math.fabs(star2[2] - star[2]))
#         if minn > summ:
#             minn = summ
#             xy = star
#     return xy
#
#
# f = open("27_A.txt", 'rt').readlines()[1:]
# arr = [[] for i in range(2)]
# for i in f:
#     xyg = list(map(float, i.replace(',','.').split()))
#     if xyg[1] > 15:
#         arr[0].append(xyg)
#     else:
#         arr[1].append(xyg)
# print(arr[0])
# print(arr[1])
# centroid_arr = []
# for n in arr:
#     centroid_arr.append(center(n))
# maxx = max(centroid_arr,key=lambda x:x[2])
# print(centroid_arr)
# print(maxx)
# print(maxx[0]*1000,maxx[1]*1000)

# f = open("26.txt", 'rt')
# f.readline()
# f.readline()
# zayavka = [list(map(int, i.split())) for i in f.readlines()]
# zayavka.sort()
# num = []
#
# for i in range(31):
#     num.append((zayavka[i][1] + 31,i + 1))
# maxx = -1
# for i in range(31, len(zayavka)):
#     # print(num)
#     num.sort()
#     first_a = [i for i in num if i[0] == min(num,key=lambda x:x[0])[0]]
#     # print(first_a,min(num,key=lambda x:x[0]))
#     # if len(first_a)>1:
#     #     input()
#     first = sorted(first_a,key=lambda x:x[1],reverse=True)[0]
#     # print("first-->",first)
#     wait = first[0] - zayavka[i][0]  if zayavka[i][0] - first[0] < 0 else 0
#     num[num.index(first)] = (zayavka[i][1]+31,num[num.index(first)][1])
#     print("wait-->",wait,zayavka[i])
#     maxx = max(wait,maxx)
# print(maxx)

# def f(s):
#     dec = 0
#     for i in range(len(s)):
#         dec += int(s[i])*22**(len(s)-i-1)
#     return dec
#
# for x in range(22):
#     if (f([1,8,x,8,9,9,5,7]) + f([8,0,x,3,3]) + f([5,2,1,x,6])) % 21 == 0:
#         print(x)
#         print(f([1,8,x,8,9,9,5,7]) , f([8,0,x,3,3]) , f([5,2,1,x,6]))
#         print((f([1,8,x,8,9,9,5,7]) + f([8,0,x,3,3]) + f([5,2,1,x,6]))/21)
# a = (int("18389957",base=22)+int("80333",base=22)+int("52136",base=22))
# print(a/21)