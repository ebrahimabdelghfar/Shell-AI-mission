#equiphontaic program
def equiphontaic(str1,str2,length):
  condition=False
  counter=0
  index1=0
  for i  in range(length):
    for j in range(length):
      if(str1[i]==str2[j]):
        counter+=1
        break
  if(counter==length):
    print("equaphontics")
  else:
    print("no equaphontics")       

while(True):
    word1=str.lower(input("please enter the first word :"))
    word2=str.lower(input("please enter the seconed word :"))
    length_word_1=len(word1)
    length_word_2=len(word2)
    if (length_word_1==length_word_2):
        equiphontaic(word1,word2,length_word_1)

    else:
        print("not equiphontaic please enter another word")
    choice=str.capitalize(input("enter ""Y"" if you wish to continue or ""N"" to exit :"))
    if(choice=="N"):
      break
    else:
       continue


