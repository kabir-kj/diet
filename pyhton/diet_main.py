from tkinter import *
from tkinter import ttk
import pandas as pd
root = Tk()
root.configure(bg="white")
root.title('NutriGenine')


def bmr():

    breakfast = pd.read_csv("breakfast_dataset.csv")   
    lunch = pd.read_csv("lunch_dataset.csv")
    dinner = pd.read_csv("dinner_dataset.csv")
    snacks = pd.read_csv("snacks_dataset.csv")
    beverages = pd.read_csv("beverages_dataset.csv")

    new=Toplevel()

    w = e1.get()
    h = e2.get()
    age = e3.get()
    act = a.get()
    gender = g.get()

    if gender == 'Male':
        cal = int()
        cal = 88.362 + (13.397*float(w)) + (4.799*float(h)) - (5.677*float(age))
    elif gender == 'Female':
        cal = int()
        cal = 447.593 + (9.247*float(w)) + (3.098*float(h)) - (4.330*float(age))
    
    if act == 'Sedentary (little or no exercise)':
        cal = cal*1.2

    elif act == 'Lightly active (1-3 days/week)':
        cal = cal*1.375

    elif act == 'Moderately active (3-5 days/week)':
        cal = cal*1.55

    elif act == 'Very active (6-7 days/week)':
        cal = cal*1.725

    elif act == 'Super active (twice/day)':
        cal = cal*1.9
    
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

    
    #spltiting the total micros (carbs, proteins and fats) for each meal (breakfast, lunch, snack, dinner)
    bk_pr = (protiens_req*30)//100      #breakfast protien requirement(bk_pr) = (protiens required for the complete day)/30%
    bk_cr = (carb_req*30)//100          #breakfast carb requirement
    bk_fr = (fats_req*30)//100          #breakfast fats requirement

    #lunch requirement: 40% of total requiremnts
    ln_pr = (protiens_req*40)//100
    ln_cr= (carb_req*40)//100
    ln_fr = (fats_req*40)//100

    #snacks requirement: 10% of total requiremnts
    sk_pr = (protiens_req*10)//100
    sk_cr = (carb_req*10)//100
    sk_fr = (fats_req*10)//100

    #dinner requirement: 20% of total requiremnts
    dr_pr = (protiens_req*20)//100
    dr_cr = (carb_req*20)//100
    dfr= (fats_req*20)//100
    #print(bk_pr,bk_cr,bk_fr,"------",ln_pr,ln_cr,ln_fr,"------",sk_pr,sk_cr,sk_fr,"------",dr_pr,dr_cr,dfr


    #giving the diet

    #for breakfast
    bkfst= {}             #declaring a dictionary variable= "bkfst" which stores food for breakfast
    for index, row in breakfast.iterrows():
        if int(row["Protein (g)"])==bk_pr:
            bkfst[row["name"]]=row["Serving Weight 1 (g)"]     #to bkfst (dictionary)...this line does the adding part
            bk_fr -= int(row["Fat (g)"])
            bk_cr -= int(row["Carbohydrate (g)"])
            break
    for index, row in breakfast.iterrows():
        if int(row["Fat (g)"]) == bk_fr:
           bkfst[row["name"]]=row["Serving Weight 1 (g)"]
           bk_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in breakfast.iterrows():
        if int(row["Carbohydrate (g)"])== bk_cr:
           bkfst[row["name"]]=row["Serving Weight 1 (g)"]
           break

    #for lunch
    lnch= {}
    for index, row in lunch.iterrows():
        if int(row["Protein (g)"])==ln_pr:
        #print(row["Protein (g)"])
           lnch[row["name"]]=row["Serving Weight 1 (g)"]
           ln_fr -= int(row["Fat (g)"])
           ln_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in lunch.iterrows():
        if int(row["Fat (g)"]) == ln_fr:
           lnch[row["name"]]=row["Serving Weight 1 (g)"]
           ln_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in lunch.iterrows():
        if int(row["Carbohydrate (g)"])== ln_cr:
           lnch[row["name"]]=row["Serving Weight 1 (g)"]
           break

    #for snacks
    snck= {}
    for index, row in snacks.iterrows():
        if int(row["Protein (g)"])==sk_pr:
           #print(row["Protein (g)"])
           snck[row["name"]]=row["Serving Weight 1 (g)"]
           sk_fr -= int(row["Fat (g)"])
           sk_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in snacks.iterrows():
        if int(row["Fat (g)"]) == sk_fr:
           snck[row["name"]]=row["Serving Weight 1 (g)"]
           sk_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in snacks.iterrows():
        if int(row["Carbohydrate (g)"])== sk_cr:
           snck[row["name"]]=row["Serving Weight 1 (g)"]
           break

    #for dinner
    dnnr= {}
    for index, row in dinner.iterrows():
        if int(row["Protein (g)"])==dr_pr:
           #print(row["Protein (g)"])
           dnnr[row["name"]]=row["Serving Weight 1 (g)"]
           dfr -= int(row["Fat (g)"])
           dr_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in dinner.iterrows():
        if int(row["Fat (g)"]) == dfr:
           dnnr[row["name"]]=row["Serving Weight 1 (g)"]
           dr_cr -= int(row["Carbohydrate (g)"])
           break
    for index, row in dinner.iterrows():
        if int(row["Carbohydrate (g)"])== dr_cr:
           dnnr[row["name"]]=row["Serving Weight 1 (g)"]
           break
    #for beverages
    beverage = {}
    one_row = beverages.sample()    #this is to select one row in a beverages dataset 
    for index, row in one_row.iterrows():
        beverage[row["name"]]= "one serving"


    b = []
    for k, v in bkfst.items():
       b.append(k)
       b.append(str(v))
    s = []
    for k, v in snck.items():
       s.append(k)
       s.append(str(v))
    d = []
    for k, v in dnnr.items():
       d.append(k)
       d.append(str(v))
    l = []
    for k, v in lnch.items():
       l.append(k)
       l.append(str(v))
    bv = []
    for k, v in beverage.items():
       bv.append(k)
       bv.append(str(v))


    if len(b)==2:
        fin = StringVar()
        fin.set("Breakfast diet: "+ b[0] +" "+ b[1] + " grams" )
        l6 = Label(new, textvariable=fin, relief=RAISED)
        l6.grid(row=0,column=3, pady=10 )
    elif len(b)==4:
        fin = StringVar()
        fin.set("Breakfast diet: "+ b[0] +" "+ b[1] + " grams and " + b[2] +" "+ b[3] + " grams" )
        l6 = Label(new, textvariable=fin, relief=RAISED)
        l6.grid(row=0,column=3, pady=10 )

    
    if len(l)==2:
        fin2 = StringVar()
        fin2.set("Lunch diet: "+ l[0] +" "+ l[1]+ " grams" )
        l7 = Label(new, textvariable=fin2, relief=RAISED)
        l7.grid(row=1,column=3, pady=10 )
    elif len(l)==4:
        fin2 = StringVar()
        fin2.set("Lunch diet: "+ l[0] +" "+ l[1]+ " grams and "+ l[2] +" "+ l[3] +" grams" )
        l7 = Label(new, textvariable=fin2, relief=RAISED)
        l7.grid(row=1,column=3, pady=10 )

    if len(s)==2:
        fin3 = StringVar()
        fin3.set("Snacks diet: "+ s[0] +" "+ s[1] + " grams" )
        l8 = Label(new, textvariable=fin3, relief=RAISED)
        l8.grid(row=2,column=3, pady=10,padx=10 )
    elif len(s)==4:
        fin3 = StringVar()
        fin3.set("Snacks diet: "+ s[0] +" "+ s[1] + " grams and " + s[2] +" "+ s[3] + " grams" )
        l8 = Label(new, textvariable=fin3, relief=RAISED)
        l8.grid(row=2,column=3, pady=10,padx=10 )

    if len(d)==2:
        fin4 = StringVar()
        fin4.set("Dinner diet: " + d[0] +" "+ d[1] + " grams" )
        l9 = Label(new, textvariable=fin4, relief=RAISED)
        l9.grid(row=3,column=3, pady=10,padx=20 )
    elif len(d)==4:
        fin4 = StringVar()
        fin4.set("Dinner diet: " + d[0] +" "+ d[1] + " grams and " + d[2] +" "+ d[3] + " grams" )
        l9 = Label(new, textvariable=fin4, relief=RAISED)
        l9.grid(row=3,column=3, pady=10,padx=20 )

    fin5 = StringVar()
    fin5.set("Beverage: "+ bv[0] +" "+ bv[1])
    l10 = Label(new, textvariable=fin5, relief=RAISED)
    l10.grid(row=4,column=3,pady=10)
    
    



l1 = Label(root,text = "Weight:",bg="white")
l1.grid(row=0,column=0)
e1= Entry(root)
e1.grid(row=0,column=1)

l2 = Label(root,text = "Height:",bg="white")
l2.grid(row=1,column=0)
e2= Entry(root)
e2.grid(row=1,column=1)

l3 = Label(root,text = "Age:",bg="white")
l3.grid(row=2,column=0)
e3= Entry(root)
e3.grid(row=2,column=1)

l4 = Label(root,text = "Gender:",bg="white")
l4.grid(row=3,column=0)
g= StringVar()
g.set("Female")
b1 = Radiobutton(root,text = "Male", variable = g, value="Male",bg="white")
b1.grid(row=3,column=2)
b2 = Radiobutton(root,text = "Female", variable = g, value="Female",bg="white")
b2.grid(row=3,column=1)

l5 = Label(root,text = "Activity level:",bg="white")
l5.grid(row=4,column=0)
a=StringVar()
a.set("--select your activity level--")
activity = OptionMenu(root,a,"Sedentary (little or no exercise)", 'Lightly active (1-3 days/week)', 'Moderately active (3-5 days/week)', 'Very active (6-7 days/week)', 'Super active (twice/day)')
activity.config(bg="white")
activity.grid(row=4,column=1)

#b1 = ttk.Button(root, text = 'Submit', command = bmr, cursor="dot")
b1 = Button(root, text = 'Submit', command = bmr, cursor="dot",bg="white")
b1.grid(row=5,column=1,pady=10)


root.mainloop()
