# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 02:49:30 2020

@author: cirpan
"""

#CASE: BOOK
import tkinter as tk

DEAD = '0'
LIVE = '1'

window = tk.Tk()
window.title('BOOK')
window.geometry('250x250+500+150')
window.minsize(200,200)
window.maxsize(550,550)

A = []
file = open("book.txt", "r")
B = file.readlines() 
for value in B: 
    C = value.rsplit() 
    C = value.rstrip('\n')
    A.append(C)
print(A)

  
  
#Bu satırlar kodun Veri Yapıları dersinin sabit ödevi olması nedeniyle gizlenmiştir.

    
window.mainloop()

#CASE: GLIDER

import tkinter as tk

DEAD = '0'
LIVE = '1'

window = tk.Tk()
window.title('GLIDER')
window.geometry('250x250+500+150')
window.minsize(200,200)
window.maxsize(550,550)

A = []
file2 = open("glider.txt", "r")
B = file2.readlines() 
for value in B: 
    C = value.rsplit() 
    C = value.rstrip('\n')
    A.append(C)
print(A)

  
  
for i in range(0,len(A)):
    for j in range(0,len(A[i])):
       if i >= 1:
          if A[i][j] == LIVE:
             label = tk.Label(window,relief=tk.RAISED,width=1,height=1,bg="black")        
             label.grid(row=i,column=j)  
          elif A[i][j] == DEAD:
             label = tk.Label(window,relief=tk.RAISED,width=1,height=1,bg="white")        
             label.grid(row=i,column=j)


window.mainloop()







        
        

