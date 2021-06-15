from data_input import DataInput
from data_description import DataDescription
from imputation import Imputation
from categorical import Categorical
from feature_scaling import FeatureScaling
from download import Download
import os
class Preprocessor:
    tasks=[
        'Menu\n\n',
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Catogorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]
    data=0
    def __init__(self):
        self.data=DataInput().inputFunction()
        #print(self.data)
        print("------------------------------------------------\n")
    
    def printData(self):
        print(self.data)
    #remove target column
    def removeTargetColumn(self):
        print("Target column\n\n")
        for clm in self.data.columns.values:
            print(clm,end="\n")
        while(1):
            column=input("\nWhich column is the target variable you want to choose (Press -1 for Exit)  ").lower()
            if column=="-1":
                print("\033[H\033[J") 
                break;
            choise=input("Are you sure ? (y/n) : ")
            if choise=="y" or choise=="Y":
                try:
                    self.data.drop([column],axis=1,inplace=True)
                except KeyError:
                    print("No column present with this name. Try again....!\n")
                    continue
                print("Done.........................!\n")
                break
            else:
                print("Try again with the correct column name..\n")
        
        #print("\033[H\033[J") 
        return
    def preprocessorMain(self):
        self.removeTargetColumn()
        print("\033[H\033[J")
        while(1):
            for tsk in self.tasks:
                print(tsk)
            while(1):
                try:
                    opt_choice=int(input("\nWhat do you want to do (Press -1 for exit)\n"))
                except ValueError:
                    print("Integer value required. Try again.....!\n")
                    continue
                break
            if opt_choice==-1:
                break
            
            elif opt_choice==1:
                print("\033[H\033[J") 
                DataDescription(self.data).describe()
            
            elif opt_choice==2:
                print("\033[H\033[J") 
                self.data=Imputation(self.data).imputer()
            
            elif opt_choice==3:
                print("\033[H\033[J") 
                self.data=Categorical(self.data).categoricalMain()
            
            elif opt_choice==4:
                print("\033[H\033[J") 
                self.data=FeatureScaling(self.data).scaling()
            
            elif opt_choice==5:
                Download(self.data).download_file()
                if input("Do you want to exit now ? (y/n) : ").lower()=='y':
                    print("Exiting..........!\n")
                    break
                else:
                    continue
            else:
                print("\nWrong Integer value. Try again......!")
                continue
            
            
            
            

obj=Preprocessor()
obj.preprocessorMain()
