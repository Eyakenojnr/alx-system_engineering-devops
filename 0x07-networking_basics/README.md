# 0x07. Networking basics #0
## Resources
### Read or watch:
* [OSI model](https://en.m.wikipedia.org/wiki/OSI_model)
* [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
* [LAN network](https://en.m.wikipedia.org/wiki/Local_area_network)
* [WAN network](https://en.m.wikipedia.org/wiki/Wide_area_network)
* [Internet](https://en.m.wikipedia.org/wiki/Internet)
* [MAC address](https://whatismyipaddress.com/mac-address)
* [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
* [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
* [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
* [Localhost](https://en.m.wikipedia.org/wiki/Localhost)
* [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [TCP/UDP ports List](https://en.m.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
* [What is ping /ICM](https://en.m.wikipedia.org/wiki/Ping_(networking_utility))
* [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)
### man or help:
* `netstat`
* `ping`
## OSI Model
* What it is
* How many layers it has
* How it is organized
## What is a LAN
* Typical usage
* Typical geographical size
## What is a WAN
* Typical usage
* Typical geographical size
## What is the Internet
* What is an IP address
* What are the 2 types of IP address
* What is `localhost`
* What is a subnet
* Why IPv6 was created
## TCP/UDP
* What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
* What is the main difference between TCP and UDP
* What is a port
* Memorize SSH, HTTP and HTTPS port numbers
* What tool/protocol is often used to check if a device is connected to a network
## Tasks
### 0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:
* The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
* The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T233823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=183d3e472a889f609a2a3fdbb131c8b32c70e73b0a4b51d2412627b3eed62e7e)
In this project, the main focus is on:

* The Transport layer and especially TCP/UDP
* On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T233823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1883f62ef62accd0e42c861ed94fd0b21c30d97d567ea2d7deca29ee7ca69295)
### 1. Types of network
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T233823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a6322ca3594fe630089a5a7488a144a828350fc8fb8e2093166d8b7768a08413)
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.
### 2. MAC and IP address
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T233823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b453542b8bddc72f903459111e3cc104ea2a50022da5364db587292b3da9d8ba)
### 4. TCP and UDP ports
Once packets have been sent to the right network device using IP with either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

Comparing a network device to a house, where IP address is like the postal address, UDP and TCP ports are like the windows and doors of the house. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free for use.

While the full list of ports shouldn't be memorized, it is important to know the most used ports:
* **22** for SSH
* **80** for HTTP
* **443** for HTTPS
Note that a specific [IP + port = socket](https://www.stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket/).
### 5. Is the host on the network
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command `ping` uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.
Example:
```
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
```
It is interesting to look at the `time` value, which is the time that it took for the ICMP request to go to the `8.8.8.8` IP and come back to the host. The IP `8.8.8.8` is owned by Google, and the quickest roundtrip between the computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between the computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the `ping` command to see what is going on!
