#import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
#import ttkwidgets
import csv
import os,sys
from Bio import SeqIO

class Gene:
    def __init__(self,bacteria_name, gene_code, virus_name,gene_name): # constructor for gene class
        self.gene_code = gene_code
        self.virus_name = virus_name
        self.gene_name = gene_name
        self.bacteria_name = bacteria_name


def search_the_db_for_tails(input_bacteria):

    if os.path.isfile('sequence_phages.faa'):
        file_location = 'sequence_phages.faa'
    else:
        file_location = os.path.join(os.path.dirname(sys.executable), 'sequence_phages.faa')
    file = open(file_location)
    line = file.readline()
    ans_lists = []
    while line != '':
        if line[0] == '>':
            gene_data = line.split('|')
            gene_code = gene_data[0][1:gene_data[0].find(' ')]
            virus_name = str.lower(gene_data[0][gene_data[0].find(' ')+1:])
            gene_name = gene_data[1]
            bacteria_name = str.lower(gene_data[2])
            if (input_bacteria == bacteria_name) and ('tail' in gene_name):
                ans_lists.append(gene_code)
            elif (input_bacteria in bacteria_name) and ('tail' in gene_name):
                ans_lists.append(gene_code)
        line = file.readline()
    return ans_lists


my_records = search_the_db_for_tails(input_bacteria ="acinetobacter baumannii")


def find_amino_seq(gene_code):
    if os.path.isfile('sequence_phages.faa'):
       file_location = 'sequence_phages.faa'
    else:
         file_location = os.path.join(os.path.dirname(sys.executable), 'sequence_phages.faa')
    amino_seq = ''
    file = open(file_location)
    found_it = False
    line = file.readline()
    while line != '':
        if line[0] == '>':
            if not found_it:
                gene_data = line.split('|')
                current_gene_code = gene_data[0][1:gene_data[0].find(' ')]
                if current_gene_code == gene_code:
                    found_it = True
            else:
                return amino_seq
        else:
            if found_it:
                amino_seq += line[:-1]
        line = file.readline()
    return amino_seq
#print(my_records[0])
for gene_code in my_records:
    seq = find_amino_seq(gene_code)
    #print(">" + seq)
    with open("filename.fasta", "a+") as file:
        # file.seek(0)
        # seq = file.readline(100)
        # if len(seq) > 0:
        #     file.write("\n")
        file.writelines('>' + seq)
file.close()
#SeqIO.write(seq, "my_example1.faa", "fasta")
