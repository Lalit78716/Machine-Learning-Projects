import pandas as pd
import sys
from os import path

class DataInput:
    supported_file_extension = [
        'csv'
    ]
    
    # function to convert all the column name into lowercase
    def change_to_lower(self,data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()},inplace=True)
        return data
    
    def inputFunction(self):
        try:
            file_name,file_extension = input("Enter the dataset name : ").split(".")
            #print((file_name,file_extension))
            if file_extension == "":
                raise SystemExit("provide the Dataset with extension")
            if file_extension not in self.supported_file_extension:
                raise SystemExit("This file Extension is not supported")
        except IndexError:
            raise SystemExit("Provide the dataset name with Extension")
        
        try:
            data = pd.read_csv(file_name+"."+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit("The file is empty")
        
        except FileNotFoundError:
            raise SystemExit("File doesn't exist")
        
        data=self.change_to_lower(data)
        return data

