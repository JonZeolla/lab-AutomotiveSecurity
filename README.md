# Automotive Security Lab

## How to clone this branch
* `git clone https://github.com/JonZeolla/lab-AutomotiveSecurity`
  * Clone the latest revision of the lab-AutomotiveSecurity repo.
* `git clone -b 2016-05-12_SCIS_AutomotiveSecurity https://github.com/JonZeolla/lab-AutomotiveSecurity`
  * Clone the revision of the lab-AutomotiveSecurity repo used during the 2016-05-12 Steel City InfoSec lab.  Cloning any of the pointers (tags) will put you in a detached HEAD state, which is expected.

## Contributing
1. [Fork the repository](https://github.com/jonzeolla/lab-AutomotiveSecurity/fork)
1. Create a feature branch via `git checkout -b feature/description`
1. Make your changes
1. Commit your changes via `git commit -am 'Summarize the changes here'`
1. Create a new pull request ([how-to](https://help.github.com/articles/creating-a-pull-request/))

## Related Events
### 2016-05-12 Steel City Information Security Lab
[Event Details](http://www.meetup.com/Steel-City-InfoSec/boards/thread/49839423)
[Event Posting](http://www.meetup.com/Steel-City-InfoSec/events/226195653/)

## How to use this repo
* `setup`  
  * Here are some scripts to setup the requirements to do the lab tutorials.  There is a [VM](https://drive.google.com/open?id=0B2NDLONqoOuTRFJvY0g0dU5RZWc) which was distributed the first time I did this lab, but the scripts in here allow the lab to be setup on additional machines.  
    * If you plan to use the VM, the username is `carhax` and the password is `P@ssword`.  
* `tutorials`  
  * All of the materials exist here, categorized into skill level (beginner, intermediate, etc.), and then type of lab (read vs write).  
* `external`  
  * All external projects used by this lab exist here as submodules.  
* `store`  
  * This is where large(ish) files go for storage, especially if they're referenced in multiple labs.  

## Updating the lab
If you'd like to update this branch, open a terminal and `cd` into the repo (if you are following the lab, this is `${HOME}/Desktop/lab-AutomotiveSecurity/`) and then run:
```
git pull
setup/configure.sh
```
 * It is possible that you will need to first run `git reset --mixed`, depending on if the `git merge` can be successful without manual intervention.  Note that running this command will reset your index, but not the working tree.  If you don't know what that means, and would like to, read [this](https://git-scm.com/docs/git-reset).

## Some other good materials  
* http://www.ni.com/white-paper/2732/en/  
* https://en.wikipedia.org/wiki/SocketCAN  
* http://www.cowfishstudios.com/blog/canned-pi-part1  
* http://dn5.ljuska.org/napadi-na-auto-sistem-1.html  
* http://dn5.ljuska.org/cyber-attacks-on-vehicles-2.html  
* http://www.ioactive.com/pdfs/IOActive_Adventures_in_Automotive_Networks_and_Control_Units.pdf  
* http://opengarages.org/handbook/2014_car_hackers_handbook_compressed.pdf  
* https://www.nostarch.com/carhacking  
* http://hackaday.com/2013/10/22/can-hacking-the-in-vehicle-network/  
* https://www.youtube.com/watch?v=Ym8xFGO0llY  
* http://www.carhackingvillage.com/  
* http://www.boschdiagnostics.com/pro/j2534-faqs  
* http://www.canbushack.com/blog/index.php  

## Migration
On 2016-12-27, this repo was migrated from the AutomotiveSecurity branch of https://github.com/JonZeolla/Lab to its own standalone repository.  This was in order to make contributions and third party use easier, as I received feedback that the branching strategy used before was confusing to some.
