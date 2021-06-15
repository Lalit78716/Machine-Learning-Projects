import pandas as pd

class DataDescription:
    tasks=[
        '1. Describe a specific column',
        '2. Show Properties of each column',
        '3. Show the Dataset'
        ]
    def __init__(self,data):
        self.data=data
    
    #print dataset
    def showDataset(self):
        while(1):
            try:
                rows=int(input("\nHow many rows to print..? (press -1 to go back) = "))
                if rows==-1:
                    break
                if rows <= 0:
                    print("Number of rows must be >0 \n")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Numeric Value is required. Try again....!\n")
                continue
            break
        return
    # print all columns
    def showcolumns(self):
        for column in self.data.columns.values:
            print(column,end="\n")
        
    def describe(self):
        while(1):
            print("\nData Description\n")
            for tsk in self.tasks:
                print(tsk)
            while(1):
                try:
                    choise = int(input("\nWhat you want to do? (Press -1 for exit) : "))
                except ValueError:
                    print("\nInteger Value required. Try again.......!\n")
                    continue
                break
            
            if choise==-1:
                print("\033[H\033[J")
                break
            elif choise==1:
                print("\033[H\033[J")
                self.showcolumns()
                while(1):
                    describeColumn=input("\nWhich column?  ").lower()
                    try:
                        print("\033[H\033[J")
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("No column present with this name. Try again.....!")
                        continue
                    break
            
            elif choise==2:
                print("\033[H\033[J")
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())
                
            elif choise==3:
                print("\033[H\033[J")
                self.showDataset()
            
            else:
                print("\nWrong integer value!! Try again......")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                