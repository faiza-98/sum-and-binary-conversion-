n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))
 #sum of series: 1 + 1/2 + 1/3 + ….. + 1/N
