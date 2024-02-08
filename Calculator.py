import tkinter as tk

window = tk.Tk()
window.title("CALCULATOR")
window.configure(background="lightblue")

expression = ""
result = ""

def press(num):

        global expression
        if num =="C":
             expression = ""
        
            
        else:
            expression += str(num)     
            text_input.set(expression)

def equalpress():
         global expression,result

         try:
             result = str(eval(expression))
             text_input.set(result)
             expression = ""

         except ZeroDivisionError:
             text_input.set("error: divison by zero")

         except Exception as e:
             text_input.set(f"error:{e}")

def clear_input():
         text_input.set("")
    
text_input = tk.StringVar()
entry =tk.Entry(window,textvariable=text_input,width=35,borderwidth=5,background="white",font=("sans-serif"))
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10 )             
    

Button_list =[
    "7","8","9","/",
    "6","5","4","*",
    "1","2","3","-",
    "0","00",".","+"       
]   

row = 1
col = 0

for button_text in Button_list:  
    button = tk.Button(
                       window,
                       text=button_text,
                       width=5,
                       background="darkblue",
                       foreground="white",
                       font=("sans-serif"),  
                       command=lambda t=button_text: press(t)
                     )
    
    button.grid(row=row,column=col,padx=5,pady=5)  
    col +=1
    if col>3:
        col=0
        row +=1

equal_button = tk.Button(window,text="=",width=11,background="darkblue",foreground="white",font=("sans-serif"),command=equalpress)
equal_button.grid(row=5,column=2,columnspan=4,padx=5,pady=5)
        

Button_list2 = ["AC"]
row += 1
for button_text in Button_list2:
    button = tk.Button( window,text=button_text,width=5,background="darkblue",foreground="white",font=("sans-serif"),command=clear_input)
    button.grid(row=5,column=0,columnspan=3,padx=5,pady=5)  
    col += 1    
    

window.mainloop()


                       
                   
             