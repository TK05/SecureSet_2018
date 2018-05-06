#!/bin/bash
#Thomas Kelley - SecureSet - 2018
#Tue, Feb 13, 2018 10:30:21 AM
#
#################################
#
# Virtual Box script to automate VBoxManage creation and modifcation
# based on user inputs
#
#################################

#i for count increase
let "i=1"

#log vms created
vmLog=()

function createVM () {
    vmName="${name}${i}"
    VBoxManage createmedium --filename "${vmName}.vdi" --size "${size}"
    VBoxManage createvm --name "${vmName}" --ostype "Linux_64" --register
    VBoxManage storagectl "${vmName}" --name "SATA Controller" --add sata --controller IntelAhci
    VboxManage storageattach "${vmName}" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "${vmName}.vdi"
    VBoxManage storagectl "${vmName}" --name "IDE Controller" --add ide
    VBoxManage storageattach "${vmName}" --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium "${path}"
    VBoxManage modifyvm "${vmName}" --ioapic on
    VBoxManage modifyvm "${vmName}" --boot1 dvd --boot2 disk --boot3 none --boot4 none
    VBoxManage modifyvm "${vmName}" --cpus "${cpus}" --memory "${memory}" --vram 16
    #VBoxManage modifyvm "${vmName}" --nic1 bridged --bridgedadapter1
    VBoxManage startvm "${vmName}" --type headless
    VBoxManage snapshot "${vmName}" take "STARTUP SNAP"
    VBoxManage snapshot "${vmName}" showvminfo "STARTUP SNAP"
    VBoxManage controlvm "${vmName}" poweroff

    vmLog+=(${vmName})
    let "i+=1"
}

function userInputs () {
    while [[ $name == '' ]]; do
        read -p "Name for VM: " name
    done

    read -p "HD Size in MB (default=10000): " size
    size=${size:-10000}

    read -p "# of CPUs <1-4> (default=1): " cpus
    cpus=${cpus:-1}

    read -p "Memory Size in MB (default=1024): " memory
    memory=${memory:-1024}

    read -p "Path to ISO (default is Temple Lite): " path
    
    #PART TO EDIT
    #path to .iso, this example uses a tiny ISO just for example
    defaultPath="E:\VM\TOS_Lite.ISO"
    path=${path:-$defaultPath}

    read -p "How many to create of this type?: " count
    count=${count:-1}

}

userInputs

COUNTER=${count}
while [ $COUNTER -gt 0 ]; do
    createVM
    let "COUNTER-=1"
done

echo "Created: ${vmLog[@]}"

