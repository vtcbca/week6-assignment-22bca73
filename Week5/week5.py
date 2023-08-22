import csv
with open ('c:\22bca73\python\student.csv','w') as f:
    data=csv.writer(f)
    field=["sid","sname","city","contact"]
    d=[[1,"sweta","bardoli",9925772304],[2,"kisu","baroda",9105677304],[3,"dhvani","vyara",9106577304],[4,"suhani","surat",9016321569],[5,"kuki","bardoli",3216549870]]
    data.writerow(field)
    data.writerows(d)

# writing csv file  using user input
import csv
with open ('c:\22bca73\python\student.csv','a') as f:
    data=csv.writer(f)
    l=[]		
    for i in range(5):
            name=int(input("Enter sid:"))
            sname=input("Enter sname:")
            city=input("Enter city:")
            contact=int(input("Enter contact no:"))
            d=(["sid","sname","city","contact"])
            l.append(d)
    data.writerows(l)	

# reading csv file
import csv
with open ('c:\22bca73\python\student.csv','r',newline='') as f:
    data=csv.reader(f)
    for i in data:
        print(i)
    
