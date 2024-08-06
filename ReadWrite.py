# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:49:53 2024

@author: Austin
"""
import csv
import os

def read_file(filename='VideoList.csv'):
    """
    Reads a csv file and turns it into a video list. Defaults to VideoList.csv 
    unless otherwise stated.

    """
    video_list = []
    try:
        with open(filename, 'r', newline='') as reg_file_reader:
            csv_file_reader = csv.reader(reg_file_reader)
            for row in csv_file_reader:
                if row:
                    video_list.append(row)
        return video_list
    
    except FileNotFoundError:
        print("File not found.")
        
    
def write_file(collection, filename='VideoList.csv'):
    """
    Writes the inputted collection to a csv file. Defaults to VideoList.csv unless
    otherwise stated.

    """
    try:    
    
        file_exists = os.path.exists(filename)
        
            
        with open(filename, 'w', newline='') as reg_file_writer:
            csv_file_writer = csv.writer(reg_file_writer)
            csv_file_writer.writerows(collection)
            
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")