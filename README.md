# 🧬 GENEDB - Mini Gene Database Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![Biopython](https://img.shields.io/badge/Bio-Python-red.svg)
![License](https://img.shields.io/badge/License-Open%20Source-brightgreen.svg)

</div>

A comprehensive desktop application for managing and analyzing genetic sequence data with integration to NCBI databases and local MySQL storage. 🔬✨

## 📋 Overview

**GENEDB** is a Python-based GUI application built with Tkinter that provides researchers and bioinformatics professionals with powerful tools to store, retrieve, and analyze genetic sequences. The application offers both local database management and direct integration with NCBI's nucleotide database for real-time sequence retrieval. 🌟

## ✨ Features

### 🧬 Sequence Management

- 💾 **Local Database Storage**: Store genetic sequences with comprehensive metadata in MySQL database
- 🌐 **NCBI Integration**: Direct search and retrieval from NCBI nucleotide database
- 📄 **FASTA Support**: Full support for FASTA format sequences
- 🏷️ **Metadata Tracking**: Track accession IDs, descriptions, organisms, sequence lengths, sources, genes, CDS, introns, exons, and taxonomic divisions

### 🔬 Sequence Analysis Tools

- 🧬➡️🧬 **DNA to RNA Transcription**: Convert DNA sequences to RNA (T→U substitution)
- 🧬➡️🔗 **RNA to Protein Translation**: Translate RNA sequences to amino acid sequences using standard genetic code
- 🔄 **Complement Generation**: Generate complement strands of DNA sequences
- ↩️ **Reverse Complement**: Generate reverse complement sequences
- 📊 **Sequence Statistics**: Calculate nucleotide frequencies, GC content, GC skew, and amino acid counts

### 🔍 Search and Retrieval

- 🔎 **Local Search**: Search stored sequences by accession ID, organism, or description
- 🌍 **NCBI Search**: Real-time search and import from NCBI nucleotide database
- 🎯 **Flexible Filtering**: Support for partial matches and wildcard searches

### 📊 Data Visualization

- 📋 **Tabular Display**: View all sequences in an organized table format
- 🖥️ **Sequence Viewer**: Dedicated FASTA sequence display with syntax highlighting
- 📈 **Statistics Window**: Popup window displaying detailed sequence analysis

## 🚀 Installation

### 📋 Prerequisites

- 🐍 Python 3.7+
- 🗄️ MySQL Server
- 📦 Required Python packages:

  ```bash
  pip install tkinter mysql-connector-python biopython
  ```

### 🛠️ Database Setup

1. 📥 Install MySQL Server
2. 🏗️ Create a database named `biologicaldata`
3. 📊 Import the provided schema:

   ```sql
   mysql -u root -p biologicaldata < genedata.sql
   ```

4. ⚙️ Update database credentials in `genedb.py` (lines with MySQL connection)

### ▶️ Running the Application

```python
python genedb.py
```

## 📖 Usage

### ➕ Adding New Sequences

1. ✏️ Fill in the required fields (marked with *)
2. 📋 Paste FASTA sequence in the text area
3. 💾 Click "SAVE" to store in local database

### 🌐 Searching NCBI

1. 🔍 Enter search term in the NCBI search box
2. 🔎 Click "SEARCH NCBI" to retrieve and auto-populate fields
3. 💾 Optionally save to local database

### 🧪 Sequence Analysis

1. 👆 Select a sequence from the table or load via search
2. 🔬 Use the analysis buttons:
   - **🧬 DNA**: Display original DNA sequence
   - **🧬 RNA**: Show transcribed RNA
   - **🔗 PROTEIN**: Display translated protein sequence
   - **📊 SEQUENOMICS**: View detailed sequence statistics
   - **🔄 COMPLEMENT**: Show DNA complement
   - **↩️ REVERSE COMPLEMENT**: Show reverse complement

### 🗄️ Local Database Operations

- ✏️ **UPDATE**: Modify existing records
- 🗑️ **DELETE**: Remove sequences from database
- 🔄 **RESET**: Clear all input fields
- 🔍 **SEARCH FROM SAVED**: Search local database

## 📁 File Structure

```text
GENEDB/
├── 🐍 genedb.py                 # Main application file
├── 🔬 ret_seq_ncbi_des.py      # NCBI retrieval utility
├── 🗄️ genedata.sql             # Database schema and sample data
├── 📝 accesion_id.txt          # Example accession IDs for testing
├── 📋 title.txt                # Field reference guide
└── 📖 README.md                # This file
```

## 🗄️ Database Schema

The application uses a MySQL table `genetable` with the following structure:

- 🔑 `accession_id` (VARCHAR(50), PRIMARY KEY)
- 📝 `description` (VARCHAR(300))
- 🦠 `organism` (VARCHAR(100))
- 📏 `sequence_length` (VARCHAR(20))
- 📍 `source` (VARCHAR(50))
- 🧬 `gene` (VARCHAR(300))
- 🔗 `cds` (VARCHAR(300))
- 🧩 `introns` (VARCHAR(300))
- 🧩 `exons` (VARCHAR(300))
- 🏷️ `division` (VARCHAR(1000))
- 📄 `fasta` (VARCHAR(10700))

## 🔄 Example Workflow

1. 🌐 **Import from NCBI**: Search for "AB012236.1" → Auto-populate fields
2. 🧪 **Analyze Sequence**: Click "DNA" → "RNA" → "PROTEIN" to see transformations
3. 📊 **View Statistics**: Click "SEQUENOMICS" for detailed analysis
4. 💾 **Save Locally**: Click "SAVE" to store in local database
5. 🔍 **Search Later**: Use local search to find and reanalyze sequences

## 📋 Requirements

- 🐍 **Python Libraries**: tkinter, mysql-connector-python, biopython, re
- 🗄️ **Database**: MySQL 8.0+
- 🌐 **Network**: Internet connection for NCBI access
- 📧 **Email**: Valid email address for NCBI API access

## ⚙️ Configuration

Update the following in `genedb.py`:

- 🔗 MySQL connection parameters (host, username, password, database)
- 📧 NCBI email address for API access

## ⚠️ Limitations

- 📏 Maximum sequence length: ~10,700 characters (database limit)
- 🔢 NCBI search returns maximum 2 results
- 🌐 Requires internet connection for NCBI features
- 🗄️ Local MySQL server required for data persistence

## 🤝 Contributing

This project is part of a bioinformatics research toolkit. For contributions or issues, please follow standard Python development practices and ensure all database operations are properly tested.

## 📄 License

Created by useless.bruh (February 2024) 👨‍💻

## 🆘 Support

For technical issues:

1. ✅ Verify MySQL connection and database setup
2. 🌐 Check internet connectivity for NCBI features
3. 📦 Ensure all required Python packages are installed
4. ✔️ Validate FASTA sequence format before saving