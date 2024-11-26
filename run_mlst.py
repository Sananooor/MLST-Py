import os
import subprocess
import pandas as pd

# Set the path to the folder containing the FASTA files
fasta_folder = '/home/sana/Desktop/crisprcas/Analysis/mlst/mlst-with-assemblies/input'
output_csv = 'mlst_results.csv'

# Create an empty list to store the results
mlst_results = []

# Iterate over all FASTA files in the folder
for fasta_file in os.listdir(fasta_folder):
    if fasta_file.endswith('.fna'):
        fasta_path = os.path.join(fasta_folder, fasta_file)

        # Run the MLST command
        try:
            result = subprocess.run(['mlst', fasta_path], capture_output=True, text=True)

            # If the command was successful, parse the output
            if result.returncode == 0:
                mlst_output = result.stdout.strip()

                # Extract the relevant information (e.g., file name, sequence type)
                parts = mlst_output.split('\t')
                file_name = os.path.basename(fasta_file)
                scheme = parts[1]  # MLST scheme used
                sequence_type = parts[2]  # Sequence type (ST)
                
                # Add the result to the list
                mlst_results.append([file_name, scheme, sequence_type])
            else:
                print(f"MLST failed for {fasta_file}: {result.stderr}")

        except Exception as e:
            print(f"Error running MLST for {fasta_file}: {e}")

# Create a DataFrame from the results
df_mlst = pd.DataFrame(mlst_results, columns=['File Name', 'Scheme', 'Sequence Type'])

# Save the DataFrame as a CSV file
df_mlst.to_csv(output_csv, index=False)

print(f"MLST results saved to {output_csv}")