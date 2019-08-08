# passwordless ssh

case wo passphrase  
~~~~
vagrant@apache01:~$ hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b4d34378b21de2b163f4308a5c266ccb
           Boot ID: 46445f147ab3479daa4514634aa9d632
    Virtualization: oracle
  Operating System: Ubuntu 16.04.5 LTS
            Kernel: Linux 4.4.0-131-generic
      Architecture: x86-64

      vagrant@apache01:~$ cat /etc/passwd | grep johnd
      johnd:x:1001:1001:John Doe:/home/johnd:

      vagrant@apache01:~$ ssh-keygen -t rsa (skipping passphrase)  

      vagrant@apache01:~$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub johnd@apache02                
      vagrant@apache01:~$ ssh johnd@apache02
      Welcome to Ubuntu 18.10 (GNU/Linux 4.18.0-10-generic x86_64)

       * Documentation:  https://help.ubuntu.com
       * Management:     https://landscape.canonical.com
       * Support:        https://ubuntu.com/advantage

        System information as of Fri Aug  2 09:28:30 UTC 2019

        System load:  0.0               Processes:           97
        Usage of /:   2.5% of 61.80GB   Users logged in:     1
        Memory usage: 30%               IP address for eth0: 10.0.2.15
        Swap usage:   0%                IP address for eth1: 192.168.45.11

       * MicroK8s 1.15 is out! Thanks to all 40 contributors, you get the latest
         greatest upstream Kubernetes in a single package.

           https://github.com/ubuntu/microk8s

      167 packages can be updated.
      100 updates are security updates.


      Last login: Fri Aug  2 09:23:49 2019 from 192.168.45.10
      $ hostnamectl
         Static hostname: apache02
               Icon name: computer-vm
                 Chassis: vm
              Machine ID: d8c87c7cc315443181e0bde89ba764ad
                 Boot ID: 07996c943a7a4367a1742ddd7a71eab0
          Virtualization: oracle
        Operating System: Ubuntu 18.10
                  Kernel: Linux 4.18.0-10-generic
            Architecture: x86-64      
~~~~
~~~~
johnd@apache02:~$ hostnamectl
   Static hostname: apache02
         Icon name: computer-vm
           Chassis: vm
        Machine ID: d8c87c7cc315443181e0bde89ba764ad
           Boot ID: 07996c943a7a4367a1742ddd7a71eab0
    Virtualization: oracle
  Operating System: Ubuntu 18.10
            Kernel: Linux 4.18.0-10-generic
      Architecture: x86-64
      johnd@apache02:~$ cat /etc/passwd | grep johnd
      johnd:x:1001:1001:John Doe:/home/johnd:/bin/sh
~~~~  
case w passphrase    
~~~~
vagrant@apache02:~$ hostnamectl
   Static hostname: apache02
         Icon name: computer-vm
           Chassis: vm
        Machine ID: d8c87c7cc315443181e0bde89ba764ad
           Boot ID: 07996c943a7a4367a1742ddd7a71eab0
    Virtualization: oracle
  Operating System: Ubuntu 18.10
            Kernel: Linux 4.18.0-10-generic
      Architecture: x86-64
      vagrant@apache02:~$ sudo useradd -m -s /bin/bash janed
      vagrant@apache02:~$ sudo passwd janed
      Enter new UNIX password:
      Retype new UNIX password:
      passwd: password updated successfully
      vagrant@apache02:~$ cat /etc/passwd | grep janed
      janed:x:1002:1002::/home/janed:/bin/bash
      vagrant@apache02:~$ su - janed
      Password:
      janed@apache02:~$
      janed@apache02:~$ ssh-keygen -t rsa -b 4096
      Generating public/private rsa key pair.
      Enter file in which to save the key (/home/janed/.ssh/id_rsa):
      Created directory '/home/janed/.ssh'.
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:
      Your identification has been saved in /home/janed/.ssh/id_rsa.
      Your public key has been saved in /home/janed/.ssh/id_rsa.pub.
      The key fingerprint is:
      SHA256:ytQuGNIFnZnnbWZ44qdUSRw5Vk1N2+ASmRbnmW/oKp4 janed@apache02
      The key's randomart image is:
      +---[RSA 4096]----+
      |    .. + ..++*+o.|
      |     .= . * +=.++|
      |      .o = +. =..|
      |   . . .+ O  . o |
      |  . o ..SB    . o|
      |   . = oo .  . . |
      |    . +..o    .  |
      |       .. .. .   |
      |         .E..    |
      +----[SHA256]-----+
      janed@apache02:~$ ls -lai .ssh/
      total 16
      1572898 drwx------ 2 janed janed 4096 Aug  2 09:51 .
      1572891 drwxr-xr-x 3 janed janed 4096 Aug  2 09:51 ..
      1572899 -rw------- 1 janed janed 3326 Aug  2 09:51 id_rsa
      1572900 -rw-r--r-- 1 janed janed  740 Aug  2 09:51 id_rsa.pub  
      janed@apache02:~$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub janed@apache01
      /usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/janed/.ssh/id_rsa.pub"
      The authenticity of host 'apache01 (192.168.45.10)' can't be established.
      ECDSA key fingerprint is SHA256:1Z76nTl7aEpVhcnFIanMDmBiVXrhL9SXkGVxN7LcLD0.
      Are you sure you want to continue connecting (yes/no)? yes
      /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
      /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
      janed@apache01's password:

      Number of key(s) added: 1

      Now try logging into the machine, with:   "ssh 'janed@apache01'"
      and check to make sure that only the key(s) you wanted were added.                      

      janed@apache02:~$ ssh janed@apache01
      Enter passphrase for key '/home/janed/.ssh/id_rsa':
      Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-131-generic x86_64)

       * Documentation:  https://help.ubuntu.com
       * Management:     https://landscape.canonical.com
       * Support:        https://ubuntu.com/advantage

      143 packages can be updated.
      92 updates are security updates.


      janed@apache01:~$

      janed@apache01:~$ exit
      logout
      Connection to apache01 closed.
      janed@apache02:~$ ssh janed@apache01
      Enter passphrase for key '/home/janed/.ssh/id_rsa':
      Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-131-generic x86_64)

       * Documentation:  https://help.ubuntu.com
       * Management:     https://landscape.canonical.com
       * Support:        https://ubuntu.com/advantage

      143 packages can be updated.
      92 updates are security updates.


      Last login: Fri Aug  2 10:02:47 2019 from 192.168.45.11           
~~~~

~~~~
vagrant@apache01:~$ hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b4d34378b21de2b163f4308a5c266ccb
           Boot ID: 46445f147ab3479daa4514634aa9d632
    Virtualization: oracle
  Operating System: Ubuntu 16.04.5 LTS
            Kernel: Linux 4.4.0-131-generic
      Architecture: x86-64
vagrant@apache01:~$ cat /etc/passwd | grep janed
vagrant@apache01:~$ sudo useradd -m -s /bin/bash janed
vagrant@apache01:~$ sudo passwd janed
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
vagrant@apache01:~$ su - janed
Password:
janed@apache01:~$ ls -lai
total 20
3407878 drwxr-xr-x 2 janed janed 4096 Aug  2 09:58 .
3407873 drwxr-xr-x 5 root  root  4096 Aug  2 09:58 ..
3407879 -rw-r--r-- 1 janed janed  220 Aug 31  2015 .bash_logout
3407880 -rw-r--r-- 1 janed janed 3771 Aug 31  2015 .bashrc
3407881 -rw-r--r-- 1 janed janed  655 May 16  2017 .profile

(after remote key copied)

janed@apache01:~$ ls -lai
total 28
3407878 drwxr-xr-x 4 janed janed 4096 Aug  2 10:00 .
3407873 drwxr-xr-x 5 root  root  4096 Aug  2 09:58 ..
3407879 -rw-r--r-- 1 janed janed  220 Aug 31  2015 .bash_logout
3407880 -rw-r--r-- 1 janed janed 3771 Aug 31  2015 .bashrc
3407882 drwx------ 2 janed janed 4096 Aug  2 10:00 .cache
3407881 -rw-r--r-- 1 janed janed  655 May 16  2017 .profile
3407884 drwx------ 2 janed janed 4096 Aug  2 10:00 .ssh
janed@apache01:~$ ls -lai .ssh/
total 12
3407884 drwx------ 2 janed janed 4096 Aug  2 10:00 .
3407878 drwxr-xr-x 4 janed janed 4096 Aug  2 10:00 ..
3407885 -rw------- 1 janed janed  740 Aug  2 10:00 authorized_keys
janed@apache01:~$ cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCmcgvzKr8H2QNG4ambm2VZ+BtVpB+40CAhgO1DhjYRO8wOyDUvHivFUChVAGorPsGPO3Ub7EnsUFlRA9paehg4J6crdwmzsdFn8XQv7g5pKOTR/biXRrt7mp+uHBRUa6GSMIUhMIIpFr0ck/9RIMoQ1OTflVH090VIRX1t4ybYwfnZYPKodWogAnIMJdNMDdnHqoWSNSRifCDMU5rco+fUS4gsmqqBCXGTlUBOKmmE2jfaqhkQFtKq2H2gBtCM5Mp0MbYIbY48e1BpX/dza01N9PppN4QRwCmR9WyeMc61mAzZc9TKSHFnURGwyzv0v/xrKbYeN8axYmM2LfD59oObuDm71gUCAJ7BQvgUUP2BHX7OWmoZh3UFOBaX6t9TZKNcb+LZLbfpKbu1y8+pg/0H4r+Yu5Zu0WDxbw3SBSBFfjnjfyrMKFcP6rRVqD2pa2BUtj3ApF2JC/x28mvGCPlVffpp0mjImKj1G6cA5yh5iEb2Ymzno7LmRI0E5Aq9wZWi7+tRajICmctKbtIBuK49/+e/NRu35krMW0RPbWUdIc4imDLdVAQHrxBbLdWsORGFjcDEPaOx5D1nImPTOSm80BhscvBng8d4hHk4jrkeOaPjR3Hql8d/gXKvP6jtkl/jW9ocpdGcchXxB+1qjIcmAr5MnGz5kpzzmreVdZLKIw== janed@apache02
~~~~
case wo passphrase, centos -> ubuntu    
~~~~
[vagrant@apache02 ~]$ hostnamectl
   Static hostname: apache02
         Icon name: computer-vm
           Chassis: vm
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: 8bb3498422254acbb185800edb8b45e7
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
      [vagrant@apache02 ~]$ useradd -m -s /bin/bash samd
      -bash: /usr/sbin/useradd: Permission denied
      [vagrant@apache02 ~]$ sudo useradd -m -s /bin/bash samd
      [vagrant@apache02 ~]$ sudo passwd samd
      Changing password for user samd.
      New password:
      BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word
      Retype new password:
      passwd: all authentication tokens updated successfully.
      [vagrant@apache02 ~]$ su - samd
      Password:
      [samd@apache02 ~]$

      [samd@apache02 ~]$ ssh-keygen -t rsa -b 4096
      Generating public/private rsa key pair.
      Enter file in which to save the key (/home/samd/.ssh/id_rsa):
      Created directory '/home/samd/.ssh'.
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:
      Your identification has been saved in /home/samd/.ssh/id_rsa.
      Your public key has been saved in /home/samd/.ssh/id_rsa.pub.
      The key fingerprint is:
      SHA256:Ei+bTTrAs7y++7bkXV/zL51zSy4VRQgJ30G2C3sg+A8 samd@apache02
      The key's randomart image is:
      +---[RSA 4096]----+
      |          ...++o.|
      |         . ..o.o.|
      |      . . . + o .|
      |   .   o . . + o |
      |    + o S E . o .|
      |   . + O   o . . |
      |    o * . . . +o.|
      |     +.o . . o+=o|
      |   .==+..   . .+B|
      +----[SHA256]-----+
      [samd@apache02 ~]$ ls -lai
      total 12
      50331776 drwx------. 3 samd samd  74 Aug  2 10:34 .
            64 drwxr-xr-x. 6 root root  59 Aug  2 10:33 ..
      50331777 -rw-r--r--. 1 samd samd  18 Oct 30  2018 .bash_logout
      50331778 -rw-r--r--. 1 samd samd 193 Oct 30  2018 .bash_profile
      50331779 -rw-r--r--. 1 samd samd 231 Oct 30  2018 .bashrc
            79 drwx------. 2 samd samd  38 Aug  2 10:34 .ssh
      [samd@apache02 ~]$ ls -lai .ssh/
      total 8
            79 drwx------. 2 samd samd   38 Aug  2 10:34 .
      50331776 drwx------. 3 samd samd   74 Aug  2 10:34 ..
            80 -rw-------. 1 samd samd 3243 Aug  2 10:34 id_rsa
            81 -rw-r--r--. 1 samd samd  739 Aug  2 10:34 id_rsa.pub


            [samd@apache02 ~]$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub samd@apache01
            /bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/samd/.ssh/id_rsa.pub"
            /bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
            /bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
            samd@apache01's password:

            Number of key(s) added: 1

            Now try logging into the machine, with:   "ssh 'samd@apache01'"
            and check to make sure that only the key(s) you wanted were added.

            [samd@apache02 ~]$ ssh samd@apache01
            Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-131-generic x86_64)

             * Documentation:  https://help.ubuntu.com
             * Management:     https://landscape.canonical.com
             * Support:        https://ubuntu.com/advantage

            143 packages can be updated.
            92 updates are security updates.


            samd@apache01:~$



~~~~
~~~~
vagrant@apache01:~$ hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b4d34378b21de2b163f4308a5c266ccb
           Boot ID: 46445f147ab3479daa4514634aa9d632
    Virtualization: oracle
  Operating System: Ubuntu 16.04.5 LTS
            Kernel: Linux 4.4.0-131-generic
      Architecture: x86-64
vagrant@apache01:~$ cat /etc/passwd | grep samd
vagrant@apache01:~$ sudo useradd -m -s /bin/bash samd
vagrant@apache01:~$ cat /etc/passwd | grep samd
samd:x:1003:1003::/home/samd:/bin/bash

vagrant@apache01:~$ sudo passwd samd
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
vagrant@apache01:~$ su - samd
Password:
samd@apache01:~$ ls -lai
total 20
3407887 drwxr-xr-x 2 samd samd 4096 Aug  2 10:38 .
3407873 drwxr-xr-x 6 root root 4096 Aug  2 10:38 ..
3407888 -rw-r--r-- 1 samd samd  220 Aug 31  2015 .bash_logout
3407889 -rw-r--r-- 1 samd samd 3771 Aug 31  2015 .bashrc
3407890 -rw-r--r-- 1 samd samd  655 May 16  2017 .profile

(after key copied)

samd@apache01:~$ ls -lai
total 28
3407887 drwxr-xr-x 4 samd samd 4096 Aug  2 10:39 .
3407873 drwxr-xr-x 6 root root 4096 Aug  2 10:38 ..
3407888 -rw-r--r-- 1 samd samd  220 Aug 31  2015 .bash_logout
3407889 -rw-r--r-- 1 samd samd 3771 Aug 31  2015 .bashrc
3407891 drwx------ 2 samd samd 4096 Aug  2 10:39 .cache
3407890 -rw-r--r-- 1 samd samd  655 May 16  2017 .profile
3407893 drwx------ 2 samd samd 4096 Aug  2 10:39 .ssh
samd@apache01:~$ ls -lai .ssh/
total 12
3407893 drwx------ 2 samd samd 4096 Aug  2 10:39 .
3407887 drwxr-xr-x 4 samd samd 4096 Aug  2 10:39 ..
3407894 -rw------- 1 samd samd  739 Aug  2 10:39 authorized_keys
samd@apache01:~$ cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDCRCAa/trriPg/XDXcXHaXHD3E/j5KNRtIqEszfjO3Pls0WBXQN1/hhmqULlq3fh8d0sPhQgWdxf/MoG6ii4K8aP2oCUVK2alXBeAOxBD5JcRgJMtfmxGBBC6htS8xTLvXWJV0tcZg8gLBHTnXtJme00UTjtktxK5pSt/mCNWCJXaxFriw5ME06O715NtmYz9FN1wllNHUR3XWNyuAfCuFBNvN2R4+GA4oQA5RuXwpLtuT3KazlfpwwLCU26tWcL7CkwrrWz2cZthnYU0LI0P5To7mI3YCgqp9cEHF38dDpE0KoxRYv+C9k5AJc3cmNHPnNSxqSRe9GJSBN2etKdTp70o7sCyHumkA03KsxuZOLEzJnzeo0cYASgYNoMes1Bw7WoeJB67QVqOQeHtZlh2aqvEP/ve9M+PCyAQ7Wy6b+XveQXha4zar49udQijFpm6oZw1mCuOOzADhH8fYLapfdMnWuGzhqAZlvtmM2A31ciSsyQushcG7t1fZ6dE26SSe3amKC3t+ipqfq0oCJY4AZRyicnjN2nvTLhI4xfux9fEEfHGp1Lw7mAm+cywmJk6Ma4/+JNp410IZg2qCri0slavxkyxVay3c02oquffUiKttEYKmjDb5PkeNO/uq1zuaphY8R4mxeqrEPLSsJo615NvDG1foMHc7TXFqb5PRiw== samd@apache02

~~~~
case wo passphrase, centos <- ubuntu
~~~~
vagrant@apache01:~$ hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b4d34378b21de2b163f4308a5c266ccb
           Boot ID: 46445f147ab3479daa4514634aa9d632
    Virtualization: oracle
  Operating System: Ubuntu 16.04.5 LTS
            Kernel: Linux 4.4.0-131-generic
      Architecture: x86-64
vagrant@apache01:~$ sudo useradd -m -s /bin/bash ginad
vagrant@apache01:~$ sudo passwd ginad
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
vagrant@apache01:~$   

vagrant@apache01:~$ su - ginad
Password:
ginad@apache01:~$ ls -lai
total 20
3407896 drwxr-xr-x 2 ginad ginad 4096 Aug  2 10:50 .
3407873 drwxr-xr-x 7 root  root  4096 Aug  2 10:50 ..
3407897 -rw-r--r-- 1 ginad ginad  220 Aug 31  2015 .bash_logout
3407898 -rw-r--r-- 1 ginad ginad 3771 Aug 31  2015 .bashrc
3407899 -rw-r--r-- 1 ginad ginad  655 May 16  2017 .profile

ginad@apache01:~$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ginad/.ssh/id_rsa):
Created directory '/home/ginad/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/ginad/.ssh/id_rsa.
Your public key has been saved in /home/ginad/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:IhjdOGO1Wpy7A8P2CKxhbk6Cor8+2ebZY7LelIcg50k ginad@apache01
The key's randomart image is:
+---[RSA 4096]----+
|      .          |
|   . = o         |
|  . * *          |
| . = = .         |
|..= E o S        |
|+o B O =         |
|=+ o+ B .        |
|B o +=oo         |
|.++*=+o.         |
+----[SHA256]-----+
ginad@apache01:~$ ls -lai
total 24
3407896 drwxr-xr-x 3 ginad ginad 4096 Aug  2 10:53 .
3407873 drwxr-xr-x 7 root  root  4096 Aug  2 10:50 ..
3407897 -rw-r--r-- 1 ginad ginad  220 Aug 31  2015 .bash_logout
3407898 -rw-r--r-- 1 ginad ginad 3771 Aug 31  2015 .bashrc
3407899 -rw-r--r-- 1 ginad ginad  655 May 16  2017 .profile
3407900 drwx------ 2 ginad ginad 4096 Aug  2 10:53 .ssh
ginad@apache01:~$ ls -lai .ssh/
total 16
3407900 drwx------ 2 ginad ginad 4096 Aug  2 10:53 .
3407896 drwxr-xr-x 3 ginad ginad 4096 Aug  2 10:53 ..
3407901 -rw------- 1 ginad ginad 3247 Aug  2 10:53 id_rsa
3407902 -rw-r--r-- 1 ginad ginad  740 Aug  2 10:53 id_rsa.pub


ginad@apache01:~$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub ginad@apache02
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/ginad/.ssh/id_rsa.pub"
The authenticity of host 'apache02 (192.168.45.11)' can't be established.
ECDSA key fingerprint is SHA256:BUkLkC96LORwOtYXv6ADoRGmpMlK9KngrTczij8unVk.
Are you sure you want to continue connecting (yes/no)? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
ginad@apache02's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'ginad@apache02'"
and check to make sure that only the key(s) you wanted were added.

ginad@apache01:~$ ssh ginad@apache02
Last login: Fri Aug  2 10:54:20 2019
[ginad@apache02 ~]$


~~~~

~~~~
[vagrant@apache02 ~]$ sudo useradd -m -s /bin/bash ginad
[vagrant@apache02 ~]$ cat /etc/passwd | grep ginad
ginad:x:1004:1004::/home/ginad:/bin/bash
[vagrant@apache02 ~]$ sudo passwd ginad
Changing password for user ginad.
New password:
BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word
Retype new password:
passwd: all authentication tokens updated successfully.
[vagrant@apache02 ~]$  

[vagrant@apache02 ~]$ su - ginad
Password:
[ginad@apache02 ~]$ ls -lai
total 12
16777286 drwx------. 2 ginad ginad  62 Aug  2 10:51 .
      64 drwxr-xr-x. 7 root  root   72 Aug  2 10:51 ..
16777287 -rw-r--r--. 1 ginad ginad  18 Oct 30  2018 .bash_logout
16777288 -rw-r--r--. 1 ginad ginad 193 Oct 30  2018 .bash_profile
16777289 -rw-r--r--. 1 ginad ginad 231 Oct 30  2018 .bashrc

(after key copied)

[ginad@apache02 ~]$ ls -lai
total 12
16777286 drwx------. 3 ginad ginad  74 Aug  2 10:55 .
      64 drwxr-xr-x. 7 root  root   72 Aug  2 10:51 ..
16777287 -rw-r--r--. 1 ginad ginad  18 Oct 30  2018 .bash_logout
16777288 -rw-r--r--. 1 ginad ginad 193 Oct 30  2018 .bash_profile
16777289 -rw-r--r--. 1 ginad ginad 231 Oct 30  2018 .bashrc
33575203 drwx------. 2 ginad ginad  29 Aug  2 10:55 .ssh
[ginad@apache02 ~]$ ls -lai .ssh/
total 4
33575203 drwx------. 2 ginad ginad  29 Aug  2 10:55 .
16777286 drwx------. 3 ginad ginad  74 Aug  2 10:55 ..
33575204 -rw-------. 1 ginad ginad 740 Aug  2 10:55 authorized_keys
[ginad@apache02 ~]$ cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDYp4sF0Pt0yRqk8sUPd2VkuQRNXmgozNVNQrD4LoHmQP5Pf45t/MP3/pk0322lAgzt/h+8ECCp9aL6NHLAV9LGw7JlGmKxIYWCE4PjbIfLkqg2JSavKfxSoJVI0/uQwNbw9BMhIJD8EYAVu7Uk88hTYLlpwN8ZwmzOt1Lxr8PGZVeNsDlZApWlt5yQsp00Q/JonYZvHS4LaTRkPl84aD8PapmXn6Hj2YTcn58irBcW+SFjn3PaPFyEiaAkwP+a91VsswvDJ1g/s9RPxazJ3M8w0mBfR5RKxmKFamF4lqxiJGd1BBWVJDBXTYyUnfou+G9mG6n4mV3dAi6WYur9tv/AzPTA4Kl/riiYFicaXSrfrkgaoL7bwbbKOKmvBfihSEKOxRjjcWv2JV7Jv5QH7XFTnTvZvJaC6O/sh6H+Wsk/8O1GnpIIVJyjPbG9x8H7r1Rtum6wj168kcOjvQLGMC1hOLlwv3yPDp7XQ2UBkjDnFGlG2vixCrmZ11AT0F4ANGoi6eJZ+DOgKefyP+uus0j73dAZ2INcCVN9A7vfZZkC6B/6Q0axn0+xaB4g4ZSJ2xIPf+SSC2Jwaxsbid4ST8vnDnJoHJQ7L+1kVFAhlPvGpvvNdItlqlgQP+wemrTCKPLiEoRfE5SU5ynSQ5ygaGKljn9yJZDq9JhoU3kGtYNF1w== ginad@apache01
~~~~
case wo passphrase, centos <-> centos
~~~~
[vagrant@apache01 ~]$ hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: 73b76745fff94384b7cf99297da6511d
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
      sudo useradd -m -s /bin/bash marad
      [vagrant@apache01 ~]$ cat /etc/passwd | grep marad
      marad:x:1001:1001::/home/marad:/bin/bash
      [vagrant@apache01 ~]$ sudo passwd marad
      Changing password for user marad.
      New password:
      BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word
      Retype new password:
      passwd: all authentication tokens updated successfully.
      [vagrant@apache01 ~]$

      [vagrant@apache01 ~]$ su - marad
      Password:
      [marad@apache01 ~]$ ls -lai
      total 12
      50331712 drwx------. 2 marad marad  62 Aug  2 11:19 .
            64 drwxr-xr-x. 4 root  root   34 Aug  2 11:19 ..
      50331713 -rw-r--r--. 1 marad marad  18 Oct 30  2018 .bash_logout
      50331714 -rw-r--r--. 1 marad marad 193 Oct 30  2018 .bash_profile
      50331715 -rw-r--r--. 1 marad marad 231 Oct 30  2018 .bashrc      


      [marad@apache01 ~]$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/marad/.ssh/id_rsa):
Created directory '/home/marad/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/marad/.ssh/id_rsa.
Your public key has been saved in /home/marad/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:piQ5LnuBSRojppGH3AGBanGxBs09jVn3pDl332AjRo4 marad@apache01
The key's randomart image is:
+---[RSA 4096]----+
|.+=.o =. . ..    |
|...=.= .. =+     |
|oo+o. .  +Eo+.+  |
|O++. .    o..o.o.|
|=B o+ . S      ..|
|o o..+ o         |
|  . ...          |
|   o.            |
|  ..             |
+----[SHA256]-----+
[marad@apache01 ~]$ ls -lai
total 12
50331712 drwx------. 3 marad marad  74 Aug  2 11:28 .
      64 drwxr-xr-x. 4 root  root   34 Aug  2 11:19 ..
50331713 -rw-r--r--. 1 marad marad  18 Oct 30  2018 .bash_logout
50331714 -rw-r--r--. 1 marad marad 193 Oct 30  2018 .bash_profile
50331715 -rw-r--r--. 1 marad marad 231 Oct 30  2018 .bashrc
      75 drwx------. 2 marad marad  38 Aug  2 11:28 .ssh
[marad@apache01 ~]$ ls -lai .ssh/
total 8
      75 drwx------. 2 marad marad   38 Aug  2 11:28 .
50331712 drwx------. 3 marad marad   74 Aug  2 11:28 ..
      76 -rw-------. 1 marad marad 3243 Aug  2 11:28 id_rsa
      77 -rw-r--r--. 1 marad marad  740 Aug  2 11:28 id_rsa.pub

      [marad@apache01 ~]$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub marad@apache02
      /bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/marad/.ssh/id_rsa.pub"
      The authenticity of host 'apache02 (192.168.45.11)' can't be established.
      ECDSA key fingerprint is SHA256:BUkLkC96LORwOtYXv6ADoRGmpMlK9KngrTczij8unVk.
      ECDSA key fingerprint is MD5:e8:00:2a:f0:27:37:f7:04:d1:32:4f:26:79:e5:aa:0d.
      Are you sure you want to continue connecting (yes/no)? yes
      /bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
      /bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
      marad@apache02's password:

      Number of key(s) added: 1

      Now try logging into the machine, with:   "ssh 'marad@apache02'"
      and check to make sure that only the key(s) you wanted were added.

      [marad@apache01 ~]$ ssh marad@apache02
      Last login: Fri Aug  2 13:02:50 2019
      [marad@apache02 ~]

~~~~
~~~~
[vagrant@apache02 ~]$ sudo useradd -m -s /bin/bash marad
[vagrant@apache02 ~]$ cat /etc/passwd | grep marad
marad:x:1005:1005::/home/marad:/bin/bash
[vagrant@apache02 ~]$ sudo passwd marad
Changing password for user marad.
New password:
BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word
Retype new password:
passwd: all authentication tokens updated successfully.
[vagrant@apache02 ~]$ hostnamectl
   Static hostname: apache02
         Icon name: computer-vm
           Chassis: vm
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: 8bb3498422254acbb185800edb8b45e7
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
[vagrant@apache02 ~]$ su - marad
Password:
[marad@apache02 ~]$ ls -lai
total 12
50331781 drwx------. 2 marad marad  62 Aug  2 11:24 .
      64 drwxr-xr-x. 8 root  root   85 Aug  2 11:24 ..
50331782 -rw-r--r--. 1 marad marad  18 Oct 30  2018 .bash_logout
50331783 -rw-r--r--. 1 marad marad 193 Oct 30  2018 .bash_profile
50331784 -rw-r--r--. 1 marad marad 231 Oct 30  2018 .bashrc


[marad@apache02 ~]$ ls -lai
total 12
16777281 drwx------. 3 marad marad  74 Aug  2 13:03 .
      64 drwxr-xr-x. 5 root  root   47 Aug  2 13:02 ..
16777282 -rw-r--r--. 1 marad marad  18 Oct 30  2018 .bash_logout
16777283 -rw-r--r--. 1 marad marad 193 Oct 30  2018 .bash_profile
16777284 -rw-r--r--. 1 marad marad 231 Oct 30  2018 .bashrc
33575200 drwx------. 2 marad marad  29 Aug  2 13:03 .ssh
[marad@apache02 ~]$ ls -lai .ssh/
total 4
33575200 drwx------. 2 marad marad  29 Aug  2 13:03 .
16777281 drwx------. 3 marad marad  74 Aug  2 13:03 ..
33575201 -rw-------. 1 marad marad 740 Aug  2 13:03 authorized_keys
[marad@apache02 ~]$ cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCoSu6H3uDKhQZo1QMbc47aLFFS16bJNCh/OYTLVjv6c8R6z59oujpvCFvRzkR3ObeP3xLHElzoGpP8rC1/cpkpXJGE2CtFrBtufxogDev3RMu4vl3gJ+3xbLMg1r4LY4oVfFMscbqFFhc3X+9SQ84yOhYB50xXel58qczBkl+e0us0yzA5CF3vUoNzV1Q41YT63RHvMcjQBxdAZLA2qtBa62UvS9R1tqETCIzynePcNLF1XQFRXQLWdDA+eG33Lx29YsKZE8MwkMvPqPNkrl5RggKvvdIs49Ibi7DHO7Be0fQomQ7u1YXHYFYLj5vPuj+qgmm4wdiDHJQIAmPUaUI7OEIlvmYDJYb4qa28YHFtTuKKGdGlrnQV+gJix1ZV+kwjdbtUqdBJ0PceXJlTUh1HQ1LhkeI57nCAxUYm9jWGV78yesaDuUw/5U1qbHZAYeZvDM9kehSz5UksuEkQ/E8I2BED2sFOotVo8SgvT/R+Qs1QK4dsa3He6T1jblRna8M1aT8jfcE5GqejhqfzOGslQsqX9AXSWfiNEvRW8H5Et9Ac4SVSYEwwaaiajT4ctEbeD3x3Uop1HWEKal19jxV7Je9KQVOkmpm5lLtwxrk96w5cdmN0w9CLUaIkeQ+gnv/XwVx9ZFbkU25euKOgM5YJ0ZEYq6U0sfKs82sjNOSNXw== marad@apache01
[marad@apache02 ~]$
~~~~

passwordless ssh enabled, disabled password authentication
~~~~
[marad@apache01 ~]$ ssh tester@apache02
tester@apache02's password:
Last login: Fri Aug  2 17:40:15 2019 from 192.168.45.10
[tester@apache02 ~]$

(Disable Password Authentication)

[marad@apache01 ~]$ ssh tester@apache02
Permission denied (publickey).

(marad, passwordless ssh user)
[marad@apache01 ~]$ ssh marad@apache02
Last login: Fri Aug  2 15:04:04 2019 from 192.168.45.10
~~~~

~~~~
[vagrant@apache02 ~]$ sudo useradd -m -s /bin/bash tester
[vagrant@apache02 ~]$ sudo passwd tester
[vagrant@apache02 ~]$ sudo cat /etc/ssh/sshd_config | grep PasswordAuthentication
#PasswordAuthentication yes
PasswordAuthentication yes

(Disable Password Authentication)

[vagrant@apache02 ~]$ sudo cat /etc/ssh/sshd_config | grep PasswordAuthentication
#PasswordAuthentication yes
PasswordAuthentication no
[vagrant@apache02 ~]$ sudo service sshd restart
Redirecting to /bin/systemctl restart sshd.service

~~~~
