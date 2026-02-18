# Wireshark_Traffic_Analysis_Lab - Network Traffic Analysis Laboratory: Capturing & Analyzing ICMP, TCP, and HTTP Traffic with Wireshark

Project Overview

🔹This laboratory project provides a hands-on examination of network communications by capturing and analyzing live traffic between two Linux-based systems. Using Wireshark as the primary analysis tool, I established a controlled testing environment consisting of a Kali Linux machine (acting as the source/attacker) and an Ubuntu machine (acting as the target/victim) to observe, filter, and interpret various network protocols at the packet level.

🔹The objective was to move beyond theoretical networking concepts by visualizing real-time data transmission, understanding protocol behaviors, and identifying security implications observable through traffic analysis. Throughout this project, I systematically generated and captured multiple traffic types to build a comprehensive understanding of how data moves across networks and how malicious activities can be detected.

🔍 Traffic Analysis Fundamentals

🔹ICMP Traffic Analysis: Generated and analyzed ping requests/responses between Kali and Ubuntu systems

🔹Wireshark Graph Utilization: Created and interpreted various Wireshark graphs (I/O Graphs, Flow Graphs) to visualize network traffic patterns

🔹Packet Filtering: Implemented display and capture filters to isolate specific traffic types and reduce noise

📡 Network Protocols & Communications

🔹TCP Three-Way Handshake: Captured and analyzed the complete SYN, SYN-ACK, ACK handshake process

🔹HTTP Traffic: Monitored and inspected unencrypted HTTP request/response cycles

🔹Packet-Level Analysis: Examined packet headers, payloads, and protocol-specific fields

🔐 Security Assessment Techniques

🔹SYN Scanning: Performed and identified port scanning activities, understanding how attackers map network services

🔹Traffic Pattern Recognition: Distinguished between legitimate traffic and potential malicious activities

Technical Environment

🔹Attack Machine: Kali Linux

🔹Target Machine: Ubuntu Linux

🔹Analysis Tool: Wireshark Network Protocol Analyzer


  🌐 PROJECT SUMMARY 

  1. Bridged Adapter - Was Necessary - Bridged Adapter makes your virtual machines act as separate devices on your physical network (like having two additional computers connected to your router,IP of both kali (attacker machine) and Ubuntu (target machine) was checked after setting it to Bridged Adapter.
   

  2. ICMP Traffic (ping) - Was the first Traffic I analyzed Where I was using Kali Linux to Ping Ubuntu's IP and analyzed Wireshark To Monitor The ICMP packets.
   


  3. TCP handshake - I was able to capture TCP(trasmission control protocol) Using Wireshark In Ubuntu While I Performed a Network Scanning Using Nmap,A Basic Versions scan can cause alot of Noise which make scanning detectable ,But when  Nmap Timing Templates is used it can make the scan Stealth/Evasion,The ones you want for slow, undetectable scanning are

   

 4. SYN scanning - Performing a Nmap Network SYN scanning If the victim is running Wireshark on their device while you perform an Nmap scan, they can definitely see and identify the scan.There are  Specific
Wireshark Filters to Detect Scans example: tcp.flags.syn == 1 && tcp.flags.ack == 0 - shows all SYN packets from potential scanner,ip.src == 192.168.1.10 - This helps us to See all traffic from the suspicious IP.



 5. HTTP requests - Since I was practicing This Project in a isolation environments,Using my own Home lab,I Had done a DOS attack from Kali Linux Using a tool called DDOS-RIPPER,This made me curious that what would happen when i did a DOS Attack on myself for educations purpose,Which ended up making me research more about HTTP Protocol.When a DOS attack is perform on a websites Which is protected By Web Application Firewall (WAF),DDoS Mitigation Service / CDN (Edge Network),Content Delivery Network (CDN) The TCP packets which is captured When you flood a server with HTTP requests.Server resources (CPU, memory, connection slots) get exhausted.Kernel network queue fills up.Network interface becomes saturated,Application (web server) can't process requests fast enough."TCP Retransmission" - Same packet sent again



6.Wireshark Packet Filtering - Packet filtering in Wireshark allows you to isolate specific traffic from large packet captures, making analysis manageable and focused.If the filter is Applied before capturing packets It would only capture the packets which is needed and Only matching packets are stored 

Common Protocol Filters
 
  🖧 HTTP Filters  = http : Show all HTTP traffic    ip.src == 192.168.1.10 and http :  Show HTTP traffic from specific IP
  🖧 SYN Packet Filters = tcp.flags.syn == 1 and tcp.flags.ack == 0 : Show all SYN packets (without ACK)  ,  tcp.flags.syn == 1 :  Show all SYN packets (including SYN-ACK)
  🖧 ACK Packet Filters = tcp.flags.ack == 1 :  Show all ACK packets  ,  ip.addr == 192.168.1.10 and ip.addr == 192.168.1.100 and tcp.flags.ack == 1 : Show ACK packets in a specific conversation
  🖧 Normal HTTP Traffic = http and ip.addr == 192.168.1.10 and ip.addr == 192.168.1.100 :  Show complete HTTP conversation  ,  tcp.flags.syn == 1 and ip.addr == 192.168.1.10 or ip.addr == 192.168.1.100 : Show TCP handshake before HTTP 


  7.Basic Traffic Analysis - Basic traffic analysis refers to the fundamental skill of examining network packets to understand what is happening on the network, identify communication patterns, and detect normal     vs. abnormal behavior.After completing this project I could look at the captured packets and extracting meaningful information without advanced tools—just observing, filtering, and interpreting confidently.I'm Knowledgeable about Packet Examination or Identification ,  ICMP Traffic Analysis (Ping) ,  TCP Handshake Analysis , SYN Scanning Analysis ,  HTTP Traffic Analysis ,  Packet Filtering Practice by doing this projects.

   
   
  🐧 PYTHON TRAFFIC SIMULATOR SCRIPT USED FOR THE PROJECT
   Purpose  -  A multi-threaded Python script designed to generate HTTP traffic for network analysis and DoS simulation in a controlled lab environment

              Key Features
🐍Component	                     Description
🐍Language	        -      Python 3 with socket and threading libraries
🐍Target	          -      Ubuntu victim machine (IP: 192.168.x.x, Port: 80)
🐍Traffic Type	    -      HTTP GET requests to root directory
🐍Concurrency	      -      10 simultaneous threads
🐍Request Volume	  -      100 requests per thread (1000 total requests)

🐧 This Simulates Light traffic load on web server and Multiple concurrent connections from single source It Uses Raw socket communication (bypasses browser/curl) and Basic HTTP flood pattern for DoS analysis
   
🐧 Wireshark Observations - When running this script from Kali to Ubuntu, Wireshark captures packets Rapidly TCP handshakes (SYN, SYN-ACK, ACK).HTTP GET requests , TCP connection terminations,Pattern of requests from same source IP can be identify and Using iptables (native Linux firewall) on your Ubuntu machine you can block a specific IP if needed so packets are'nt send to you.
                
 







 
