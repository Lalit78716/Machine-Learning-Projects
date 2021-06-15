# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:43:01 2021

@author: Lalit Mali
"""
import pandas as pd
from colorama import Fore,Style

class Download:
    def __init__(self,data):
        self.data=data
    
    def download_file(self):
        #toBeDownload={}
        #for column in self.data.columns.values:
         #   toBeDownload[column]=self.data[column]
        newFileName=input("\nEnter the New modified File name you want (Press -1 to go back)\n")
        
        if newFileName=="-1":
            return
        newFileName=newFileName + ".csv"
        
        new_df=pd.DataFrame(self.data)
        new_df.to_csv(newFileName,index=False)
        
        print(Fore.GREEN + "Successfully Saved modified version of dataset\n")
        print(Style.RESET_ALL)
        
        return