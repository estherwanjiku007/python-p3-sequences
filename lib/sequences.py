#!/usr/bin/env python3
fibonacci_seq=[]
def print_fibonacci(n):
    
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        value=print_fibonacci(n-1) +print_fibonacci(n-2)
        #fibonacci_seq[n]=value
    return value
result=print_fibonacci(9)
print(result)
#for n in range(1,10):
  #  print(n ,":",fibonacci(n))
my_list=["a","b","d","d","e"]
my_list[2]="c"
my_list.append("f")
my_list.insert(6,"g")
my_list.insert(1000,"h")
del(my_list[0:2])
my_list.remove("d")
print(my_list)
my_list.pop(0)
my_str="Hello World!"
my_str2=my_str.upper()
my_str3=my_str2.lower()
my_str4=my_str3.capitalize()
my_str5=my_str.title()
for w in my_str:
   print (w)
   my_tuple=(1,2,3,4,5,"Esther")
   print(len(my_tuple))

#Use this to replace the switch statement if you prefer a cleaner approach
   
   def option1():
      return "Option 1 is chosen"
   def option2():
      return "Option 2 is chosen"
   def option3():
      return "Option 3 is chosen"
   def defaultOp():
      return "Def option is chosen"
   
   options={
      1:option1,
      2:option2,
      3:option3
   }
   def swith_case(option):
      return options.get(option,defaultOp)()
   print(swith_case(5))
  
for a in range(4):
   print(a)
#SETS
   my_set={"apple","banana","orange",False,0}
print(my_set)
my_add=my_set.add("Mango")
print(my_add)
