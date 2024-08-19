import csv

def student(name,father,mother,age,location,phone):
    
    try:
        if age == 5 or age == 6:
            with open("first.csv","a",newline="",encoding="utf-8") as file:
             writer= csv.writer(file)
             writer.writerow([name ,father,mother,age,location,phone])
        elif age ==  7:
             with open("secon.csv","a",newline="",encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerow([name,father,mother,age,location,phone])
        elif age ==  8:
            with open("third.csv","a",newline="",encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerow([name ,father,mother,age,location,phone])
        elif age ==  9:
            with open("fourth.csv","a",newline="",encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerow([name , father,mother,age,location,phone])
        elif age ==  10:
            with open("fifth.csv","a",newline="",encoding="utf-8") as file :
             writer = csv.writer(file)
             writer.writerow([name , father,mother,age,location,phone])       
        elif age ==  11:
            with open("sixth.csv","a",newline="",encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerow([name , father,mother,age,location,phone ])       
    except:
        pass
def Search_Student(): #يقوم التابع بل البحث عن الطالب
    #إدخال الاسم و العمر
    target_name = input ("Enter the name of student : ")
    age =  int(input("Enter the age : "))
    try:
        #مقارنة العمر 
        if age == 5 or age == 6 :
            with open("first.csv","r",encoding="utf-8")as file :
                reader = csv.reader(file)
                for col in reader:
                    name= col[0] 
                    father= col[1]
                    mother= col[2]
                    age= col[3]
                    location= col[4]
                    phone= col[5]
                    #مقارنة الاسم المدخل مع الاسماء ضمن الملف
                    if target_name== name:
                        print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone}:")
                        break
                else:
                    print("الطالب على العثور يتم لم ")
        elif age == 7 :            
                with open("first.csv","r",encoding="utf-8")as file :
                    reader = csv.reader(file)
                    for col in reader:
                        name= col[0] 
                        father= col[1]
                        mother= col[2]
                        age= col[3]
                        location= col[4]
                        phone= col[5]
                        if target_name== name:
                            print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone} :")
                            break
                        else:
                            print("الطالب على العثور يتم لم ")
        elif age == 8 :            
            with open("third.csv","r",encoding="utf-8")as file :
                reader = csv.reader(file)
                for col in reader:
                    name= col[0] 
                    father= col[1]
                    mother= col[2]
                    age= col[3]
                    location= col[4]
                    phone= col[5]
                    if name == target_name:
                        print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone}:")
                        break
                else:
                    print("الطالب على العثور يتم لم ")
        elif age == 9 :
            with open("fourth.csv","r",encoding="utf-8")as file :
                reader = csv.reader(file)
                for col in reader:
                    name= col[0] 
                    father= col[1]
                    mother= col[2]
                    age= col[3]
                    location= col[4]
                    phone= col[5]
                    if name == target_name:
                        print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone}:")
                        break
                else:
                    print("الطالب على العثور يتم لم ")
        elif age == 10 :
            with open("fifth.csv","r",encoding="utf-8")as file :
                reader = csv.reader(file)
                for col in reader:
                    name= col[0] 
                    father= col[1]
                    mother= col[2]
                    age= col[3]
                    location= col[4]
                    phone= col[5]
                    if name == target_name:
                        print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone}:")
                        break
                else:
                     print("الطالب على العثور يتم لم ")
        elif age == 11 :
            with open("sixth.csv","r",encoding="utf-8")as file :
                reader = csv.reader(file)
                for col in reader:
                    name= col[0] 
                    father= col[1]
                    mother= col[2]
                    age= col[3]
                    location= col[4]
                    phone= col[5]
                    if name == target_name:
                        print (f"الطالب {name}\nاسم الأب {father}\n اسم الأم :{mother} \n العمر : {age} \n السكن : {location} \n رقم الهاتف {phone}:")
                        break
                else:
                     print("الطالب على العثور يتم لم ")
    except:
        pass
def main():
    #name = input ("Enter the name of student : ")
    #father = input("Enter the name of father :")
    #mother = input("Enter the name of mather :")
    #age = int (input("Enter the age of student  : "))
    #location = input("Enter location :")
    #phone = int(input("Enter the number of the phone :"))
    #student(name,father,mother,age,location,phone)
    Search_Student()

if __name__=="__main__":
    main()
