import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from data_description import DataDescription
from colorama import Fore,Style


class Categorical:
    
    tasks=[
        "1. Show categorical columns",
        "2. Performing OneHot Encoding",
        "3. Show the Dataset"
        ]
    
    def __init__(self,data):
        self.data=data
    
    # show all categorical columns and the number of unique values in them
    def categoricalColumn(self):
        #print(self.data.nunique())
        count=0
        print("\n{0: <20}".format("Categorical Column") + "{0: <5}".format("Unique values"))
        #select_dtypes selects the columns with object datatype (which could be further categorize)    
        for column in self.data.select_dtypes(include="object"):
            count+=1
            print("{0:<20}".format(column) + "{0: <5}".format(self.data[column].nunique()))
        if count==0:
            print(Fore.RED +"There is no categorical column in dataset\n")
            print(Style.RESET_ALL)

            
    def encoding(self):
        categorical_column=self.data.select_dtypes(include="object")
        print(categorical_column)
        while(1):
            column=input("\nWhich column would you like to one hot encode? (Press -1 to go back)  ").lower()
            if column=="-1":
                print("\033[H\033[J")
                break
            
            if column in categorical_column:
                print(self.data)
                print("\n----------------------------------------------------------------------\n\n")
                self.data = pd.get_dummies(data=self.data,columns=[column])
                print(self.data)
                
                print(Fore.GREEN+"\nEncoding is done...................!\n")
                print(Style.RESET_ALL)
                choice=input("Are there more columns to be encoded(y/n)?")
                if choice=='y' or choice=='Y':
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                print(Fore.RED+"\nWrong Column Name. Try again.....!")
                print(Style.RESET_ALL)
                
    #Main function for categorical class
    def categoricalMain(self):
        while(1):
            print("\nTask\U0001F447")
            for task in self.tasks:
                print(task)
            while(1):
                try:
                    choice = int(input("\nWhat you want to do (Press -1 to go back) : "))
                except ValueError:
                    print("\nInteger value required. Try again.....")
                    continue
                break
            
            if choice==-1:
                print("\033[H\033[J")
                break
            elif choice==1:
                self.categoricalColumn()
            elif choice==2:
                self.categoricalColumn()
                self.encoding()
            elif choice==3:
                print("\033[H\033[J")
                DataDescription.showDataset(self)
            else:
                print("\nWrong Integer Value. Try again......!")
        return self.data
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
                
                
    