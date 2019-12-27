def func1(n):
    if n==0 or n==1:
        print(n, end=" ")
        return
    func1(int(n/2))
    func1(n%2)
num=int(input("Enter any decimal number"))
print("binary converted number")
func1(num)
