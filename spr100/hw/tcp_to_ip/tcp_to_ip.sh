#!/bin/bash
#Thomas Kelley - SecureSet 2018 
#Sun 04 Feb 2018 05:22:01 PM MST
#
###############################
#
#Bash script to parse data from the /proc/net/tcp file
#and pass individual ip's to nslookup
#
###############################

#build array from /proc/net/tcp
readarray -t -s4  tcpArray <<< "$(cat /proc/net/tcp)"

#splice into local and remote ips/ports
localIPandPort=()
remIPandPort=()

for line in "${tcpArray[@]}"; do
    read -a address <<< "${line}"
    _localIPandPort+=(${address[1]})
    _remIPandPort+=(${address[2]})
done    

#remove duplicates remote and local
eval remIPandPort=($(printf "%q\n" "${_remIPandPort[@]}" | sort -u))
eval localIPandPort=($(printf "%q\n" "${_localIPandPort[@]}" | sort -u))

OIFS="$IFS"
IFS=":"

#list local TCP connections

echo "LOCAL ADDRESS TCP CONNECTIONS"

for line in "${localIPandPort[@]}"; do
    read -a address <<< "${line}"
    
    ip1="$((0x${address[0]:6:2}))"
    ip2="$((0x${address[0]:4:2}))"
    ip3="$((0x${address[0]:2:2}))"
    ip4="$((0x${address[0]:0:2}))"
    port="$((0x${address[1]}))"
    ip="${ip1}.${ip2}.${ip3}.${ip4}"

    echo "${ip}:${port}"
    #echo "LOCAL ADDRESS NSLOOKUP on ${ip}"
    #nslookup $ip

done


#split each ip, little endian, convert to decimal and build ip
#pass each to nslookup
#port can be enabled with nslookup $port $ip

for line in "${remIPandPort[@]}"; do
    read -a address <<< "${line}"

    #localIP+=("${address[0]:6:2}.${address[0]:4:2}.${address[0]:2:2}.${address[0]:0:2}")
    ip1="$((0x${address[0]:6:2}))"
    ip2="$((0x${address[0]:4:2}))"
    ip3="$((0x${address[0]:2:2}))"
    ip4="$((0x${address[0]:0:2}))"
    port="-port=$((0x${address[1]}))"
    ip="${ip1}.${ip2}.${ip3}.${ip4}"

    echo "REMOTE ADDRESS NSLOOKUP on ${ip}"
    nslookup $ip

done

IFS="$OIFS"