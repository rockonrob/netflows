# Network flows data analysis

Repo to share scripts and analysis for a PIC project at UIUC.

## First data set

The programs scripts/load_traces.ch and scripts/extract_flows.sh (executed
in that order) will emit a CSV file of network flows, about 14M records
in total.

The public dataset at
[Simple Web wiki](http://www.simpleweb.org/wiki/Labeled_Dataset_for_Intrusion_Detection).
is a MySQL dump. The scripts assume that a MySQL server is running locally
and the default user has "create database" privileges.
