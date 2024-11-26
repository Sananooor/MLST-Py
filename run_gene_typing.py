import os
import subprocess
import pandas as pd

# Folder containing FASTA files
fasta_folder = '/home/sana/Desktop/crisprcas/Analysis/mlst/mlst-with-assemblies/input' # change the path for your input file
output_csv = 'mlst_gene_st_results.csv'

# List to store MLST results for each genome
mlst_gene_results = []

# Run MLST on each FASTA file
for fasta_file in os.listdir(fasta_folder):
    if fasta_file.endswith('.fna'):
        fasta_path = os.path.join(fasta_folder, fasta_file)

        # Run the mlst command to get the gene-based alleles
        result = subprocess.run(['mlst', fasta_path], capture_output=True, text=True)

        # Print the output to inspect its structure
        mlst_output = result.stdout.strip()
        print(f"MLST output for {fasta_file}:")
        print(mlst_output)

        # If the command was successful, parse the output
        if result.returncode == 0:
            # Split the output by tabs
            mlst_output_split = mlst_output.split('\t')
            mlst_gene_results.append(mlst_output_split)
        else:
            print(f"Error running MLST on {fasta_file}: {result.stderr}")

# Find the maximum number of columns (in case some entries have more genes/alleles)
max_columns = max(len(row) for row in mlst_gene_results)

# Generate column names dynamically based on the maximum number of fields
# Assuming the first two fields are 'File Name' and 'Scheme', and the last field is 'Sequence Type'
columns = ['File Name', 'Scheme'] + [f'Gene_{i}' for i in range(1, max_columns - 2)] + ['Sequence Type']

# Pad rows with missing data to ensure all rows have the same number of columns
for row in mlst_gene_results:
    while len(row) < max_columns:
        row.append('')

# Create the DataFrame with dynamically generated columns
df_mlst_genes = pd.DataFrame(mlst_gene_results, columns=columns)

# Save the DataFrame to a CSV file
df_mlst_genes.to_csv(output_csv, index=False)
