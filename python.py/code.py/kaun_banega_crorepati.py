questions=[
    ["what is 2+2","3","6","4","5", 3],
    ["which city is called orange city","jaipur","jodhpur","chennai","nagpur", 4],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],
    ["iran comes in which continent","asia","south america","europe","africa", 1],
    ["iran has stopped which sea path- what that 30 m path called","starit of hamaz","strait of homruz","trade deal of west asia","west asia oil bridge", 2],    
]

limits=[1000,2000,3000,5000,10000,20000,30000,50000,100000,2000000,300000,5000000,10000000,7000000]

i=0
money=0
for i in range(0,len(questions)):
    current_ques= questions[i]
    print(f"your question for rs.{limits[i]} is on the screen")
    print(current_ques[0])
    print(f"a.{current_ques[1]}                                             b.{current_ques[2]}")
    print(f"c.{current_ques[3]}                                             d.{current_ques[4]}")
    
    ans=int(input("enter your answer(1-4) :\n"))
    if(ans==0):  #game quit option 
        money=limits[i-1]
        print("okay! so you quit the game :\n")
        break
    elif(ans==current_ques[-1]):
        print(f"your answer is correct, you won {limits[i]} :\n")

        if(i==4):
            money=limits[i]
    
        elif(i==9):
            money=limits[i]

        elif(i==12):
            money=limits[i]

    else:
        print("WRONG ANSWER!!!!!!")
        break
    

print(f"you take home money rs. {money}")

