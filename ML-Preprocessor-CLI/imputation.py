import pandas as pd
from data_description import DataDescription

class Imputation:
    tasks=[
        "1. Show number of Null values",
        "2. Remove Columns",
        "3. Fill Null values (with mean)",
        "4. Fill Null values (with median)",
        "5. Fill Null values (with mode)",
        "6. Show the Dataset"
        ]
    def __init__(self,data):
        self.data=data
    
    def showColumns(self):
        for column in self.data.columns.values:
            print(column,end=" || ")
        return
    
    def printNullValues(self):
        print("\nNull values of each column:")
        for column in self.data.columns.values:
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("\n")
        return
    
    def removeColumn(self):
        self.showColumns()
        while(1):
            columns=input("\nEnter all the name that you want to delete (press -1 for exit)\n").lower()
            if columns=="-1":
                print("\033[H\033[J")
                break
            choice = input("Are you sure?(y/n)  ")
            if choice=='y' or choice=='Y':
                try:
                    self.data.drop(columns.split(" "),axis=1,inplace=True)
                except KeyError:
                    print("\nOne or more columns are not present. Try again.........!")
                    continue
                print("\nDone......!")
                break
            else:
                print("\nNot Deleting.....!")
        return
    
    
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column=="-1":
                print("\033[H\033[J")
                break;
            choice = input("Are you sure?(y/n)  ")
            if choice=='y' or choice=='Y':
                try:
                    self.data[column]=self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("\nColumn is not present. Try again.......!")
                    continue
                except TypeError:
                    #Imputation is only possible on some specific datatypes like int, float etc.
                    print("\nThe Imputation is not possible here....")
                    continue
                print("\nDone...............!")
                break
            else:
                print("\nNot changing.........!")
        return
    
    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column=="-1":
                print("\033[H\033[J")
                break;
            choice = input("Are you sure?(y/n)  ")
            if choice=='y' or choice=='Y':
                try:
                    self.data[column]=self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("\nColumn is not present. Try again.......!")
                    continue
                except TypeError:
                    #Imputation is only possible on some specific datatypes like int, float etc.
                    print("\nThe Imputation is not possible here....")
                    continue
                print("\nDone...............!")
                break
            else:
                print("\nNot changing.........!")
        return
    
    def fillNullWithMod(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column=="-1":
                print("\033[H\033[J")
                break;
            choice = input("Are you sure?(y/n)  ")
            if choice=='y' or choice=='Y':
                try:
                    self.data[column]=self.data[column].fillna(self.data[column].mode()[0])
                except KeyError:
                    print("\nColumn is not present. Try again.......!")
                    continue
                except TypeError:
                    #Imputation is only possible on some specific datatypes like int, float etc.
                    print("\nThe Imputation is not possible here....")
                    continue
                print("\nDone...............!")
                break
            else:
                print("\nNot changing.........!")
        return
    
    #main function for imputation Class ::
    def imputer(self):
        while(1):
            print("\nIMPUTATION TASKS : -\n")
            for tsk in self.tasks:
                print(tsk)
            
            while(1):
                try:
                    choice = int(input("\n What you want to do ? (Press -1 to go back) ::  "))
                except ValueError:
                    print("\nInteger value required. Try again.........")
                    continue
                print("\033[H\033[J")
                break
            if choice==-1:
                print("\033[H\033[J")
                break
            elif choice==1:
                self.printNullValues()
            elif choice==2:
                self.removeColumn()
            elif choice==3:
                self.fillNullWithMean()
            elif choice==4:
                self.fillNullWithMedian()
            elif choice==5:
                self.fillNullWithMod()
            elif choice==6:
                print("\033[H\033[J")
                DataDescription.showDataset(self)
            else:
                print("\nWrong integer value!! Try agian......!")
        return self.data
                
    
    
    
    
    
    
    
    
    
    
    
        
    