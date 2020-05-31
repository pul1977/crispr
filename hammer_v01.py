### Tool for adding hammerhead and hdv ribozymes to sgRNAs
## First 6 bases of the hammerhead ribozyme have to be complementary to the first 6 bases of the sgRNA
# Attachment of cloning overhangs and export of the oligonucleotides into excel

import os
clear = lambda: os.system('clear') #on Linux System
clear()


# Export sequence to excel sheet
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('oligo_hammerhead.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Generated by hammer_v0****pul2020')          # write_string()
worksheet.write(1, 0, '+++ http://www.crispr.de +++')      
worksheet.write(3, 0, 'oligo_name')
worksheet.write(3, 1, 'oligo_sequence')                         


# Version infos
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print("++++++++++ hammer0.1 ++++++++++++++\nReady-to-order oligonucleotides - attachment of hammerhead and hdv ribozymes to CRISPR guide sequences")
print("Ü. Pul 2020 \n##### http//www.crispr.de ##### github: pul1977/crispr")
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print()
print()
print('### Tool for adding hammerhead and hdv ribozymes to sgRNAs')
print('## First 6 bases of the hammerhead ribozyme have to be complementary to the first 6 bases of the sgRNA')
print("# Hammer attaches hammerhead with spacer-complementary 5'-end")
print("# Hammer attaches hdv-ribozyme the 3'-end")
print("# Hammer generates ready-to-order fw_oligonucleotide with users 5'-cloning overhang")
print("# Hammer generates ready-to-order rev_oligonucleotide with users 3'-cloning overhang")
print("# Hammer exports the user named oligonucleotides into an excel sheet")
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print()
print()
print()


#while = True:
# Take spacer sequence and name

print("[1] Sequence of the spacer sequence:")
spacer = input()

length = len(spacer)
print("Length of your spacer sequence: " +str(length)+ " nt.")
if length > 20:
    print('\n!!! Warning! Spacer length is > 20 nt !!!')
elif length < 20:
    print('\n!!! Warning! Spacer length is < 20 nt !!!')
    


print("\n[2] Name of the guide sequence:")
spacer_name = input()

# Define hh complementary region
first_six_bases = spacer[0:6]

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
seq = first_six_bases
reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
hh = "CTGATGAGTCCGTGAGGACGAAACGAGTAAGCTCGTC"
hdv = "GGCCGGCATGGTCCCAGCCTCCTCGCTGGCGCCGGCTGGGCAACATGCTTCGGCATGGCGAATGGGAC"
hh_spacer = reverse_complement+hh+spacer
hh_spacer_hdv = hh_spacer+hdv

reverse_complement_total = "".join(complement.get(base, base) for base in reversed(hh_spacer_hdv))

# Take the 5'-overhang
print("\n[3] Add the sequence of the 5´-cloning overhang:")
five_overhang = input()
forward_oligo = five_overhang+hh_spacer_hdv


# Take the 3'-overhang
print("\n[4] Add the sequence of the 3´-cloning overhang:")
three_overhang = input()
reverse_oligo = three_overhang+reverse_complement_total

# excel sheet


# Some data we want to write to the worksheet.
oligo_seq = (
    [spacer_name+'_fw', forward_oligo],
    [spacer_name+'_rev', reverse_oligo],

)

# Start from the first cell. Rows and columns are zero indexed.

row = 4
col = 0

# Iterate over the data and write it out row by row.
for oligo_name, oligo_sequence in (oligo_seq):
    worksheet.write(row, col,     oligo_name)
    worksheet.write(row, col + 1, oligo_sequence)
    row += 1

workbook.close()

print('')
print('')


currentDirectory = os.getcwd()
print('\n***** Location of the excel file: ' +str(currentDirectory)+ '/oligo_hammerhead.xlsx ******')
print('')
print('')
print('Added oligonucleotides:')
print(spacer_name+'_fw'+ ' 5- ' +forward_oligo+ ' -3')
print(spacer_name+'_rev'+ ' 5- ' +reverse_oligo+ ' -3')
print('\n++++ hammerv0.1 finished ++++')
print('')
print('')
print('')