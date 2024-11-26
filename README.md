
# MLST Analysis Pipeline

## Overview

This repository provides a pipeline for automating **Multi-Locus Sequence Typing (MLST)** and **gene-based sequence typing** on bacterial genome assemblies in FASTA format. The pipeline integrates two workflows:
1. Whole-genome MLST for sequence type (ST) assignment.
2. Gene-based analysis to determine allele profiles for individual genes.

Results are saved as structured CSV files, suitable for downstream analysis and reporting.



## Features

- **Automated MLST Workflow**:
  - Processes multiple `.fna` files for MLST using an external command-line tool (`mlst`).
  - Extracts key information such as file name, MLST scheme, and sequence type (ST).

- **Gene-Based Typing**:
  - Identifies allele profiles for individual genes based on the MLST output.
  - Dynamically handles genes across schemes with varying allele numbers.

- **CSV Output**:
  - Saves results in tabular CSV format for easy interpretation and further analysis.

- **Error Handling**:
  - Logs errors and unsuccessful runs for better debugging.



## Prerequisites

### Software
1. **Python 3.8+**: Required for running the scripts.
2. **`mlst` Tool**: A command-line tool for performing MLST.

### Python Libraries
Install the required Python libraries using:
```bash
pip install pandas
```



## File Structure

Place your input `.fna` files in the specified directory:
```
input/
├── sample1.fna
├── sample2.fna
└── ...
```

The scripts will output:
- `mlst_results.csv`: MLST results containing file name, scheme, and sequence type.
- `mlst_gene_st_results.csv`: Gene-based results with allele profiles for individual genes.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sananooor/mlst-py.git
   cd mlst-py
   ```

2. Install Python dependencies:
   ```bash
   pip install pandas
   ```

3. Ensure the `mlst` tool is installed and accessible in your system PATH.



## Usage

### 1. Run Whole-Genome MLST
Run the first script for MLST on all `.fna` files:
```bash
python run_mlst.py
```

- **Input**: FASTA files in the `input/` directory.
- **Output**: Results saved as `mlst_results.csv`.

### 2. Run Gene-Based Typing
Run the second script for allele profiling:
```bash
python run_gene_typing.py
```

- **Input**: FASTA files in the `input/` directory.
- **Output**: Results saved as `mlst_gene_st_results.csv`.

---

## Outputs

### MLST Results (`mlst_results.csv`):
| File Name      | Scheme       | Sequence Type |
|----------------|--------------|---------------|
| sample1.fna    | Escherichia  | 20            |
| sample2.fna    | Salmonella   | 15            |

### Gene-Based Typing Results (`mlst_gene_st_results.csv`):
| File Name      | Scheme       | Gene_1 | Gene_2 | Gene_3 | Sequence Type |
|----------------|--------------|--------|--------|--------|---------------|
| sample1.fna    | Escherichia  | 2      | 3      | 7      | 20            |
| sample2.fna    | Salmonella   | 1      | 4      | 6      | 15            |

---

## Notes

- Ensure the `mlst` tool is properly configured and the required MLST database is installed.
- The pipeline assumes the presence of `.fna` files in the `input/` folder.
- For large datasets, consider optimizing the pipeline with parallel execution using Python's `multiprocessing` or `concurrent.futures`.



## Troubleshooting

- **MLST Tool Errors**:
  - Check the installed version of the `mlst` tool.
  - Ensure the database for your target species is configured correctly.

- **Script Errors**:
  - Verify Python dependencies are installed.
  - Ensure the input directory path is correctly set in the script.

---


## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgments

- [PubMLST](https://pubmlst.org/) for the MLST methodology and tools.
- Python libraries used: `pandas`.

