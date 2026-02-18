# Wireshark_Traffic_Analysis_Lab - Network Traffic Analysis Laboratory: Capturing & Analyzing ICMP, TCP, and HTTP Traffic with Wireshark
  ------------------------------
Project Overview
----------------
🔹This laboratory project provides a hands-on examination of network communications by capturing and analyzing live traffic between two Linux-based systems. Using Wireshark as the primary analysis tool, I established a controlled testing environment consisting of a Kali Linux machine (acting as the source/attacker) and an Ubuntu machine (acting as the target/victim) to observe, filter, and interpret various network protocols at the packet level.

🔹The objective was to move beyond theoretical networking concepts by visualizing real-time data transmission, understanding protocol behaviors, and identifying security implications observable through traffic analysis. Throughout this project, I systematically generated and captured multiple traffic types to build a comprehensive understanding of how data moves across networks and how malicious activities can be detected.

🔍 Traffic Analysis Fundamentals
   =============================
🔹ICMP Traffic Analysis: Generated and analyzed ping requests/responses between Kali and Ubuntu systems

🔹Wireshark Graph Utilization: Created and interpreted various Wireshark graphs (I/O Graphs, Flow Graphs) to visualize network traffic patterns

🔹Packet Filtering: Implemented display and capture filters to isolate specific traffic types and reduce noise

📡 Network Protocols & Communications
   ===================================
🔹TCP Three-Way Handshake: Captured and analyzed the complete SYN, SYN-ACK, ACK handshake process

🔹HTTP Traffic: Monitored and inspected unencrypted HTTP request/response cycles

🔹Packet-Level Analysis: Examined packet headers, payloads, and protocol-specific fields

🔐 Security Assessment Techniques
   ==============================
   
🔹SYN Scanning: Performed and identified port scanning activities, understanding how attackers map network services

🔹Traffic Pattern Recognition: Distinguished between legitimate traffic and potential malicious activities

Technical Environment:

🔹Attack Machine: Kali Linux

🔹Target Machine: Ubuntu Linux

🔹Analysis Tool: Wireshark Network Protocol Analyzer


  🌐 PROJECT SUMMARY 
  ====================

     
  Wireshark Traffic Analysis Lab
  ==============================

🔹This project focuses on analyzing network traffic in a controlled and isolated lab environment to understand TCP/IP behavior, HTTP communication, and basic attack patterns.

🔹The lab was conducted within a virtualized environment using VirtualBox, where both attacker and target machines were configured on a bridged network to simulate real-world communication. Kali Linux was used as the attacking machine, and Ubuntu served as the target system.

🔹Using Wireshark, network packets were captured and analyzed to study TCP handshakes, SYN packets, HTTP requests, retransmissions, and traffic patterns. A controlled DoS attack simulation was performed in a home lab using ddos-ripper to observe traffic spikes and server behavior under stress.

🔹Additionally, a custom Python traffic generator script was developed to send packets at a controlled rate to avoid overwhelming the server while enabling detailed packet inspection.

🔹This project demonstrates practical understanding of network protocols, packet-level analysis, traffic monitoring, and basic attack detection techniques in a safe lab setup.

1️⃣ Lab Environment Setup
=========================

 - Created isolated home lab using VirtualBox

 - Configured network settings to Bridged Mode

 - Verified IP addresses for both attacker and target machines

 - Ensured controlled and safe testing environment
    

2️⃣ Traffic Monitoring & Packet Analysis
========================================

 - Captured and analyzed TCP SYN packets,Full TCP three-way handshake and had retransmission because of port 80 protected by firewall

Identified:TCP Handshake behavior and TCP Handshake with No SYN-ACK response (Port closed or filtered) Filtered Specified IP traffic from the same IP address,
Used I/O Graph in Wireshark to monitor traffic spikes and drops.practiced on X-axis and Y-axis

3️⃣ Port 80 & Retransmission Research
=====================================

 - Conducted detailed analysis of HTTP traffic over Port 80 using Wireshark to examine request packets and server responses. Investigated TCP retransmissions to understand packet loss, network delays, and conditions leading to repeated transmissions during communication.

 - Conducted detailed analysis of HTTP traffic over Port 80 using Wireshark to examine request packets and server responses. Investigated TCP retransmissions to understand packet loss, network delays, and conditions leading to repeated transmissions during communication. Additionally, analyzed scenarios where a TCP handshake received no SYN-ACK response, identifying indications of closed or filtered ports and firewall-based traffic control.

4️⃣ Controlled DoS Simulation (Home Lab)
=======================================

 - Performed a controlled DoS simulation within an isolated virtual lab using ddos-ripper to generate high traffic for analysis purposes. Monitored packet flow, traffic spikes, and server behavior in real time using Wireshark. Evaluated how abnormal traffic patterns appear at the packet level and studied system response under stress in a safe home lab environment.

  - Additionally, documented the observed traffic patterns and response behavior to understand early indicators of potential DoS conditions and basic detection techniques within a monitored network environment.

 
Common Protocol Filters
=======================

 
  🖧 HTTP Filters  = http : Show all HTTP traffic    ip.src == 192.168.1.10 and http :  Show HTTP traffic from specific IP
  
  🖧 SYN Packet Filters = tcp.flags.syn == 1 and tcp.flags.ack == 0 : Show all SYN packets (without ACK)  ,  tcp.flags.syn == 1 :  Show all SYN packets (including SYN-ACK)
  
   🖧 ACK Packet Filters = tcp.flags.ack == 1 :  Show all ACK packets  ,  ip.addr == 192.168.1.10 and ip.addr == 192.168.1.100 and tcp.flags.ack == 1 : Show ACK packets in a specific conversation
  
   🖧 Normal HTTP Traffic = http and ip.addr == 192.168.1.10 and ip.addr == 192.168.1.100 :  Show complete HTTP conversation  ,  tcp.flags.syn == 1 and ip.addr == 192.168.1.10 or ip.addr == 192.168.1.100 : Show TCP handshake before HTTP 



 
  5️⃣PYTHON TRAFFIC SIMULATOR SCRIPT USED FOR THE PROJECT
  =======================================================

  
   Purpose  -  A multi-threaded Python script designed to generate HTTP traffic for network analysis and DoS simulation in a controlled lab environment
   =======


              
 KEY FEATURES
 ============

 
🐍Component	                     Description

🐍Language	        -      Python 3 with socket and threading libraries

🐍Target	          -      Ubuntu victim machine (IP: 192.168.x.x, Port: 80)

🐍Traffic Type	    -      HTTP GET requests to root directory

🐍Concurrency	      -      10 simultaneous threads

🐍Request Volume	  -      100 requests per thread (1000 total requests)



🐧 This Simulates Light traffic load on web server and Multiple concurrent connections from single source It Uses Raw socket communication (bypasses browser/curl) and Basic HTTP flood pattern for DoS analysis


   
🐧 Wireshark Observations - When running this script from Kali to Ubuntu, Wireshark captures packets Rapidly TCP handshakes (SYN, SYN-ACK, ACK).HTTP GET requests , TCP connection terminations,Pattern of requests from same source IP can be identify and Using iptables (native Linux firewall) on your Ubuntu machine you can block a specific IP if needed so packets are'nt send to you.


6️⃣.I/O Graph Analysis: Traffic Simulator Results :
===================================================

   Graph                 Color	                  Display Filter	                             What It Shows
   =====                 =====                    ==============                              ===============   
 
 🔹 All Packets         	Blue	                      (none)	                           Total network traffic (all protocols)
 
  
 🔹 TCP Errors        	  Red                    	tcp.analysis.flags	                 TCP problems (retransmissions, dup ACKs, etc.)
 
  
  🔹 Filtered packets 	  Green                  	 tcp.port==80	                         HTTP/port 80 traffic specifically
  


Wireshark I/O Graph
===================

  🖧The I/O Graph (Input/Output Graph) is a powerful visualization tool in Wireshark that displays network traffic over time. It plots packets, bytes, or custom metrics on a timeline, allowing you to see patterns, spikes, and anomalies in your captured data.

      
        
Key Components
==============

  Element	What It Does
  ---------------------
   X-Axis	         -      Time (seconds/minutes/hours)
   Y-Axis     	   -     Traffic volume (packets/sec, bytes/sec, etc.)
   Graph Lines	   -    Different traffic types you define (up to 5)
   Interval	       -   Time bucket size (default 1 sec)


   Configurable Settings
   ----------------------
- Display Filter: What traffic to include (e.g., http, tcp.flags.syn==1)

- Style: Line, Bar, Impulse, Dot

- Y Axis: Packets, Bytes, Bits, or custom fields

- Color: Visual distinction between graphs

- SMA Period: Smoothing to show trends through noise

- Used Wireshark I/O graphs with SMA smoothing to visualize trends hidden in raw packets, allowing comparison of multiple traffic types simultaneously. Detected patterns such as steady lines for normal traffic, spikes for DoS or port scans, sawtooth shapes for congestion, and drops indicating application issues, enabling quick identification of attacks and pinpointing problem times directly from the graph.


- IN THIS PROJECT [REPORT]
  ------------------------

  The Graph showed:

=Blue line: All packets (total traffic)

=Red line: TCP errors (retransmissions spiking with load)

=Green line: Port 80 traffic (confirming HTTP target)

=The pattern proved your traffic simulator successfully overwhelmed the server

=Present findings visually in reports




 🖧"The I/O graph shows the traffic pattern generated by the multi-threaded Python script. Blue peaks represent bursts of HTTP requests from concurrent threads, reaching 500-600 packets per second. Red TCP error spikes during these peaks confirm the server experienced load sufficient to trigger retransmissions, demonstrating a successful traffic simulation that pushed the target beyond its comfortable processing capacity."
                
 







 
