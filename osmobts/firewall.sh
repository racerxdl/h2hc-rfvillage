sudo iptables -t nat -A POSTROUTING -s 192.168.42.0/24 -o br0 -j MASQUERADE
sudo iptables -t nat -I POSTROUTING -o apn0 -j MASQUERADE
sudo iptables -A FORWARD -i apn0 -o br0 -j ACCEPT
sudo iptables -A FORWARD -i br0 -o apn0 -j ACCEPT
