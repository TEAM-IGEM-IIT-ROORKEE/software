# IIT_Roorkee_Web_Application
## iGEM Indian Institute of Technology Roorkee 2020 - TailScout Web_Application

### Basic Instructions for running the codes individually on your systems :

##### Dependencies:
```
- Python, To install python on your system
```
> - sudo apt install python3.7
```
- Python dependency xmltramp2
```
> - pip install --upgrade pip xmltramp2 requests
```
- Perl, To install perl on your system
```
> - sudo apt-get update
> - sudo apt-get install perl

##### For checking the search_the_db_for_tails(input_bacteria) and find_amino_seq(gene_code) functions of the gene detection code:
```
- Paste the 'sequence_phages.faa' and 'phage_details.csv' files into the directory which has the python script as well
- Run the python script with arguments such as search_the_db_for_tails('staphylococcus aureus') or find_amino_seq('YP_009006775.1')
```
> **Can use any of the bacteria from ESKAPE or any gene_code from the phage_details.csv file**

##### For running Clustal omega MSA API python code:
```
- In order to run the MSA, input sequence fasta file and clustalo.py script should be in the same directory.
- Next, after running the script, the result files are stored in the same direcotry.
- Last,to run the script following example should be used on terminal or cmd:
```
> python clustalo.py --email <your@email.com> --sequence <sequence_file_name.fasta>

##### For running the jpred api on your system using command prompt: 
``` 
- Next, go to the directory which has jpredapi file and the seq file as well
- Then type 'perl jpredapi submit file=filename mode=batch format=fasta email=emailid@domain.com name=my_test_job skipPDB=on'
on the command prompt.
```
> **Here, 'name' and 'skipPDB' parameters are optional but you need to provide other parameters,
you will recieve the result on the mentioned email id**

> - **For creating the database files such as phage_setails.csv and sequence_phages.faa we used NCBI(National Center for Biotechnology Information) and Genomenet virushostdb databases.**
> - **If you also want to make your own set of database files you can take them from these or similar databases.**



