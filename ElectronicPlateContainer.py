class Plate:
    arr=[]
    dfct1,dfct2,dfct3,dfct4,dfct5=input("Enter the 5 damages plate no.:-")
    dfct1=int(dfct1)
    dfct2 = int(dfct2)
    dfct3 = int(dfct3)
    dfct4 = int(dfct4)
    dfct5 = int(dfct5)
    c=0
    def putPlate(self):
        ele=int(input("Enter the plate no. which you want to put into the container:-"))
        Plate.arr.append(ele)

    def popPlate(self):
        Plate.arr.pop()

    def totalPlate(self):
        for i in range (len(Plate.arr)):
           Plate.c+=1
        print("Total no. of plate inside the container is",Plate.c)

    def containerPlate(self):
        for i in range(len(Plate.arr)):
            print("Plate which is inside the container are:-",Plate.arr[i])

    def damagedPlate(self):
        for i in range(len(Plate.arr)):
            if(Plate.arr[i]==Plate.dfct1 or Plate.arr[i]==Plate.dfct2 or Plate.arr[i]==Plate.dfct3 or Plate.arr[i]==Plate.dfct4 or Plate.arr[i]==Plate.dfct5 ):
                print("found")
            else:
                print("not found")

obj=Plate()


while(True):
    print("------Electronic Plate Container------")
    print("\nIn the wedding ceromany a order has been booked by the party")
    print("\nNo. of plates ofr the party has been written by the party organiser")
    print("\n There are 5 damaged plate inside the container")
    print("\nHe wants to keep the every plate to be inside the container when the ceromany ended")
    print("\nPress 1. to add plate into the container")
    print("\nPress 2. to take out the plate from the container")
    print("\nPress 3. to count the no. of plate in the container")
    print("\nPress 4. Plate which is inside the container")
    print("\nPress 5. to check the defected plate no. which is in the container")
    choice=int(input("Enter your choice:-"))
    if(choice==1):
        obj.putPlate()
    elif(choice==2):
        obj.popPlate()
    elif(choice==3):
        obj.totalPlate()
    elif(choice==4):
        obj.containerPlate()
    elif(choice==5):
        obj.damagedPlate()
    else:
        exit()


