###########################################################
tcpdump cheatsheet: command-line capture of network traffic
###########################################################

:date: 2011-05-18
:author: Stephanie Lockwood-Childs
:tags: tcpdump, troubleshooting, network
:category: cheatsheets
:slug: tcpdump_cheatsheet
:summary: tcpdump command-line cheatsheet 

tcpdump cheatsheet for command-line capture of network packets,
useful for cases where where using wireshark for capture is not practical
(e.g. network troubleshooting on remote servers or embedded devices)

==================
tcpdump cheatsheet
==================

Modes
-----

tcpdump has two main modes

* text display on console (but can be saved to file with redirection)
* binary capture to file for detailed analysis (stored in pcap format)

Overall syntax
--------------

 tcpdump <options> <filter expression>

where both options and filter expression are optional 

Using just the plain command,

 tcpdump

tells tcpdump to use default settings

Default settings
----------------

* listen on first network interface (which is often "eth0")
* text display on console (as opposed to saving to file)
* display summary of info from each packet header
* display all packets
* unlimited capture (don't quit until killed, e.g. with ctrl-c)

Common options
--------------

* which interface: *-i eth0*, *-i eth1*, *-i usb0*, *-i any*
  ("any" is a virtual interface that includes packets from all
  interfaces) 
* skip name lookups for ip addresses or port numbers: *-n*
  (use this if DNS is having problems so that name lookups are slow or
  failing)
* limit number of packets to capture: *-c 100*, *-c 2000*
* display packet data in addition to header:  *-X*
* limit data size for each packet: *-s 100*, *-s 2000*
  **PROBABLY DO NOT WANT THIS WHEN STORING PACKETS FOR LATER ANALYSIS!**
* write captured packets to file: *-w filename*
* read from existing file (instead of live capture): *-r filename*
* verbose: *-v*, *-vv*, or -vvv for increasing verbosity
  (when capturing to file, any of the above usefully enables a count of received packets)

**NOTE:**
  when writing packets to file, full contents of packets are saved
  in pcap format; flags such as *-X* are only needed if displaying
  on console, when the default display summarizes header info 
  and skips packet payloads altogether

Filter syntax
--------------

* limit by ip address/hostname: host x.x.x.x, host somehost.com
* limit by port number/port name: port 80, port http
  official port names can be found in /etc/services
* limit by packet type: ip, tcp, udp, icmp, arp, esp, ah
  (last couple being IPSEC packets)
* combine simple limits into more complex criteria: not, and, or 
* group operators in complex criteria: ( )
  good idea to use quotes around the whole filter statement
  if it is complicated enough to need parentheses...

Examples
--------

* display summary of packets to/from eth1 network card, skipping hostname lookups

    tcpdump -i eth1 -n

* display summary of packets to/from any web server

    tcpdump -i any port http

* save summary of ping packets to/from google.com to a file

    tcpdump -i any icmp and host google.com > /tmp/google_ping.txt

* capture all traffic to a file for later analysis (e.g. in wireshark)

    tcpdump -i any -w /tmp/saved_traffic.pcap -v  

* capture all traffic except your own ssh connection to a file 

    tcpdump -i any -w /tmp/saved_traffic.pcap -v "not ( port ssh and host me.org )"

**NOTE:**
  ignore any unintentional wrapping of command-lines due to html display, each should be a single line
