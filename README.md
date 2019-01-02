# Posag-relay-trigger
Python scripting that will read from the network and look for specific pager address and trigger a relay 


this scripting was composed from many others and I thank them for sharing the parts i used. It is just compiled in a way that works for my setup.  Included in the files is the hand built command to launch rtl-FM, dial into the local channel with my SDR, decode the message with Multimon-ng. From there passing the message to Pagermon and last but not least broadcast to the local network where the other scrips come in. The original Freq and codes have been removed for security. The code is constantly changing with little things that make it easier to manage and those changes will be added as i go. Thank you for looking.



Credits go to:

https://github.com/osmocom/rtl-sdr 

https://github.com/jes1510/raspberry-gpio-email 

https://github.com/davidmckenzie/pagermon 

https://github.com/EliasOenal/multimon-ng
