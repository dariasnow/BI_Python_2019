# filter_fastq

filter_fastq is a simple filter for .fastq (.fq) files written on Python 3.

## Installation  
To install filter_fastq download file 'filter_fastq.py' from this repository.  
Be sure you use Python 3.

## Usage
To run filter_fastq type the following command in terminal:  
    ```python3 /path/to/filter_fastq.py -min_length ... [args] -file /path/to/your.fastq```    
    
Arguments:   
     **--min_length** -- minimal read length, integer > 0 (required)  
     **--keep_filtered** -- save failed reads, default: False  
     **--gc_bounds** -- GC-content in %, if you want to point minimal content - point one threshold,
     if you want to point interval - point two thresholds. For example: --gc_content MIN or --gc_content MIN MAX.  
     If no values are pointed all reads will be passed.  
    **-o**, **--output_base_name** -- common name for output file(s), default: base name of input file  
    **-file** -- FASTQ file should be filtered (required)  
    
Examples:  
    ```python3 filter_fastq.py --min_length 100 --gc_bounds 30 60 --keep_filtered -file my_file.fastq```  
    ```python3 filter_fastq.py --min_length 50 --gc_bounds 40 -o filtered_file -file my_file.fastq```  
    
**NB!** Be sure you dont't already have the file named '<output_base_name>__passed.fastq' in your working directory.   

Output files:
- <output_base_name>__passed.fastq -- contains reads passed filtration
- <output_base_name>__failed.fastq -- contains reads failed filtration  

Contact: dariasnow97@gmail.com
    
