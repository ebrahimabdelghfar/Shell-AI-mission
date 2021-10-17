#made by Ebrahim Abdelghfar
#made by python 3.9.7
# modified bubble sorting
def cmp(a, b):
    return (a >= b) - (a <= b)

def modified_sorting(list,length_of_list): #comprison and swap function of the array
    Counter_1 =0
    for i in range(length_of_list):
        temp=list
        for j in range (length_of_list-2):
            if(list[j]>=list[j+2]):
               list[j],list[j+2]=list[j+2],list[j]
            elif(j==(length_of_list-2)):
                if(list[j]>=list[j+1]):
                    list[j],list[j+2]=list[j+2],list[j]
                    break
            else:
                continue
        Counter_1+=1
        print(Counter_1)
        if(cmp(list,temp)==1):  #this condition is to decrease complexity of algorithms by break the un necessary loop
            break
        else:
            continue #continue the loop when the next loop is nessesary
    
                
                    
            
while(True):
    array=[]#defining array
    list_length=int(input("please enter the number of items you will add :"))
    for i in range (list_length):
        array.append(float(input("the item with index ("+str(i)+") =")))
    print("the list you enter ="+str(array))
    modified_sorting(array,list_length)
    print("the list after sorting="+str(array))
    choice=str.capitalize(input("enter ""Y"" if you wish to continue or ""N"" to exit :"))
    if(choice=="N"):
      break
    else:
       continue