# Writing to the CAN bus via CLI  
## Preparations  
You need to make sure you are in the vircar directory, which should be located in `${HOME}/Desktop/lab-AutomotiveSecurity/external/vircar/`  

See the related blog post [here](http://dn5.ljuska.org/cyber-attacks-on-vehicles-2.html).  

## `vircar`  
Run the following command to start up the virtual car:  
`sudo ./vircar`  
If you get the error message `RTNETLINK answers: File exists`, you've already run vircar once and the interface still exists.  Although it should not cause an issue, you can delete the interface and get a clean start by either deleting the interface using:  
`sudo ip link delete vircar`  
or you can "blow the car up", which is a bit funner.  Do that by running:  
`sudo ./vircar k`  

## `vircar-fuzzer`  
`vircar-fuzzer` is a ruby script written by the author of `vircar`, which was meant to do some fuzzing and brute forcing of the virtual `vircar`, in order to prove a point.  Something similar could be done for real cars, although it would be much more expensive if you were successful =)  
  
In order to run `vircar-fuzzer`, ensure you are in `${HOME}/Desktop/lab-AutomotiveSecurity/external/vircar-fuzzer/src` and run:  
`ruby vircar-fuzzer.rb`  
This script essentially is a wrapper for `cangen` and allows for slightly more directed fuzzing using `vircar-fuzzer/src/frames` as an input.  Feel free to take a look around in the script.  

## `canbus_send.py`  
Play around with `${HOME}/Desktop/lab-AutomotiveSecurity/external/Python_Can/canbus_send.py`  

