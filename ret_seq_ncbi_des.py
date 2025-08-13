# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:36:02 2024

@author: useless.bruh
"""

from Bio import Entrez, SeqIO

def retrieve_sequence(description):
    Entrez.email = "abhijithkrishnag234@gmail.com"  # Provide your email for NCBI usage

    # Search for the nucleotide sequences using the description
    handle = Entrez.esearch(db="nucleotide", term=description, retmax=1)
    record = Entrez.read(handle)

    if record["Count"] == "0":
        print(f"No sequence found for description: {description}")
        return None

    # Fetch the nucleotide sequence using the accession number
    accession_number = record["IdList"][0]
    handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="gb", retmode="text")
    sequence_record = SeqIO.read(handle, "genbank")
    handle.close()

    return sequence_record

if __name__ == "__main__":
    description = input("Enter the description of the nucleotide sequence: ")
    sequence_record = retrieve_sequence(description)

    if sequence_record:
        print(f"\nSequence Information for {description}:")
        print(f"Accession Number: {sequence_record.id}")
        print(f"Description: {sequence_record.description}")
        print(f"Sequence:\n{sequence_record.seq}")
