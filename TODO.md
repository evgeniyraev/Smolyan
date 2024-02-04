# Tasks
- [ ] find start point

- [ ] end in current moon position
    - [ ] find current moon phase

- [ ] moon phases
    usecertant what needs to be done

- [x] connect to wifi
    - [ ] copy from previos pi
     sudo grep -r '^psk=' /etc/NetworkManager/system-connections/

     sudo nmcli c add type wifi con-name <connection-name> ifname wlan0 ssid <yourssid>
     sudo nmcli c modify <connection-name> wifi-sec.key-mgmt wpa-psk wifi-sec.psk <wifipassword>

     nmcli connection modify <connection-name> connection.autoconnect-priority 10

     nmcli connection delete id <connection name>

     [raspberry pi documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#using-the-command-line)
