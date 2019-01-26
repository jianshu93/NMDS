# NMDS
This is a hands-on NMDS function for community ecology. 2 distance metrics are offered. A sample by feature table should be used as input file. This is mandatory. Group file can also be used for grouping purposes but can be omitted.

# usage
In a command line:

python3 nmds.py -f sample-by-feature.txt -g group.txt -d BrayCurtis

This will create a pdf figure using the first 2 axis of nmds. The distance option could be BrayCurtis or Jaccard
