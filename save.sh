rm -rf ~/.ssh/known_hosts

# Ändere das aktuelle Arbeitsverzeichnis
cd "`dirname "$0"`"

./device/iproxy 4444:44 > /dev/null 2>&1 &

echo "Mounting"
./device/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'mount -o rw,union,update /'
echo "Mounted!"

INTERNAL=$(./device/sshpass -p alpine ssh -o StrictHostKeyChecking=no root@localhost -p 4444 find /private/var/containers/Data/System -name internal)

ACTIVATION_RECORDS=$(./device/sshpass -p alpine ssh -o StrictHostKeyChecking=no root@localhost -p 4444 find /private/var/containers/Data/System -name activation_records)

ACTIVATION_RECORDS=${INTERNAL%?????????????????}

records=$ACTIVATION_RECORDS/Library/activation_records

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:$records/activation_record.plist ./files/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:$INTERNAL/data_ark.plist ./files/


./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:/private/var/mobile/Library/FairPlay/ ./files/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:/private/var/wireless/Library/Preferences/com.apple.commcenter.device_specific_nobackup.plist/ ./files/

