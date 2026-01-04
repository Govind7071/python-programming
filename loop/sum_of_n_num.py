# def sum(n):
#     sum=0
#     for n in range(1,n+1):
#       sum=sum+n
#     print("sum=",sum)#sum of natural number
# sum(n=int(input("enter a natural number")))





def cal_sum(*number):
   sum=0
   for num in number:
      sum=sum+num
   print("sum=",sum)
cal_sum(3,4)
cal_sum(3,4,5,6)