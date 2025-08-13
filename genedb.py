# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 12:10:04 2024

@author: useless.bruh
"""
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re
from Bio import Entrez
from Bio import SeqIO

class genedb:
    
    def __init__(self,root):
        self.root=root
        self.root.title("MINI GENE DATABASE")
        self.root.attributes('-fullscreen',True)
        self.root.configure(background="cyan")
        
        self.accession_id=StringVar()
        self.description=StringVar()
        self.organism=StringVar()
        self.sequence_length=StringVar()
        self.source=StringVar()
        self.gene=StringVar()
        self.cds=StringVar()
        self.introns=StringVar()
        self.exons=StringVar()
        self.division=StringVar()

        self.global_value=[]

        self.searchval=StringVar()
        self.searchopt=StringVar()
        self.ncbisearch=StringVar()

        
        # ======Dataframe======================================================================================
        style=ttk.Style()
        DataFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE,background="cyan")
        DataFrame.place(x=0,y=0,width=1536,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                            font=("times new roman",12,"bold"),text="GENE INFORMATION",background="cyan")
        DataFrameLeft.place(x=-15,y=0,width=870,height=355)
        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                            font=("times new roman",12,"bold"),text="FASTA",background="cyan")
        DataFrameRight.place(x=855,y=0,width=615,height=355)

        # ===========Buttonframe================================================================================
        ButtonFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE,background="teal")
        ButtonFrame.place(x=0,y=400,width=1536,height=74)
        
        ButtonFrame1=Frame(self.root,bd=20,padx=20,relief=RIDGE,background="teal")
        ButtonFrame1.place(x=0,y=474,width=1536,height=74)

        # =======Framedetails===================================================================================
        FrameDetails=Frame(self.root,bd=20,padx=20,relief=RIDGE,background="aqua")
        FrameDetails.place(x=0,y=548,width=1536,height=317)

        # ===============================DataFrame Left==========================================================
      
        lblaccession=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="accession id **",padx=2,pady=3,background="cyan")
        lblaccession.grid(row=0,column=0,sticky=W)
        txtaccession=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.accession_id,width=67,background="powder blue")
        txtaccession.grid(row=0,column=1)

        lbldescription=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="description *",padx=2,pady=3,background="cyan")
        lbldescription.grid(row=1,column=0,sticky=W)
        txtdescription=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.description,width=67,background="powder blue")
        txtdescription.grid(row=1,column=1)

        lblorganism=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="organism *",padx=2,pady=3,background="cyan")
        lblorganism.grid(row=2,column=0,sticky=W)
        txtorganism=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.organism,width=67,background="powder blue")
        txtorganism.grid(row=2,column=1)

        lblsequence_length=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="bp count *",padx=2,pady=3,background="cyan")
        lblsequence_length.grid(row=3,column=0,sticky=W)
        txtsequence_length=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.sequence_length,width=67,background="powder blue")
        txtsequence_length.grid(row=3,column=1)

        lblsource=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="source *",padx=2,pady=3,background="cyan")
        lblsource.grid(row=4,column=0,sticky=W)
        txtsource=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.source,width=67,background="powder blue")
        txtsource.grid(row=4,column=1)

        lblgene=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="gene",padx=2,pady=3,background="cyan")
        lblgene.grid(row=5,column=0,sticky=W)
        txtgene=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.gene,width=67,background="powder blue")
        txtgene.grid(row=5,column=1)

        lblcds=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="cds *",padx=2,pady=3,background="cyan")
        lblcds.grid(row=6,column=0,sticky=W)
        txtcds=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.cds,width=67,background="powder blue")
        txtcds.grid(row=6,column=1)

        lblintrons=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="introns",padx=2,pady=3,background="cyan")
        lblintrons.grid(row=7,column=0,sticky=W)
        txtintrons=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.introns,width=67,background="powder blue")
        txtintrons.grid(row=7,column=1)

        lblexons=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="exons",padx=2,pady=3,background="cyan")
        lblexons.grid(row=8,column=0,sticky=W)
        txtexons=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.exons,width=67,background="powder blue")
        txtexons.grid(row=8,column=1)

        lbldivision=Label(DataFrameLeft,font=("times new roman",14,"bold"),text="division *",padx=2,pady=3,background="cyan")
        lbldivision.grid(row=9,column=0,sticky=W)
        txtdivision=Entry(DataFrameLeft,font=("times new roman",14,"bold"),textvariable=self.division,width=67,background="powder blue")
        txtdivision.grid(row=9,column=1)


        # ===================================DataframeRight====================================

        self.txtfasta=Text(DataFrameRight,font=("Courier New",10),width=52,height=19,padx=2,bg="black",fg="white")
        self.txtfasta.place(x=-20,y=-5,width=595,height=295)
        

        # ===================================ButtonFrame1=====================================
        
        
        btnDNA=Button(DataFrameRight,text="DNA",command=self.dnaclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnDNA.place(x=-20,y=290,width=198)
        
        btnRNA=Button(DataFrameRight,text="RNA",command=self.rnaclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnRNA.place(x=178,y=290,width=198)
        
        btnPROTIEN=Button(DataFrameRight,text="PROTIEN",command=self.protclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnPROTIEN.place(x=376,y=290,width=198)
        
        btnDNA=Button(DataFrameRight,text="SEQUENOMICS",command=self.seqclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnDNA.place(x=-20,y=257,width=198)
        
        btnRNA=Button(DataFrameRight,text="COMLEMENT",command=self.compclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnRNA.place(x=178,y=257,width=198)
        
        btnPROTIEN=Button(DataFrameRight,text="REVERSE COMPLEMENT",command=self.revclk,font=("times new roman",12,"bold"),bg="deepskyblue4",fg="white")
        btnPROTIEN.place(x=376,y=257,width=198)
        
        btnReceipt=Button(ButtonFrame,text="SAVE",command=self.iinsert,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnReceipt.place(x=-20,y=0,width=300)

        btnExit=Button(ButtonFrame,text="UPDATE",command=self.update_data,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnExit.place(x=280,y=0,width=300)

        btnDelete=Button(ButtonFrame,text="DELETE",command=self.iDelete,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnDelete.place(x=580,y=0,width=300)

        btnReset=Button(ButtonFrame,text="RESET",command=self.iReset,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnReset.place(x=880,y=0,width=300)

        btnExit=Button(ButtonFrame,text="EXIT",command=self.iExit,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnExit.place(x=1180,y=0,width=295)
        
        #=========================buttonframe2=======================================================
        
        selsearchopt=ttk.Combobox(ButtonFrame1,textvariable=self.searchopt,state="readonly",
                                                         font=("times new roman",19,"bold"),width=17,foreground="cadetblue4")
        selsearchopt['value']=("accession id","organism","description")
        selsearchopt.place(x=-20,y=0,width=300)
        self.searchopt.set("select option")
        
        txtsrchbar=Entry(ButtonFrame1,font=("times new roman",19,"bold"),textvariable=self.searchval,width=25,background="powder blue")
        txtsrchbar.place(x=280,y=0,width=300)
        
        btnsrch=Button(ButtonFrame1,text="SEARCH FROM SAVED",command=self.fetch_one,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnsrch.place(x=580,y=0,width=300)
        
        txtncbisearch=Entry(ButtonFrame1,font=("times new roman",19,"bold"),textvariable=self.ncbisearch,width=25,background="powder blue")
        txtncbisearch.place(x=880,y=0,width=300)
        
        btnncbisearch=Button(ButtonFrame1,text="SEARCH NCBI",command=self.srchncbi,font=("times new roman",12,"bold"),width=19,bg="deepskyblue4",fg="white")
        btnncbisearch.place(x=1180,y=0,width=295)
        
        # =======Scrollbar=====================================================================================
        
        style=ttk.Style(root)
        style.theme_use("alt")
        style.configure("Treeview", background="cyan4", 
                fieldbackground="cyan4", foreground="white")

        self.gene_table=ttk.Treeview(FrameDetails,column=("accession_id","description","organism","sequence_length","source","gene","cds","introns","exons","division"))
        scroll_x=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL,command=self.gene_table.xview)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(FrameDetails,orient=VERTICAL,command=self.gene_table.yview)
        scroll_y.pack(side=RIGHT,fill=Y)
              
        self.gene_table.heading("accession_id",text="accession_id")
        self.gene_table.heading("description",text="description")
        self.gene_table.heading("organism",text="organism")
        self.gene_table.heading("sequence_length",text="sequence length")
        self.gene_table.heading("source",text="source")
        self.gene_table.heading("gene",text="gene")
        self.gene_table.heading("cds",text="cds")
        self.gene_table.heading("introns",text="introns")
        self.gene_table.heading("exons",text="exons")
        self.gene_table.heading("division",text="divsion")
        

        self.gene_table["show"]="headings"
   
        self.gene_table.column("accession_id",width=150)
        self.gene_table.column("description",width=150)
        self.gene_table.column("organism",width=150)
        self.gene_table.column("sequence_length",width=150)
        self.gene_table.column("source",width=150)
        self.gene_table.column("gene",width=150)
        self.gene_table.column("cds",width=150)
        self.gene_table.column("introns",width=150)
        self.gene_table.column("exons",width=150)
        self.gene_table.column("division",width=150)

        self.gene_table.pack(fill=BOTH,expand=1)
        self.txtfasta.delete("1.0",END)
        self.gene_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    def get_cursor(self,event):
        cursor_row=self.gene_table.focus()
        content=self.gene_table.item(cursor_row)
        row=content["values"]
        self.accession_id.set(row[0])
        self.description.set(row[1])
        self.organism.set(row[2])
        self.sequence_length.set(row[3])
        self.source.set(row[4])
        self.gene.set(row[5])
        self.cds.set(row[6])
        self.introns.set(row[7])
        self.exons.set(row[8])
        self.division.set(row[9])
        self.iFasta()
        self.retall()
        

  # ======================================Function Declaration=============================================

    def iinsert(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        my_cursor.execute("select accession_id from genetable")
        rows=my_cursor.fetchall()
        rows=[item[0] for item in rows]
        
        if self.accession_id.get()=="" or self.description.get()=="" or self.organism.get()=="" or self.sequence_length.get()=="" or self.source.get()=="" or self.cds.get()=="" or self.division.get()=="" or self.txtfasta.get(1.0, "end-1c")=="":
            messagebox.showwarning("EMPTY FIELDS"," all the fields are required having * symbol\n( including FASTA sequence )")
        elif self.accession_id.get() in rows:
            messagebox.showerror("DUPLICATION ! ","ID already exits")
        else:
            RAWseq=self.txtfasta.get(1.0, "end-1c")
            character=">"
            pattern = re.compile(f'.*{re.escape(character)}.*\n')
            NEWseq= re.sub(pattern, '', RAWseq)
            dnaseq=(">original dna\n"+NEWseq)
            my_cursor.execute("insert into genetable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.accession_id.get(),
                                                                                                        self.description.get(),
                                                                                                        self.organism.get(),
                                                                                                        self.sequence_length.get(),
                                                                                                        self.source.get(),
                                                                                                        self.gene.get(),
                                                                                                        self.cds.get(),
                                                                                                        self.introns.get(),
                                                                                                        self.exons.get(),
                                                                                                        self.division.get(),
                                                                                                        dnaseq
                                                                                                      
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success","Record has been inserted")
        conn.close()
            

    def update_data(self):
        self.retall()
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        my_cursor.execute("select accession_id from genetable")
        rows=my_cursor.fetchall()
        rows=[item[0] for item in rows]
        RAWseq=self.txtfasta.get(1.0, "end-1c")
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        NEWseq= re.sub(pattern, '', RAWseq)
        orgnlseqset={'\n','A','T','G','C','N'}
        retseqset=set(NEWseq)
        if retseqset.issubset(orgnlseqset) and ">original dna" in RAWseq:
            dnaseq=(">original dna\n"+NEWseq)
            if self.accession_id.get() not in rows:
                my_cursor.execute("update genetable set description=%s,organism=%s,sequence_length=%s,source=%s,gene=%s,cds=%s,introns=%s,exons=%s,division=%s,fasta=%s  where accession_id=%s",(
                                                                                
                                                                                    
                                                                                                        self.description.get(),
                                                                                                        self.organism.get(),
                                                                                                        self.sequence_length.get(),
                                                                                                        self.source.get(),
                                                                                                        self.gene.get(),
                                                                                                        self.cds.get(),
                                                                                                        self.introns.get(),
                                                                                                        self.exons.get(),
                                                                                                        self.division.get(),
                                                                                                        dnaseq,
                                                                                                        self.accession_id.get()
                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showwarning("WARNING ! ","accession id cannot be changed\n\nupdated without changing gene id")
                self.iReset()
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
                my_cursor=conn.cursor()
                my_cursor.execute("select accession_id from genetable")
                rows=my_cursor.fetchall()
                my_cursor.execute("update genetable set description=%s,organism=%s,sequence_length=%s,source=%s,gene=%s,cds=%s,introns=%s,exons=%s,division=%s,fasta=%s  where accession_id=%s",(
                                                                                
                                                                                    
                                                                                                        self.description.get(),
                                                                                                        self.organism.get(),
                                                                                                        self.sequence_length.get(),
                                                                                                        self.source.get(),
                                                                                                        self.gene.get(),
                                                                                                        self.cds.get(),
                                                                                                        self.introns.get(),
                                                                                                        self.exons.get(),
                                                                                                        self.division.get(),
                                                                                                        dnaseq,
                                                                                                        self.accession_id.get()
                                                                                                     ))
                conn.commit()
                messagebox.showinfo("UPDATE","record has been updated successfully")
                self.fetch_data()
                conn.close()
                self.iReset()
                
            
        else:
            messagebox.showerror("sequence error","sequence does'nt seem to be a DNA sequence\ntry : \n\tclicking on DNA button and update")
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from genetable")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.gene_table.delete(*self.gene_table.get_children())
            for i in rows:
                self.gene_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def fetch_one(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        if self.searchval.get()=="":
            messagebox.showinfo("SEARCHBAR EMPTY","ENTER A VALUE TO SEARCH")
        if self.searchopt.get()=="accession id":
            my_cursor.execute("select * from genetable where accession_id=%s",(self.searchval.get(),))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.gene_table.delete(*self.gene_table.get_children())
                for i in rows:
                    self.gene_table.insert("",END,values=i)
                    conn.commit()
        elif self.searchopt.get()=="organism":
            xget=self.searchval.get()
            pp1="%"+xget;pp2=xget+"%";pp3="%"+xget+"%"
            my_cursor.execute("select * from genetable where organism like %s or organism like %s or organism like %s",(pp3,pp2,pp1))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.gene_table.delete(*self.gene_table.get_children())
                for i in rows:
                    self.gene_table.insert("",END,values=i)
                    conn.commit()            
        elif self.searchopt.get()=="description":
            xget=self.searchval.get()
            pp1="%"+xget;pp2=xget+"%";pp3="%"+xget+"%"
            my_cursor.execute("select * from genetable where description like %s or description like %s or description like %s",(pp3,pp2,pp1))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.gene_table.delete(*self.gene_table.get_children())
                for i in rows:
                    self.gene_table.insert("",END,values=i)
                    conn.commit()             
        else:
            messagebox.showwarning("NO SELECTION","select an option")
        conn.close()
                                                                                           
    
    def iExit(self):
        iExit=messagebox.askyesno("exit","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

    def iDelete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        query="delete from genetable where accession_id=%s"
        value=(self.accession_id.get(),)
        my_cursor.execute(query,value)
                
        conn.commit()
        conn.close()
        self.fetch_data()
        self.iReset() 
        messagebox.showinfo("DELETE","record has been Deleted successfully")
                 
    def iReset(self):
        self.accession_id.set("")
        self.description.set("")
        self.organism.set("")
        self.sequence_length.set("")
        self.source.set("")
        self.gene.set("")
        self.cds.set("")
        self.introns.set("")
        self.exons.set("")
        self.division.set("")
        self.searchval.set("")
        self.txtfasta.delete("1.0",END)
        self.searchopt.set("select option")
        self.fetch_data()
        
    def iFasta(self):
        self.txtfasta.delete("1.0",END)
        conn=mysql.connector.connect(host='localhost',username='root',password='Mymosi@132513',database='biologicaldata')
        my_cursor=conn.cursor()
        my_cursor.execute("select fasta from genetable where accession_id=%s",(self.accession_id.get(),))
        rows=my_cursor.fetchall()
        fasta1 = [item[0] for item in rows]
        fasta2=fasta1[0]
        
        self.txtfasta.insert(END,fasta2)
        conn.close()
        
    
    def transcribe(self,seq):
        RAWseq=seq
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        NEWseq= re.sub(pattern, '', RAWseq)
        if NEWseq=="":
            messagebox.showerror("DETECTION ERROR","NO DNA SEQUENCE DETECTED")
        elif "D"in NEWseq or "E"in NEWseq or "F"in NEWseq or "H"in NEWseq or "I"in NEWseq or "K"in NEWseq or "L"in NEWseq or "M"in NEWseq or "P"in NEWseq or "Q"in NEWseq or "S"in NEWseq or "V"in NEWseq or "W"in NEWseq or "R"in NEWseq or "Y"in NEWseq or "J"in NEWseq or "O"in NEWseq or "X"in NEWseq or "B"in NEWseq or "Z"in NEWseq or any(char.islower() for char in NEWseq)==True or "U"in NEWseq:
            messagebox.showerror("sequence error","sequence does'nt seem to be a DNA sequence\ntry : \n\tclicking on DNA button and update")
        else:
            NEWseq = re.sub('T', 'U', NEWseq)
            rnaseq=(">transcribed rna\n"+NEWseq)
            return(rnaseq)
    
    def translate(self,seq):
        RAWseq=seq
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        NEWseq= re.sub(pattern, '', RAWseq)
        if NEWseq=="":
            messagebox.showerror("DETECTION ERROR","NO RNA SEQUENCE DETECTED")
        elif "D"in NEWseq or "E"in NEWseq or "F"in NEWseq or "H"in NEWseq or "I"in NEWseq or "K"in NEWseq or "L"in NEWseq or "M"in NEWseq or "P"in NEWseq or "Q"in NEWseq or "S"in NEWseq or "V"in NEWseq or "W"in NEWseq or "R"in NEWseq or "Y"in NEWseq or "J"in NEWseq or "O"in NEWseq or "X"in NEWseq or "B"in NEWseq or "Z"in NEWseq or any(char.islower() for char in NEWseq)==True or "T"in NEWseq:
            messagebox.showerror("DETECTION ERROR","DOES'NT SEEM T BE A RNA SEQUENCE\ntry: 1. CHECK THE CASE OF THE SEQUENCE\n     2. CHECK THE NUCLEOTIDE SYMBOLS")
        else:
            codon_to_aa = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L','CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L','AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M','GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V','UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S','CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P','ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T','GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A','UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*','CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q','AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K','GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E','UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W','CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R','AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R','GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
            pattern = re.compile('|'.join(codon_to_aa.keys()))
            NEWseq = pattern.sub(lambda x: codon_to_aa[x.group()], NEWseq)
            protseq=(">translated protien\n"+NEWseq)
            return(protseq)
            
    def complement(self,seq):
        RAWseq=seq
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        NEWseq= re.sub(pattern, '', RAWseq)
        if NEWseq=="":
            messagebox.showerror("DETECTION ERROR","NO FASTA SEQUENCE DETECTED")
        elif "D"in NEWseq or "E"in NEWseq or "F"in NEWseq or "H"in NEWseq or "I"in NEWseq or "K"in NEWseq or "L"in NEWseq or "M"in NEWseq or "P"in NEWseq or "Q"in NEWseq or "S"in NEWseq or "V"in NEWseq or "W"in NEWseq or "R"in NEWseq or "Y"in NEWseq or "J"in NEWseq or "O"in NEWseq or "X"in NEWseq or "B"in NEWseq or "Z"in NEWseq or "U"in NEWseq or any(char.islower() for char in NEWseq)==True:
            messagebox.showerror("DETECTION ERROR","DOES'NT SEEM T BE A NUCLEOTIDE SEQUENCE\ntry: 1. CHECK THE CASE OF THE SEQUENCE\n     2. CHECK THE NUCLEOTIDE SYMBOLS")
        else:
            swap_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
            pattern = re.compile('|'.join(swap_dict.keys()))
            NEWseq = pattern.sub(lambda x: swap_dict[x.group()], NEWseq)
            compseq=(">complement of dna\n"+NEWseq)
            return(compseq)
                
    def revcomp(self,seq):
        RAWseq=seq
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        NEWseq= re.sub(pattern, '', RAWseq)
        NEWseq=NEWseq[::-1]
        if NEWseq=="":
            messagebox.showerror("DETECTION ERROR","NO FASTA SEQUENCE DETECTED")
        elif "D"in NEWseq or "E"in NEWseq or "F"in NEWseq or "H"in NEWseq or "I"in NEWseq or "K"in NEWseq or "L"in NEWseq or "M"in NEWseq or "P"in NEWseq or "Q"in NEWseq or "S"in NEWseq or "V"in NEWseq or "W"in NEWseq or "R"in NEWseq or "Y"in NEWseq or "J"in NEWseq or "O"in NEWseq or "X"in NEWseq or "B"in NEWseq or "Z"in NEWseq or "U"in NEWseq or any(char.islower() for char in NEWseq)==True:
            messagebox.showerror("DETECTION ERROR","DOES'NT SEEM T BE A NUCLEOTIDE SEQUENCE\ntry: CHECK THE CASE OF THE SEQUENCE")
        else:
            swap_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
            pattern = re.compile('|'.join(swap_dict.keys()))
            NEWseq = pattern.sub(lambda x: swap_dict[x.group()], NEWseq)
            revseq=(">reverse complement of dna\n"+NEWseq)
            return(revseq)
        
    def sequenomics(self,dna,prot):
        character=">"
        pattern = re.compile(f'.*{re.escape(character)}.*\n')
        dna= re.sub(pattern, '', dna)   
        prot= re.sub(pattern, '', prot)
        dnalen=len(dna)
        # nucleotide freq
        a_count=dna.count('A')
        t_count=dna.count('T')
        g_count=dna.count('G')
        c_count=dna.count('C')
        gc_count=g_count+c_count
        #gc content
        gc_content=(gc_count/dnalen)*100
        # gc skew
        g_minus_c=g_count-c_count
        gc_skew=g_minus_c/gc_count
        #AA count
        aa_count=len(prot)
        seqret=(f"Nucleotide Frequency:\n A: {a_count:.0f}\n T: {t_count:.0f}\n G: {g_count:.0f}\n C: {c_count:.0f}\n\nGC content: {gc_content:.4f} %\n\nGC skew: {gc_skew:.4f}\n\nAmino Acid Count: {aa_count:.0f}")
        return(seqret)
        
    def retall(self):
        dna=self.txtfasta.get(1.0, "end-1c")
        rna=self.transcribe(dna)
        prot=self.translate(rna)
        comp=self.complement(dna)
        rev=self.revcomp(dna)
        seqnom=self.sequenomics(dna, prot)
        
        self.global_value.clear()
        
        self.global_value.append(dna)
        self.global_value.append(rna)
        self.global_value.append(prot)
        self.global_value.append(comp)
        self.global_value.append(rev)
        self.global_value.append(seqnom)
        
    def get_feature_positions(self,feature_type, features):
        positions = []
        for feature in features:
            if feature.type == feature_type:
                start, end = feature.location.start, feature.location.end
                positions.append((start, end))
        return positions
        
    def retrieve_nucleotide_by_name(self,name):
      try:
        # Connect to NCBI and set your email address
        Entrez.email = "abhijithkrishnag234@gmail.com"  # Replace with your valid email address

        # Search for the sequence using the name
        handle = Entrez.esearch(db="nucleotide", term=name, retmax=2)
        record = Entrez.read(handle)
        id_list = record["IdList"]

        # If no results found, return None
        if not id_list:
          return None

        # Retrieve sequence information for the first ID
        accession_id = id_list[0]
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb")
        record = SeqIO.read(handle, "gb")

        # Create a dictionary with desired information
        info = {
          "accession_id": record.id,
          "description": record.description,
          "organism": record.annotations["organism"],
          "length": len(record.seq),
          "Sequence":record.seq,
          
          "cds_positions" :self.get_feature_positions("CDS", record.features),
          "intron_positions" :self.get_feature_positions("intron", record.features),
          "exon_positions" :self.get_feature_positions("exon", record.features),
          "gene_positions" :self.get_feature_positions("gene", record.features),
          "source" :self.get_feature_positions("source",record.features),
          "division_code" :record.annotations.get("taxonomy")
          
          # Add more information fields as needed
        }

        return info

      except Exception as e:
        x=(f"Error in : {e}")
        messagebox.showerror("error retriving",x)
        return None
    
    def dnaclk(self):
        self.txtfasta.delete("1.0",END)
        dna=self.global_value[0]
        self.txtfasta.insert(END,dna)
        
    def rnaclk(self):
        self.txtfasta.delete("1.0",END)
        rna=self.global_value[1]
        self.txtfasta.insert(END,rna)
    
    def protclk(self):
        self.txtfasta.delete("1.0",END)
        prot=self.global_value[2]
        self.txtfasta.insert(END,prot)
        
    def seqclk(self):
        seqnom=self.global_value[5]
        seq=Tk()
        seq.title("sequenomics")
        seq.geometry("300x350")
        seqframe=Frame(seq,bd=10,padx=10,relief=RIDGE,background="cyan4")
        seqframe.place(x=0,y=0,width=300,height=350)
        lblseq=Label(seqframe,font=("times new roman",14),text=seqnom,background="cyan4")
        lblseq.place(x=40,y=0)
        btnok=Button(seqframe,text="OK",command=seq.destroy,font=("times new roman",12),width=10,bg="deepskyblue4",fg="white")
        btnok.place(x=80,y=280)
        seq.mainloop()
    
    def compclk(self):
        self.txtfasta.delete("1.0",END)
        comp=self.global_value[3]
        self.txtfasta.insert(END,comp)
    
    def revclk(self):
        self.txtfasta.delete("1.0",END)
        rev=self.global_value[4]
        self.txtfasta.insert(END,rev)
    
    def srchncbi(self):
        self.iReset()
        name =   self.ncbisearch.get()
        info = self.retrieve_nucleotide_by_name(name)
        if info:
          addhead=(">original dna\n"+info["Sequence"])
          self.accession_id.set(info["accession_id"])
          self.description.set(info["description"])
          self.organism.set(info["organism"])
          self.sequence_length.set(info["length"])
          self.source.set(info["source"])
          self.gene.set(info["gene_positions"])
          self.cds.set(info["cds_positions"])
          self.introns.set(info["intron_positions"])
          self.exons.set(info["exon_positions"])
          self.division.set(info["division_code"])
          self.txtfasta.insert(END,addhead)
          self.retall()
          self.ncbisearch.set("")
          
        else:
          messagebox.showerror("error","search value invalid")

    
if __name__ == "__main__":
    root=Tk()
    application=genedb(root)
    root.mainloop()