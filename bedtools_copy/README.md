# bedtools_copy

A simple implementation of some bedtools functions for BED-files processing in Python 3.

## Usage  
To run bedtools_copy download file "bedtools_copy.py" and type the following code in terminal:  
- to sort or to merge intervals:  
```python3 /path/to/bedtools_copy.py [args] -i /path/to/input_file```  
- to intersect or to subtract intervals:  
```python3 /path/to/bedtools_copy.py [args] -a /path/to/input_file_A -b /path/to/input_file_B ```  
OR  
import functions directly to your own code :)  

Options:   
**-o**, **--output_base_name** -- common name for output file, default: base name of input file  
**--bed6** -- indicates that input file in BED6 format, default: False  
**-i**, **--input** -- input file to be sorted or merged in BED format')  
**--sort** -- sort intervals by chromosome, then by start position and stop position   
**--merge** -- merge intervals  
**--dist** -- maximum distance allowing to merge intervals, default: 0  
**--intersect** -- intersect intervals, returns positions that ARE presented in both files  
**--subtract** -- subtract intervals, returns positions that are NOT presented in the second file  
**-a** -- the first file to intersect/to subtract in BED format, should be sorted and merged before  
**-b** -- the second file to intersect/to subtract in BED format, should be sorted and merged before  

--Other functions in process--
