#!/bin/bash
#Thomas Kelley - SecureSet - 2018
#Wed 07 Feb 2018 09:48:44 PM MST
#
#####################################
#
#Replicate ps -aef command manually
#
#####################################

OIFS=$IFS
#move to /proc/ folder
cd /proc/

#get PID# from folders starting w/ numbers and sort
pid_num=$(ls -d [0-9]*)
function sorted { for i in ${pid_num[@]}; do echo "$i"; done | sort -n; }
pid_nums=( $(sorted) )

#get UID using stat
pid_uid=()
for pid in ${pid_nums[@]}; do

	cd /proc/"${pid}"

	uid_name=$(stat -c "%U" .)

	pid_name_3="$(cat status | grep Name:)"
	IFS=: read -r -a pid_name_2 <<< "$pid_name_3"
	pid_name="$(echo -e "${pid_name_2[1]}" | tr -d '[:space:]')"

	ppid_name_3="$(cat status | grep PPid:)"
	IFS=: read -r -a ppid_name_2 <<< "$ppid_name_3"
	ppid_name="$(echo -e "${ppid_name_2[1]}" | tr -d '[:space:]')"
	
	pid_uid+="${uid_name}\t${pid}\t${ppid_name}\t\t${pid_name} \n"
	

done
printf "PID\tPPID\tUID\t\tNAME\n"

#find better way to format output
awk 'print $1 $2 $3 $4'
#printf "${pid_uid[@]}"

IFS=$OIFS
