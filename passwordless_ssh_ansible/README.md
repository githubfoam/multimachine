# passwordless ssh deployment

centos apache01 -> centos apache02  
~~~~
[root@apache01 ~]# hostnamectl
   Static hostname: apache01
         Icon name: computer-vm
           Chassis: vm
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: f588f88177b34be3b2cd29798f1b3cbb
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
[root@apache01 ~]# ls -lai
total 28
100663361 dr-xr-x---.  3 root root  149 Aug  4 18:30 .
       64 dr-xr-xr-x. 18 root root  239 Aug  4 18:30 ..
100663363 -rw-------.  1 root root 2768 Dec 28  2018 anaconda-ks.cfg
101121762 -rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
101121763 -rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
101121764 -rw-r--r--.  1 root root  176 Dec 29  2013 .bashrc
101121765 -rw-r--r--.  1 root root  100 Dec 29  2013 .cshrc
100663362 -rw-------.  1 root root 2094 Dec 28  2018 original-ks.cfg
 33586326 drwxr-----.  3 root root   19 Aug  4 18:30 .pki
101121766 -rw-r--r--.  1 root root  129 Dec 29  2013 .tcshrc
[root@apache01 ~]# ping -c 2 apache02.local
PING apache02.local (192.168.45.11) 56(84) bytes of data.
64 bytes from apache02.local (192.168.45.11): icmp_seq=1 ttl=64 time=0.633 ms
64 bytes from apache02.local (192.168.45.11): icmp_seq=2 ttl=64 time=0.350 ms

--- apache02.local ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.350/0.491/0.633/0.143 ms




[root@apache02 ~]# hostnamectl
   Static hostname: apache02
         Icon name: computer-vm
           Chassis: vm
        Machine ID: cfa0388701ff415dbceb1d083ec3fdfd
           Boot ID: 077f5ae188b6427bb9ee76596640849a
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.1.3.el7.x86_64
      Architecture: x86-64
[root@apache02 ~]# ls -lai
total 28
100663361 dr-xr-x---.  3 root root  149 Aug  4 18:30 .
       64 dr-xr-xr-x. 18 root root  239 Aug  4 18:30 ..
100663363 -rw-------.  1 root root 2768 Dec 28  2018 anaconda-ks.cfg
101121762 -rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
101121763 -rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
101121764 -rw-r--r--.  1 root root  176 Dec 29  2013 .bashrc
101121765 -rw-r--r--.  1 root root  100 Dec 29  2013 .cshrc
100663362 -rw-------.  1 root root 2094 Dec 28  2018 original-ks.cfg
 33586326 drwxr-----.  3 root root   19 Aug  4 18:30 .pki
101121766 -rw-r--r--.  1 root root  129 Dec 29  2013 .tcshrc
[root@apache02 ~]# ping -c 2 apache01.local
PING apache01.local (192.168.45.10) 56(84) bytes of data.
64 bytes from apache01.local (192.168.45.10): icmp_seq=1 ttl=64 time=0.431 ms
64 bytes from apache01.local (192.168.45.10): icmp_seq=2 ttl=64 time=0.462 ms

--- apache01.local ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1004ms
rtt min/avg/max/mdev = 0.431/0.446/0.462/0.026 ms





[root@apache01 ~]# ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:gJVqd61rfGZVrMI60e0HUZBXRXE800eu/+ppFxauarA root@apache01
The key's randomart image is:
+---[RSA 4096]----+
|      ..    .o *X|
|     o.     . o+=|
|    ...  .   +  =|
|    o ... . . oo |
|   . . .S+ . +o .|
|        o.+ =  = |
|       . +o+ .o o|
|        *E+...o.o|
|       . =...++o.|
+----[SHA256]-----+
[root@apache01 ~]# ls -lai .ssh/
total 12
100728721 drwx------. 2 root root   57 Aug  5 07:02 .
100663361 dr-xr-x---. 4 root root  161 Aug  5 06:56 ..
100728723 -rw-------. 1 root root 3243 Aug  5 07:02 id_rsa
100728724 -rw-r--r--. 1 root root  739 Aug  5 07:02 id_rsa.pub
100728722 -rw-r--r--. 1 root root  190 Aug  5 06:56 known_hosts
[root@apache01 ~]# ssh-copy-id -i $HOME/.ssh/id_rsa.pub root@apache02.local
/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/root/.ssh/id_rsa.pub"
/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@apache02.local's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'root@apache02.local'"
and check to make sure that only the key(s) you wanted were added.

[root@apache01 ~]# ssh root@apache02.local
Last failed login: Mon Aug  5 07:03:12 UTC 2019 from 192.168.45.10 on ssh:notty
There were 6 failed login attempts since the last successful login.
Last login: Mon Aug  5 06:56:33 2019 from 192.168.45.10
[root@apache02 ~]# exit
logout
Connection to apache02.local closed.
[root@apache01 ~]#



[root@apache02 ~]# ls -lai .ssh/
total 4
 34099183 drwx------. 2 root root  29 Aug  5 07:06 .
100663361 dr-xr-x---. 4 root root 182 Aug  5 07:06 ..
 34099189 -rw-------. 1 root root 739 Aug  5 07:06 authorized_keys
[root@apache02 ~]# cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDPCl+fXxfIogCXR+uvc9e6LlO7lzB+UZID9CUReYy5P94X6kboV3V4BXNn6j99FFYgXFgMqVfkEiCFUdOfwfT4ffHndmXUhtmjM9hCl81jyPnrxza+ki+AXLc1mip0IO5dokt3fTuxUJjWuZOtlgk79VsFcF1nv/xmihmt5t+pPRdvUXlmn8uDqlXqxIyBzLaORQ1PGY8DXRtYBl5y/zQ/dBjhwmBKJv7Tk6j76+0CChDBZEeMdJYUEB1zKJFxTXerIqb5QNeWngu3eL+ygGCZeEtfG59MTGtnmk2aKKl/3wUwuGAgXRIypiAy8Q/A8pUxIht9cQsiz5r8R0LI5oT2+NUcRSR+85wjZ4jEYpItNNj/h7tqTkALizidanovReeNFb1CCILHLwiH+m4+okCqW8nMfHKYzLUA5yidVn+MzgHhbsSl3QHtGqtRqWx2TbNZC/IlkE3040mrDs8GvIXWgoqXPPvEtdKl/iKQVXNSb4zNWm/QGThF08yS9dWlvm4Xe7WEIEbixnl8XcwMyfoKEC+DW0WoeL6v3E+789awkoSci7QBy0xjLxVbeL9gu4IIbGRYnaaoEN8q90uUarMwJp6rFmMvHHvuZ89k5BP0oBVvbJ/GWHfEBOXgrW7nQFvaJV9tyvrgZ/qmo9wK4wCf2DsY6nbLJ7cvUwRXmVPxgw== root@apache01





[root@apache02 ~]# cat /etc/ssh/sshd_config | grep PermitRootLogin
#PermitRootLogin yes
# the setting of "PermitRootLogin without-password".
[root@apache02 ~]# cat /etc/ssh/sshd_config | grep PasswordAuthentication
#PasswordAuthentication yes
PasswordAuthentication yes
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication, then enable this but set PasswordAuthentication
[root@apache02 ~]# sed -ie 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
[root@apache02 ~]# cat /etc/ssh/sshd_config | grep PasswordAuthentication
#PasswordAuthentication no
PasswordAuthentication no
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication, then enable this but set PasswordAuthentication
[root@apache02 ~]# service sshd restart
Redirecting to /bin/systemctl restart sshd.service
[root@apache02 ~]# cat /etc/passwd | grep devops1
[root@apache02 ~]# cut -d: -f1 /etc/group | sort | grep sudo
[root@apache02 ~]# groupadd sudo
[root@apache02 ~]# cut -d: -f1 /etc/group | sort | grep sudo
sudo
[root@apache02 ~]#




[root@apache01 ~]# ssh root@apache02.local
Last failed login: Mon Aug  5 07:08:50 UTC 2019 from 192.168.45.10 on ssh:notty
There were 2 failed login attempts since the last successful login.
Last login: Mon Aug  5 07:06:41 2019 from 192.168.45.10
[root@apache02 ~]# exit
logout
Connection to apache02.local closed.
[root@apache01 ~]#




(generated passphrae in ssh-setup.yml)
# echo "devops1badpassword" | mkpasswd --stdin --method=sha-512 --salt="devops1mybadsalt"
[root@apache01 ~]# cat /etc/passwd | grep devops1
[root@apache01 ~]# useradd -m -s /bin/bash devops1
[root@apache01 ~]# passwd devops1
Changing password for user devops1.
New password:
BAD PASSWORD: The password is shorter than 8 characters
Retype new password:
passwd: all authentication tokens updated successfully.
[root@apache01 ~]# su - devops1
[devops1@apache01 ~]$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/devops1/.ssh/id_rsa):
Created directory '/home/devops1/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/devops1/.ssh/id_rsa.
Your public key has been saved in /home/devops1/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:OoMQY13jdlJ/a4vdje23mB0Ll8HOWDGsJObBigQpGBE devops1@apache01
The key's randomart image is:
+---[RSA 4096]----+
| E=  .+ .        |
| . o +.o ..   .  |
|  + o +.. .=.. + |
| . o ..o. +.+.o o|
|  .    .S. .o. + |
|   . . .   + o=+o|
|    . +   . ooo*o|
|       o      *.+|
|             o ++|
+----[SHA256]-----+
[devops1@apache01 ~]$ ls -lai .ssh/
total 8
      75 drwx------. 2 devops1 devops1   38 Aug  5 07:21 .
50331712 drwx------. 3 devops1 devops1   74 Aug  5 07:21 ..
      76 -rw-------. 1 devops1 devops1 3243 Aug  5 07:21 id_rsa
      77 -rw-r--r--. 1 devops1 devops1  742 Aug  5 07:21 id_rsa.pub
[devops1@apache01 ~]$ exit
logout

[root@apache01 ~]# ansible-playbook -i /vagrant/provisioning/inventory.hosts /vagrant/provisioning/ssh-setup.yml
 [WARNING]: Found variable using reserved name: remote_user


PLAY [cluster] ****************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [apache02.local]

TASK [user] *******************************************************************************************************************************************************************************************************
changed: [apache02.local]

TASK [authorized_key] *********************************************************************************************************************************************************************************************
changed: [apache02.local]

TASK [template] ***************************************************************************************************************************************************************************************************
changed: [apache02.local]

TASK [service] ****************************************************************************************************************************************************************************************************
changed: [apache02.local]

PLAY RECAP ********************************************************************************************************************************************************************************************************
apache02.local             : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

[root@apache01 ~]# su - devops1
Last login: Mon Aug  5 07:21:32 UTC 2019 on pts/0
[devops1@apache01 ~]$ ssh devops1@apache02.local
The authenticity of host 'apache02.local (192.168.45.11)' can't be established.
ECDSA key fingerprint is SHA256:BUkLkC96LORwOtYXv6ADoRGmpMlK9KngrTczij8unVk.
ECDSA key fingerprint is MD5:e8:00:2a:f0:27:37:f7:04:d1:32:4f:26:79:e5:aa:0d.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'apache02.local,192.168.45.11' (ECDSA) to the list of known hosts.
[devops1@apache02 ~]$ exit
logout
Connection to apache02.local closed.
[devops1@apache01 ~]$ ssh devops1@apache02.local
Last login: Mon Aug  5 07:26:34 2019 from apache01.local
[devops1@apache02 ~]$ exit
logout
Connection to apache02.local closed.
[devops1@apache01 ~]$ su - root
Password:
Last login: Mon Aug  5 06:54:52 UTC 2019 on pts/0
[root@apache01 ~]# ssh root@apache02.local
Permission denied (publickey).
[root@apache01 ~]#




[root@apache02 ~]# cat /etc/passwd | grep devops1
devops1:x:1001:1002:devops1:/home/devops1:/bin/bash
[root@apache02 ~]# id devops1
uid=1001(devops1) gid=1002(devops1) groups=1002(devops1),1001(sudo)
[root@apache02 ~]# ls -lai ~devops1/.ssh/
total 12
      75 drwx------. 2 devops1 devops1   61 Aug  5 07:26 .
50331776 drwx------. 3 devops1 devops1   95 Aug  5 07:26 ..
      79 -rw-------. 1 devops1 devops1  742 Aug  5 07:26 authorized_keys
      76 -rw-------. 1 devops1 devops1 1679 Aug  5 07:26 id_rsa
      77 -rw-r--r--. 1 devops1 devops1  411 Aug  5 07:26 id_rsa.pub
[root@apache02 ~]# cat ~devops1/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDlpCZ+PcIbQl+hL5jWa3ktBIja5NsQJNM8of1vO70guhuVxYhInL6CBTQvHsGduqc7TQg6Fqlj3Li+UuJZASONAXKAfsxqlE7cyn6VHBJeIjEK3cyDExujprCbNaYvX9gHs/e/33PiKhp/+/h/ryRU6XTvtp22QvLSBWVpmybEa33i4jds+wiW97Us1+IO1R1wDTcicQMeANyqD8zSiU3DtyvBwwcdPZrYBOsEP2CFMzXZKdkd0eJQF6696682Sk3r2tOjYwZUCjZTG4krDws/xC15cdJV3D0G+LoSdaeGkr5b4DOKCngAJnEr2NpKXmC4ZKB0ai/ZrwedWHVl4STUPXKJ2YR5Yl7wbBujqkKaCYPnueeslQB81/saa9XkAD/c3DL9su6HfeQ2VS7L8oMHM+R7IkXvo64sZnOC/YdCkM9RTXMrOyR1EJwSWmUu5AFDT97Ihx0uLg6ITeVpA4LPFPxA6HtwsrfFrW2CCbuZBx4eZ8pJIzJ2ukQoSZKCYAAOLJp4a8rb6PJi/cWss//o0oDl4/AqUNFgeIu8rxlKs+wUl3T3JjYCa2KmdCR/oJrxSgmtpZUTAX6OKefMtergsp9u4aNypaCmKRqLm6EMPqUGX3aCdy5mFNpLfl+4UT+ex45iazyB6JD0x3iPcfqAkXz6jOt/Fa4YMHGUh/m9XQ== devops1@apache0





[root@apache01 ~]# cat ~devops1/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDlpCZ+PcIbQl+hL5jWa3ktBIja5NsQJNM8of1vO70guhuVxYhInL6CBTQvHsGduqc7TQg6Fqlj3Li+UuJZASONAXKAfsxqlE7cyn6VHBJeIjEK3cyDExujprCbNaYvX9gHs/e/33PiKhp/+/h/ryRU6XTvtp22QvLSBWVpmybEa33i4jds+wiW97Us1+IO1R1wDTcicQMeANyqD8zSiU3DtyvBwwcdPZrYBOsEP2CFMzXZKdkd0eJQF6696682Sk3r2tOjYwZUCjZTG4krDws/xC15cdJV3D0G+LoSdaeGkr5b4DOKCngAJnEr2NpKXmC4ZKB0ai/ZrwedWHVl4STUPXKJ2YR5Yl7wbBujqkKaCYPnueeslQB81/saa9XkAD/c3DL9su6HfeQ2VS7L8oMHM+R7IkXvo64sZnOC/YdCkM9RTXMrOyR1EJwSWmUu5AFDT97Ihx0uLg6ITeVpA4LPFPxA6HtwsrfFrW2CCbuZBx4eZ8pJIzJ2ukQoSZKCYAAOLJp4a8rb6PJi/cWss//o0oDl4/AqUNFgeIu8rxlKs+wUl3T3JjYCa2KmdCR/oJrxSgmtpZUTAX6OKefMtergsp9u4aNypaCmKRqLm6EMPqUGX3aCdy5mFNpLfl+4UT+ex45iazyB6JD0x3iPcfqAkXz6jOt/Fa4YMHGUh/m9XQ== devops1@apache01

~~~~
alternatives
~~~~
$ printf "badpassword" | mkpasswd --stdin --method=sha-512 --salt="g3RYi6b0nk9y43Rl"
$ tr -dc A-Za-z0-9 < /dev/urandom | dd bs=100 count=1 2>/dev/null; echo ''
$ dd if=/dev/urandom bs=1 count=32 2>/dev/null | base64 -w 0 | rev | cut -b 2- | rev
$ python -c "import crypt, getpass, pwd; print(crypt.crypt('password', '\$6\$saltsalt\$'))"
$ gpg2 --gen-random --armor 1 14
~~~~
