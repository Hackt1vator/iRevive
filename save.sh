rm -rf ~/.ssh/known_hosts

# Change the current working directory
cd "`dirname "$0"`"

./device/iproxy 4444:44 > /dev/null 2>&1 &


echo "Mounting"
./device/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'mount -o rw,union,update /'
echo "Mounted!"

ACT1=$(./device/sshpass -p alpine ssh -o StrictHostKeyChecking=no root@localhost -p 4444 find /private/var/containers/Data/System -name internal)

ACT2=$(./device/sshpass -p alpine ssh -o StrictHostKeyChecking=no root@localhost -p 4444 find /private/var/containers/Data/System -name activation_records)

echo $ACT1

ACT2=${ACT1%?????????????????}

echo $ACT2 ACT3=$ACT2/Library/internal/data_ark.plist

ACT4=$ACT2/Library/activation_records


./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:$ACT4/activation_record.plist ./Activation/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:$ACT1/data_ark.plist ./Activation/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:/private/var/containers/Data/System/ ./Activation/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:/private/var/mobile/Library/FairPlay/ ./Activation/

./device/sshpass -p alpine scp -rP 4444 -o StrictHostKeyChecking=no root@localhost:/private/var/wireless/Library/Preferences/com.apple.commcenter.device_specific_nobackup.plist/ ./Activation/
