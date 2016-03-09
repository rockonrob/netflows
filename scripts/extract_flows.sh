#!/bin/sh

DB="traces"
TABLE="flows"
DATAPATH="$HOME/data/netflows"
DEST="$DATAPATH/$TABLE.csv"

mkdir -p $DATAPATH
HEADER="src_ip,dst_ip,packets,octets,start_ts,end_ts,src_port,dst_port,tcp_flags,prot"
echo $HEADER > "$DATAPATH/$TABLE.cols.txt"

SELECT_COLS="src_ip, dst_ip, packets, octets,\
 concat(start_time, '.', start_msec),\
 concat(end_time, '.', end_msec),\
 src_port, dst_port, tcp_flags, prot"

RECORD_COUNT=$(mysql -D $DB -N -e "select count(*) from $TABLE")
echo "extracting $RECORD_COUNT records"
mysql -D $DB -N -e "select $SELECT_COLS from $TABLE" > $DEST
echo "check: $(wc -l $DEST)"
