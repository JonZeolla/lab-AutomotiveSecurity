# Reading from the CAN bus via CLI
## Preparations  
First, you need to make sure that you have a can interface up (either vcan0 or can0).  You can verify this by running `ip addr | grep can0`.  
* If you are using the VM, or if you've already run `${HOME}/Desktop/lab-AutomotiveSecurity/setup/configure.sh`, the correct interface should already be available.  If not, you can run `${HOME}/Desktop/setup_can.sh` or `${HOME}/Desktop/setup_vcan.sh`, whichever is appropriate.  You should only have the `setup_can.sh` script available if you've successfully configured a can0 interface in the past using the `setup` scripts.  

Also, you need to have something to prove that your reads are working.  Run the below command to send some CAN frames onto the can bus.  
`cangen vcan0`  
  
## `candump`
Now, if you plan to use a virtual CAN interface, run the below command.  
`candump -tA vcan0,0:0`  
  
This will show you all of the activity coming to the vcan0 interface, which currently should randomly generated CAN messages.  
  
There are plenty of different arguments that `candump` allows.  Feel free to play around with some of the examples given when you run `candump`.  
  
## `cansniffer`
Another tool that you can use to monitor traffic on the CAN bus is `cansniffer`.  This sort of interface may be familiar to those of you who have done 802.11 or 802.3 sniffing in the past.  Let's start with:  
`cansniffer vcan0`  
If you stop and start the `cangen` process, you will see that packets slowly fade off of the screen.  Now, let's try:  
`cangen vcan0 -g 750`  
`cansniffer vcan0 -c`  
What's interesting about the `-c` flag, is that it will highlight new/different CAN frames.  In a network which will often spew the same message dozens of times a minute, this feature is invaluable at picking out the signal from the noise.  
  
  
# Reading from the CAN bus or viewing CAN recordings using a GUI  
## `wireshark`  
Even the tried-and-true wireshark can capture and display CAN frames.  Try this:  
`wireshark -i vcan0 -k &`  
 * Don't forget that you need something producing CAN frames that wireshark can pick up.  For something generic, try `cangen vcan0`.  
  
## `kayak`  
Kayak is a great tool for parsing through CAN recordings.  To run it, execute:  
`${HOME}/Desktop/lab-AutomotiveSecurity/external/Kayak/application/target/kayak/bin/kayak`  

## `icsim`  
ICSim is an Instrument Cluster Simulator.  The standard method of interfacing with the display is by using the control, as you will see once you run the below commands.  
`cd ${HOME}/Desktop/lab-AutomotiveSecurity/external/ICSim/`  
`./icsim vcan0 &`  
`./controls vcan0 &`  
For something more interesting, fire up some of the tools described in the `write` folder and try and make the instruments change.  You could also listen to what's being sent across the can bus in a more raw format by using the `candump` or `cansniffer` tools from above.  

