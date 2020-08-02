from tkinter import *
import tkinter.messagebox as mb
import mysql.connector as mysql
from tkinter import ttk


def elogin() :
    


    

    def main_login():
        name = ename.get()
        password= epassword.get()

        if ( password =="" or name == "" ) :
            mb.showinfo("insert status" , "All fields are required")
            window1.destroy()

        elif ( name=="jishnu" and password== "8129290529"):
            
          

            if (name=="jishnu"):
                
            ##################################

            #page 3
                def eupdate(rud1) :

                    tv.delete(*tv.get_children())
                    for i in rud1 :
                        tv.insert('', 'end' , values=i)


                def update() :
                    

                    #######################################


                    #page 4


                    def update1() :
                        ename = name.get()
                        etotal = total.get()
                        

                        
                
                        con = mysql.connect(host="localhost" , user="root" ,password="root",database="kochikuri")
                        cursor = con.cursor()
                        cursor.execute("update user set balance='"+etotal+"' where uname='"+ename+"' ")
                        con.commit()
                        con.close()
                        window3.destroy()

                        
                        
                    def update2() :
                        ename = name.get()
                        epending = pending.get()


                        
                        con = mysql.connect(host="localhost" , user="root" ,password="root",database="kochikuri")
                        cursor = con.cursor()
                        cursor.execute("update user set pending='"+epending+"' where uname='"+ename+"' ")
                        con.commit()
                        con.close()
                        window3.destroy()
                        
                    def update3() :
                        ename = name.get()
                        efine = fine.get()


                        con = mysql.connect(host="localhost" , user="root" ,password="root",database="kochikuri")
                        cursor = con.cursor()
                        cursor.execute("update user set fine='"+efine+"' where uname='"+ename+"' ")
                        con.commit()
                        con.close()
                        window3.destroy()
                        
                    def update4() :
                        ename = name.get()
                        etotal = total.get()
                        epending = pending.get()
                        efine = fine.get()

                        
                        
                        con = mysql.connect(host="localhost" , user="root" ,password="root",database="kochikuri")
                        cursor = con.cursor()
                        cursor.execute("update user set balance='"+etotal+"' , pending ='"+epending+"' , fine='"+efine+"'  where uname='"+ename+"' ")
                        con.commit()
                        con.close()
                        window3.destroy()

                        
                        

                    window3=Tk()
                    window3.geometry("900x600")
                    window3.title("kochikuri")
                    id=Label(window3,text="KOCHI KURI ..." , font=("Georgia",50) ,fg="#22A471" )
                    id.place(x=220,y=150)


                    name=Label(window3,text="NAME   :")
                    name.place(x=80,y=300)


                    total=Label(window3,text="TOTAL AMOUNT       :")
                    total.place(x=280,y=300)
                
    
                    pending=Label(window3,text="PENDING          :")
                    pending.place(x=280,y=360)


                    fine=Label(window3,text="FINE           :")
                    fine.place(x=280,y=420)
   
                    name=Entry(window3)
                    name.place(x=150 , y=300)

                    total=Entry(window3)
                    total.place(x=410 , y=300)
    
    
                    pending=Entry(window3)
                    pending.place(x=410 , y=360)



                    fine=Entry(window3)
                    fine.place(x=410 , y=420)


                    update1=Button(window3,text="  UPDATE   " ,bg="white" , command=update1)
                    update1.place(x=580,y=300)

                    update2=Button(window3,text="  UPDATE   " ,bg="white" , command=update2)
                    update2.place(x=580,y=360)

                    update3=Button(window3,text="  UPDATE   " ,bg="white" , command=update3)
                    update3.place(x=580,y=420)

                    


                    
                    update4=Button(window3,text="  CONFIRM UPDATE   " ,bg="white" , command=update4)
                    update4.place(x=500,y=480)

                    
                    window3.mainloop()
                                    
                    #########################################
            

                def refresh():
                    
                    con = mysql.connect(host="localhost" , user="root" ,password="root",database="kochikuri")
                    cursor = con.cursor()
                    cursor.execute("select * from user  ")
                    rud1=cursor.fetchall()
                    eupdate(rud1)
                    con.close()
                    
 
                    
                window2=Tk()
                window2.state('zoomed')
                window2.geometry("900x700")
                window2.title("kochikuri")
                window1.destroy()

                tv = ttk.Treeview(window2, columns=(1,2,3,4,5,6,7) , show= "headings",height="14")

                tv.pack()


                tv.heading(1 , text ="NAME")
                tv.heading(2 , text ="GMAIL")
                tv.heading(3 , text ="PASSWORD")
                tv.heading(4 , text ="PHONE")
                tv.heading(5 , text ="BALANCE")
                tv.heading(6 , text ="PENDING")
                tv.heading(7 , text ="FINE")

                refresh()
                


                refresh=Button(window2,text=" REFRESH  " ,bg="white" ,command=refresh)
                refresh.place(x=360,y=390)


                update=Button(window2,text=" UPDATE  " ,bg="white" ,command=update)
                update.place(x=470,y=390)

                exits=Button(window2,text="  LOGOUT   " ,bg="white" , command=window2.destroy)
                exits.place(x=580,y=390)



            
                window2.mainloop()

                

               
              
    






          
            #########################
        
        else :
            print("fail")
            mb.showinfo("login","   login failed ...   try again")
        
            epassword.delete(0,'end')
            ename.delete(0, 'end')
    
            window1.destroy()

# 2nd  window 
    window1=Tk()
    window1.geometry("600x600")
    window1.title("kochikuri")


    id=Label(window1,text="KOCHI KURI ..." , font=("Georgia",50) ,fg="#22A471" )
    id.place(x=80,y=150)


    name=Label(window1,text="NAME              :")
    name.place(x=150,y=300)
    
    
    password=Label(window1,text="PASSWORD     :")
    password.place(x=150,y=340)
   


    ename=Entry(window1)
    ename.place(x=260 , y=300)
    
    
    epassword=Entry(window1)
    epassword.place(x=260 , y=340)
    


    login=Button(window1,text=" LOGIN  " ,bg="white",command=main_login)
    login.place(x=320,y=390)

    window1.mainloop()
    

 

    
    





#main window


window=Tk()
window.state('zoomed')
window.geometry("900x700")
window.title("kochikuri")

id=Label(window,text="Welcome" , font=("Georgia",30) ,fg="#51AD88" )
id.place(x=10,y=10)

id=Label(window,text="KOCHI KURI ..." , font=("Georgia",50) ,fg="#22A471" )
id.place(x=300,y=300)


login=Button(window,text="LOGIN HERE..." ,bg="white" ,command= elogin)
login.place(x=800,y=350)

window.mainloop()
