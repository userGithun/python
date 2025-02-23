num =list(map(int,input().split()))
#print(num)
sum = num[0]
for i in range(0,len(num)//2):
    sum = sum + int(num[i])
print(sum)


# num = list(map(int,input().split()))
# even,odd = 0, 0
# for i in range  (0,len(num),2):
#     odd+=num[i]
# for i in range (1,len(num),2):
#     even +=num[i]
# print(max(even,odd))    