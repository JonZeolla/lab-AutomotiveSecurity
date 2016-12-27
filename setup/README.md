# Automotive Security Lab Setup
A VM has been provided for the lab [here](https://drive.google.com/open?id=0B2NDLONqoOuTRFJvY0g0dU5RZWc), but if you'd like to configure this on a different system please run `setup/configure.sh` on your system.  
##### Login Credentials  
* Username:  carhax  
* Password:  P@ssword  
  
## Configuring a new VM for distribution  
* Install Kali 2016.1 in a VM[1], login as root, then open a terminal  
  * Take a snapshot  
  * `apt-get -y install open-vm-tools-desktop fuse`  
    * This will make the below configuration steps much easier  
  * `history -c && gnome-session-quit`  
* Login as root, then open a terminal
  * `echo -e "\n# Add a CLASSPATH to .bashrc\n# TODO: This is a horrible hack and should be improved\nexport CLASSPATH=/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/resources.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/rt.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/sunrsasign.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jsse.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jce.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/charsets.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/jfr.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/classes:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/icedtea-sound.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/sunec.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/cldrdata.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/zipfs.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/nashorn.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/sunpkcs11.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/java-atk-wrapper.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/sunjce_provider.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/dnsns.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/localedata.jar:/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/jaccess.jar\n" >> /etc/skel/.bashrc`  
  * `echo -e "# Add additional sbin and bin directories to \$PATH\nexport PATH=\$PATH:\${HOME}/bin:/sbin:/usr/sbin:/usr/local/sbin\n\n# Include .bashrc if it exists\nif [ -f "\${HOME}/.bashrc" ]; then\n  . "\${HOME}/.bashrc"\nfi\n" > /etc/skel/.bash_profile`  
  * `echo -e "# Kali rolling repos\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\n#deb-src http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list`  
  * `echo -e "\n\n# Add additional sbin directories to \$PATH\nexport PATH=\$PATH:/sbin:/usr/sbin:/usr/local/sbin\n" >> /etc/skel/.profile`  
  * `echo "W8wnTFMhhU7RHHAnLIPJdWPKdbySMgIpnh3qwf4uEKnSlytbbB1EWKAEvkTHLAX7uE51T2BDkQqMmttziyErC0kmQLiUeScEmYWo" >> /etc/scis.conf`  
  * `useradd -m -p $(openssl passwd -1 P@ssword) -s /bin/bash -c "SCIS Automotive Security User" -G sudo carhax`  
  * `history -c && gnome-session-quit`  
* Login as carhax  
  * Rearrange and remove Favorites shortcuts as appropriate  
  * Open a terminal  
    * `sudo systemctl disable rsyslog;sudo systemctl stop rsyslog`  
    * `sudo logrotate -f /etc/logrotate.conf`  
    * `sudo rm -rf /var/log/*1 /var/log/*old /var/log/*gz`  
    * `cd ${HOME}/Desktop`  
    * `git clone -b AutomotiveSecurity --recursive https://github.com/JonZeolla/lab-AutomotiveSecurity`  
    * `lab-AutomotiveSecurity/setup/configure.sh full`  
      * Answer the prompts as appropriate.  
    * `sudo systemctl enable rsyslog`  
    * `rm ~/.bash_history;history -c`  
  * Shutdown the virtual machine using the GUI  
* Create the OVA  
  * On a Mac using VMware Fusion, this looks something like:  

   `cd /Applications/VMware\ Fusion.app/Contents/Library/VMware\ OVF\ Tool/`  
   `./ovftool --acceptAllEulas /path/to/VM.vmx /path/to/VM.ova`  

[1]:  I typically make sure to create VMs as harware version 10 under Compatibility because I've found it fixes some issues with transferring VMs between VMware Fusion and ESXi 5.5.  

