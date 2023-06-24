#!/bin/bash

rm -rf ~/.ssh/known_hosts

cd "$(dirname "$0")" || exit

run_ssh_command() {
  ./device/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost -p2222 "$@"
}

copy_files() {
  ./device/sshpass -p 'alpine' scp -rP 2222 -o StrictHostKeyChecking=no root@localhost:"$1" "$2"
}

./device/iproxy 2222:22 > /dev/null 2>&1 &

echo "Mounting"
if ! run_ssh_command 'mount_filesystems'; then
  osascript -e 'display dialog "Error: Failed to mount filesystems" with title "Error"'
fi
echo "Mounted!"

if ! copy_files "/mnt2/mobile/Media/1/files/activation_record.plist" ./files/; then
  osascript -e 'display dialog "Error: Failed to copy activation_record.plist" with title "Error"'
fi

if ! copy_files "/mnt2/root/Library/Lockdown/data_ark.plist" ./files/; then
  osascript -e 'display dialog "Error: Failed to copy data_ark.plist" with title "Error"'
fi

if ! copy_files "/mnt2/mobile/Library/FairPlay/" ./files/; then
  osascript -e 'display dialog "Error: Failed to copy FairPlay folder" with title "Error"'
fi

if ! copy_files "/mnt2/wireless/Library/Preferences/com.apple.commcenter.device_specific_nobackup.plist/" ./files/; then
  osascript -e 'display dialog "Error: Failed to copy com.apple.commcenter.device_specific_nobackup.plist" with title "Error"'
fi

if ! run_ssh_command '/sbin/reboot'; then
  osascript -e 'display dialog "Error: Failed to reboot" with title "Error"'
fi

osascript -e 'display dialog "Activation files saved!" with title "Success"'

kill %1 > /dev/null 2>&1

