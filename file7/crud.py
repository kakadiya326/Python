# CRUD Operations on Student Records
while True:
    print('1.Add Student 2.Disply 3.Search 4.Delete 5.Edit 6.Sort 7.Exit')
    ch=int(input())
    match ch:
        case 1:
            f=open('crud.txt','a')
            f.write('\n'+input())
            f.close()
        case 2:
            f=open('crud.txt','r')
            s=f.read().split("\n")
            for row in s:
                print(*row.split(","))
            f.close()
        case 3:
            sid=input("Enter Student ID to search : ")
            f=open('crud.txt','r')
            s=f.read().split("\n")
            f.close()
            for row in s:
                if row.split(",")[0]==sid:
                    print(row)
                    break
        case 4:
            sid=input("Enter Student ID to delete : ")
            f=open('crud.txt','r')
            s=f.readlines()
            f.close()
            for i in range(len(s)):
                if s[i].split(",")[0]==sid:
                    del s[i]
                    break
            s[-1]=s[-1].strip()
            f=open('crud.txt','w')
            f.writelines(s)
            f.close()
        case 5:
            sid=input("Enter student ID : ")
            name=input("Enter new name : ")
            f=open('crud.txt','r')
            s=f.readlines()
            f.close()
            for i in range(len(s)):
                row=s[i].split(",")
                if row[0]==sid:
                    row[1]=name
                    s[i]=",".join(row)
                    break
                else:
                    print('Not matched')
                f=open('crud.txt','w')
                f.writelines(s)
                f.close()
        case 6:
            f=open('crud.txt','r')
            l=f.readlines()
            f.close()
            for i in range(len(l)):
                l[i]=l[i].strip().split(",")
            l.sort(key=lambda x:int(x[4]))
            for row in l:
                print(*row)
        case _:
            break