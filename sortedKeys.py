#Sorting List by giving specific key ID
# [[101, 'Chiranj', 'MCA', 90], [102, 'c2', 'csc', 30], [103, 'c3', 'BCA', 50]]
# [[101, 'Chiranj', 'MCA', 90], [102, 'c2', 'csc', 30], [103, 'c3', 'BCA', 50]]
# [[102, 'c2', 'csc', 30], [103, 'c3', 'BCA', 50], [101, 'Chiranj', 'MCA', 90]]
std=[]
n=int(input())
for i in range(n):
    std.append([int(input("ID : ")),input("Name : "), input("Department : "), int(input("Marks : "))])
print(std)
print(sorted(std))
print(sorted(std,key=lambda x:(x[3],x[2])))