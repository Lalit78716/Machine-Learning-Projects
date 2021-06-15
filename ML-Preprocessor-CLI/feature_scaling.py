import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler,StandardScaler

class FeatureScaling:
    
    tasks=[
        "\n1. Perform Normalization (MinMax Scaler)",
        "2. Perform Standardization (Standard Scaler)",
        "3. Show the Dataset"
        ]
    tasks_normalization=[
        "\n1. Normalize a specific Column",
        "2. Normalize the whole Dataset",
        "3. Show the Dataset"
        ]
    tasks_standardization=[
        "\n1. Standardize a specific Column",
        "2. Standardize the whole Dataset",
        "3. Show Dataset"
        ]
    def __init__(self,data):
        self.data=data
    
    #Normalization
    def normalization(self):
        while(1):
            print("----------------------------------\n")
            print("TASKs (Normalization)\n")
            for task in self.tasks_normalization:
                print(task)
            
            while(1):
                try:
                    choice=int(input("\nWhat you want to do? (press -1 to go back) : "))
                except ValueError:
                    print("Integer value required. Try again...!\n")
                    continue
                break
            if choice==-1:
                print("\033[H\033[J")
                break
            #normalization on specific column
            elif choice==1:
                print(self.data.dtypes)
                columns=input("Enter all the column name which you want to normalize (press -1 to go back) \n").lower()
                if columns=="-1":
                    break
                for column in columns.split(" "):
                    try:
                        minValue=self.data[column].min()
                        maxValue=self.data[column].max()
                        self.data[column]=(self.data[column]-minValue)/(maxValue-minValue)
                    except:
                        print("Not possible.....\n")
                print("Done..........!\n")
            
            #normalization on whole dataset
            elif choice==2:
                try:
                    self.data=pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                    print("Done.....!\n")
                except:
                    print("String column are present so Not possible\n")
            
            #Show  dataset
            elif choice==3:
                print("\033[H\033[J")
                DataDescription.showDataset(self)
            
            else:
                print("You passed wrong key!! Try again....!\n")
        return
    
    #Function to perform standardization 
    def standardization(self):
        while(1):
            for task in self.tasks_standardization:
                print(task)
            
            while(1):
                try:
                    choice=int(input("\nWhat you wanr to do? (Press -1 to go back) : "))
                except ValueError:
                    print("Integer value required. Try again....!\n")
                    continue
                break
            if choice==-1:
                print("\033[H\033[J")
                break
            #for specific column
            elif choice==1:
                print(self.data.dtypes)
                columns=input("Enter all columns name which you want to standardize (Press -1 to go back )\n").lower()
                if columns=="-1":
                    break
                for column in columns.split(" "):
                    try:
                        mean=self.data[column].mean()
                        standard_deviation=self.data[column].std()
                        self.data[column]=(self.data[column]-mean)/standard_deviation
                    except:
                        print("\nNot Possible...!")
                print("Done..........!\n")
            
            #for whole dataset
            elif choice==2:
                try:
                    self.data=pd.DataFrame(StandardScaler().fit_transform(self.data))
                    print("Done.........!\n")
                except:
                    print("String columns are present so not possible to standardize whole dataset\n You can try first option \n")
                break
            elif choice==3:
                print("\033[H\033[J")
                DataDescription.showDataset(self)
            else:
                print("You passed wrong Key!! Try again.....!\n")
            
        return
    
    def scaling(self):
        while(1):
            #print("\033[H\033[J")
            print("\nTasks (Feature Scaling)\n")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice=int(input("\nWhat you want to do ? (Press -1 to go back) :  "))
                except ValueError:
                    print("\nInteger value required. Try again...!")
                    continue
                break
            if choice==-1:
                print("\033[H\033[J")
                break
            elif choice==1:
                print("\033[H\033[J")
                self.normalization()
            elif choice==2:
                print("\033[H\033[J")
                self.standardization()
            elif choice==3:
                print("\033[H\033[J")
                DataDescription.showDataset(self)
            else:
                print("\nWrong Integer value . Try again....!")
        return self.data
                
                        
                        
                        
                        
                        
                        
                        
                        