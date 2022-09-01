# 0x08. Networking basics #1
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png)
## Resources
### Read or watch:
* [What is localhost](https://en.m.wikipedia.org/wiki/Localhost)
* [What is 0.0.0.0](https://en.m.wikipedia.org/wiki/0.0.0.0)
* [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
* [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)
* [Docker sed](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)
### man or help:
* `ifconfig`
* `telnet`
* `nc`
* `cut`
## General
* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is `/etc/hosts`
* How to display your machine’s active network interfaces
## Note:
* If you’re running `0-change_your_home_IP` script on a machine that you’ll continue to use, be sure to revert `localhost` to `127.0.0.1`. Otherwise, a lot of things will stop working!

* `100-port_listening_on_localhost` can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
