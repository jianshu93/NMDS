# NMDS
This is a hands-on NMDS function for community ecology. 2 distance metrics are offered. A sample by feature table should be used as input file. This is mandatory. Group file can also be used for grouping purposes but can be omitted.

# usage
In a command line:
```nmds.py [-h] [-f DATA_FILE] [-d {Jaccard,BrayCurtis}] [-g GROUP_FILE]```
optional arguments:
 -h, --help            show this help message and exit`
` -f DATA_FILE, --file DATA_FILE         matrix data file. rows are variables, columns are samples.
  -d {Jaccard,BrayCurtis}, --distance_metric {Jaccard,BrayCurtis}     choose distance metric used for PCoA.
  -g GROUP_FILE, --grouping_file GROUP_FILE       plot samples by same colors and markers when they belong to the same group. Please indicate Tab- separated 'Samples vs. Group file' ( first columns are sample names, second columns are group names ).

This will create a pdf figure using the first 2 axis of nmds. 