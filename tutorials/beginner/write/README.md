# Writing to the CAN bus via CLI  
## Preparations  
First, you need to make sure that you have a can interface up (either vcan0 or can0).  You can verify this by running `ip addr | grep can0`.  
* If you are using the VM, or if you've already run `${HOME}/Desktop/lab-AutomotiveSecurity/setup/configure.sh`, the correct interface should already be available.  If not, you can run `${HOME}/Desktop/setup_can.sh` or `${HOME}/Desktop/setup_vcan.sh`, whichever is appropriate.  You should only have the `setup_can.sh` script available if you've successfully configured a can0 interface in the past using the `setup` scripts.  

Next, in one terminal window, setup a listener and let it run so that you can examine all of your CAN bus writes.  
`candump -tA vcan0,0:0`  

## `cansend`  
Open a second terminal window, and send something a custom CAN frame to your virtual CAN interface  
`cansend vcan0 111#534349534C6162`  
  
If you go back to the CAN listener, you should have seen your message go across.  
  
You can then send another message with a slightly longer data field  
`cansend vcan0 111#546869736973776179746f6f6c6f6e67`  
now, you may have noticed that the message got truncated on the listening side.  This is because CAN can only send 8 bytes per frame, per the spec.  
  
## `cangen`  
Now, let's send a bit more traffic.  Run the below command to generate random frames and put them on the CAN bus.  
`cangen vcan0`  
  
You can also refine cangen to send only what you want, or to view what is being sent without having to refer to `candump`.  
You can run `cangen` to see all of your options.  Specifically, pay attention to `-D`, `-L`, and `-v`.  
  
## `canplayer`  
Okay, so say you wanted to record a session and then replay it back.  Assuming you have frames on your can interface that you want to record, you can use `candump` to log them to a file, and then use `canplayer` to play them back in the future.  That would look something like this:  
`cangen vcan0 # To get something on the CAN bus`  
`candump vcan0,0:0 -l vcan0 # Start recording the traffic`  
Once that's run for a few seconds, you'll need to cancel the cangen and candump (`Ctrl+C`, `kill`, etc.).  Then, you can replay the CAN messages using:  
`canplayer vcan0=vcan0 -I candump*log`  
That will replay the contents of your candump log file, mapping the receive interface from candump (vcan0) to the interface you want it to output on (vcan0).  
There are also some handy switches such as `-t` which will send the CAN messages as quickly as possible, `-li` which will loop the candump file infinitely, or `-v` to print the sent CAN frames to stdout.  
  
## `socketcand`
The socketcand tool connects a network interface to a CAN interface on a host.  This means that you are able to connect to one or multiple CAN busses that are connected to a host running this software, over an ethernet network connection.  
You could then send/receive messages to/from that CAN bus remotely.  Below is an example of how you'd set that up.  
`cd ${HOME}/Desktop/lab-AutomotiveSecurity/external/socketcand`  
`./socketcand -i vcan0 -v`  

