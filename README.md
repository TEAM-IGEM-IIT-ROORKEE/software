# IIT_Roorkee_Web_Application
iGEM Indian Institute of Technology Roorkee 2020 - TailScout Web_Application

Basic Instructions for running the codes individually on your systems :

For checking the search_the_db_for_tails(input_bacteria) and find_amino_seq(gene_code) functions of the gene detection code 
First ensure that you have python installed on your system, 
paste the 'sequence_phages.faa' and 'phage_details.csv' files into the directory which has the python script as well
then run the python script with arguments such as search_the_db_for_tails('staphylococcus aureus') or find_amino_seq('YP_009006775.1')
[Can use any of the bacteria from ESKAPE or any gene_code from the phage_details.csv file , just ensure that none of the letter is capital while using the search_the_db_for_tails(input_bacteria) function ]

For running the jpred api on your system using command prompt first install perl on your system 
then go to the directory which has jpredapi file and the seq file as well, 
then type 
'perl jpredapi submit file=filename mode=batch format=fasta email=emailid@domain.com name=my_test_job skipPDB=on'
on the command prompt
Here, 
'name' and 'skipPDB' parameters are optional but you need to provide other parameters 
You will recieve the result on the mentioned email id 

