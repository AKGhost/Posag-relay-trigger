cd pagermon/client
rtl_fm -M fm -p 72 -s 22050 -g 50 -l 70 -f (FREQ HERE)M - |  multimon-ng -t raw -a POCSAG512 -f alpha /dev/stdin | node ./reader.js | socat - udp-datagram:255.255.255.255:50000,broadcast

