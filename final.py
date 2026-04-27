
# stu = {"index": 0 , "name": "Kanav Aneja ", "total_marks":{"maths":80, "phy":80, "chem":80 },
#      "avg_marks": 360 , "result" : "pass"}


def input_data(name):

    maths = int(input("maths: "))
    phy = int(input("phy: "))
    chem = int(input("chem: "))
    total = maths + phy + chem 
    global i 
    i+=1 
    avg = (maths+phy+chem)/3 
    if avg>=33:
          idk = "passed"
    else:
          idk = "failed"
          
          
    name={"name":name, "sub":{"maths": maths ,"phy": phy , "chem": chem}, "avg":avg , "result":idk,"index":i , "total":total}
    students.append(name)
    

    
    
    
def list_students():
      for k in students:
        print(f"{k["index"]}.{k["name"]}")
               
def list_marks():
    for k in students:
        print(f'''
               Maths: {k["total"]["maths"]})
               Chem:  {k["total"]["chem"]})
               Phy:   {k["total"]["phy"]}''')
        
def total_avg_result(x):
    
    if x == 0:
        for k in students:
            print(f" {k["name"]} : {k["total"]}")
        
   
    if x==1:
      
      for k in students:
          
            print(f"Avg Marks of {k["name"]} is {k["avg"]}")
            
    if x==2:
        
      for k in students:
          print(f"{k["name"]} :  {k["result"]} (with {k["avg"]} marks) ")
         
def high_low():
    high = 0 
    low = 1000
    for k in students:
        if k["total"] > high:
            high = k["total"]
            ans = f" Highest : {k["name"]} : {high} marks"
        if k["total"] < low:
            low = k["total"]
            ans1 = f"Lowest : {k["name"]} : {low} marks"
    print(ans)
    print(ans1)
    
    # kanav king is the author of this repo
def grade_card(x):
    
 for k in students:
  if x == k["name"]:
      print(f''' 
                Grade Card 
             ----------------
             Name   : {k["name"]}
             maths  : {k["sub"]["maths"]}
             phy    : {k["sub"]["phy"]}
             chem   : {k["sub"]["chem"]}
             Total  : {k["total"]}
             Avg    : {k["avg"]}
             Result : {k["result"]}
             
             ''')
    
def ranking():
    list_temp = []
    sorted = [ ]
    for k in students: 
        b = {f"{k["name"]}": k["total"] }
        list_temp.append(b)
        
students=[]
i = 0 

choice = int(input("To get going enter 1 .....\n"))

while choice in range(0,9):
    
 if choice == 0 :
     print("Thanks for using Student Grade Management System........")
     break

 if choice ==1:
    sub_choice=int(input("Enter 1 to start entering a student data  "))
      
    while sub_choice!= 0 : 
       if sub_choice==1:
        name= input("Enter Name: ")
        input_data(name)
     
       if sub_choice == 2:
          pass
        
               
       sub_choice=int(input('''  
                            Enter 1 to keep entering more students data
                            Enter 0 to go to previous menu......'''))
       
 if choice==2:
    list_students()
    
 if choice == 3 :
    total_avg_result(0)
    
 if choice==4:
    total_avg_result(1)
    
 if choice==5:
     total_avg_result(2)
     
 if choice ==6:
     high_low()
     
 if choice==7:
     x = input("Enter Name: ")
     grade_card(x)
    
 if choice == 8 :
     ranking()
     
     
        
 choice=int(input('''
                    Enter 1 to start entering a student data
                    Enter 2 to see list of students
                    Enter 3 to see total marks 
                    Enter 4 to see avg marks
                    Enter 5 to see pass/fail status
                    Enter 6 to see highest and lowest marks 
                    Enter 7 to Generate Individual Grade Cards
                    
                    Enter 0 to exit the program
                    \n
                    '''))
    
    
    

        
        
        
        
    