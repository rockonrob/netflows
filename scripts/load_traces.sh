#!/bin/sh

# set up the home MySQL user first with all privileges

wget https://traces.simpleweb.org/traces/netflow/netflow2/tracelabel_public.sql.gz

mysql -e "create database traces" 
zcat tracelabel_public.sql.gz |mysql traces

