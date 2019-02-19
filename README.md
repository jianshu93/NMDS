# NMDS
This is a hands-on NMDS function. Two distance metrics are offered (Jaccard and Bray-Curtis). A sample by feature table should be used as input file. This is mandatory. Group file can also be used for grouping purposes but can be omitted.

# usage
In a command line:
`python nmds_.py [-h] [-f DATA_FILE] [-d {Jaccard,BrayCurtis}] [-g GROUP_FILE] `
`python nmds3D.py -h -f DATAFILE -d {Jaccard,BrayCurtis} -g GROUPFILE
`optional arguments:
 -h, --help            show this help message and exit
 -f DATA\_FILE, --file DATA\_FILE         matrix data file. rows are variables, columns are samples.
  -d {Jaccard,BrayCurtis}, --distance\_metric {Jaccard,BrayCurtis}     choose distance metric used for NMDS.
  -g GROUP\_FILE, --grouping\_file GROUP\_FILE       plot samples by same colors and markers when they belong to the same group. Please indicate Tab- separated 'Samples vs. Group file' ( first columns are sample names, second columns are group names ).

The nmds.py function will create a pdf figure using the first 2 axis of nmds. The nmds_3D.py will create a 3D figure using the first 3 axis to nmds.

You can also modified it for your own purposes

