#!/usr/bin/env python3
"""
HCIA-Security Comprehensive Question Bank Generator
Generates a single .tex file with >1000 exam questions:
  - Single-answer questions
  - Multi-answer questions
  - True/False questions
Each question includes a concise concept explanation.
"""

import os
import re

# ---------------------------------------------------------------------------
# LaTeX helpers
# ---------------------------------------------------------------------------

def tex_escape(text):
    """Escape characters that are special in LaTeX."""
    if text is None:
        return ""
    # Must process backslash first
    text = text.replace('\\', '\\textbackslash{}')
    conv = {
        '{': '\\{',
        '}': '\\}',
        '$': '\\$',
        '&': '\\&',
        '#': '\\#',
        '^': '\\textasciicircum{}',
        '_': '\\_',
        '~': '\\textasciitilde{}',
        '%': '\\%',
    }
    for k, v in conv.items():
        text = text.replace(k, v)
    return text


class Q:
    def __init__(self, qtype, topic, question, options, answer, explanation):
        self.qtype = qtype          # 'single', 'multi', 'tf'
        self.topic = topic
        self.question = question
        self.options = options      # list of strings
        self.answer = answer        # string like 'B' or 'A,C,D'
        self.explanation = explanation


questions = []

def add(qtype, topic, question, options, answer, explanation):
    questions.append(Q(qtype, topic, question, options, answer, explanation))


# =============================================================================
# CHAPTER 1: Network Security Concepts and Specifications
# =============================================================================

add('single', 'Network Security Concepts',
    'In a broad sense, network security refers to:',
    ['Physical security of devices only',
     'Cybersecurity / cyberspace security at a national level',
     'Only firewall deployment',
     'Only antivirus protection'],
    'B',
    'Broadly, network security is synonymous with cybersecurity, covering national laws, regulations, and processes to protect cyberspace.')

add('single', 'Network Security Concepts',
    'In a narrow sense, network security focuses on:',
    ['National cyberspace policies only',
     'Vendor devices and solutions that ensure secure running of enterprise networks',
     'Only social engineering defense',
     'Only data-center cooling'],
    'B',
    'In a narrow sense, network security refers to measures such as firewalls, IPS, VPNs, and policies that protect enterprise networks.')

add('single', 'Network Security Concepts',
    'Which period of security history mainly used stream ciphers and physical protection?',
    ['Information security period', 'Communication security period', 'Cyberspace security period', 'Information assurance period'],
    'B',
    'The communication security period (1940s) relied on physical security and cryptographic communication, mainly stream ciphers.')

add('single', 'Network Security Concepts',
    'During the information security period, which three goals were the main focus?',
    ['Confidentiality, integrity, availability', 'Speed, bandwidth, latency', 'Power, cooling, cabling', 'Routing, switching, NAT'],
    'A',
    'The classic CIA triad — confidentiality, integrity, and availability — became the core objectives of information security.')

add('single', 'Network Security Concepts',
    'Which two properties were added to the CIA triad during the information assurance period?',
    ['Controllability and non-repudiation', 'Speed and redundancy', 'Encryption and hashing', 'NAT and VLAN'],
    'A',
    'In the information assurance period, controllability (monitoring and control) and non-repudiation (proof of actions) joined the CIA triad.')

add('single', 'Network Security Concepts',
    'The cyberspace security period aims to protect:',
    ['Only web servers', 'Only user passwords', 'Facilities, data, users, and operations across cyberspace', 'Only email gateways'],
    'C',
    'Cyberspace security expands protection to the entire digital ecosystem: facilities, data, users, and operations.')

add('single', 'Network Security Standards',
    'ISO 27001 specifies requirements for:',
    ['An information security management system (ISMS)', 'A firewall hardware model', 'A routing protocol', 'A programming language'],
    'A',
    'ISO/IEC 27001 is the international standard for establishing, implementing, maintaining, and continually improving an ISMS.')

add('single', 'Network Security Standards',
    'ISO 27002 is best described as:',
    ['A certification standard', 'A code of practice with security controls', 'A firewall configuration guide', 'A wireless protocol'],
    'B',
    'ISO/IEC 27002 provides best-practice security controls, while ISO 27001 is the certifiable requirements standard.')

add('single', 'Network Security Standards',
    'Cybersecurity Classified Protection 2.0 is issued by:',
    ['Huawei', 'China (as a national standard/policy)', 'IEEE', 'IETF'],
    'B',
    'Classified Protection 2.0 is a Chinese national cybersecurity baseline and compliance framework.')

add('single', 'Network Security Standards',
    'Classified Protection 2.0 uses a protection-level scale from:',
    ['Level 1 to Level 5', 'Level 0 to Level 4', 'Level A to Level E', 'Level I to Level V'],
    'A',
    'The Chinese classified protection system defines five levels, with Level 5 being the highest.')

add('single', 'Network Security Standards',
    'Which of the following is NOT a typical Classified Protection 2.0 lifecycle phase?',
    ['Classification', 'Filing', 'Construction and rectification', 'Marketing and sales'],
    'D',
    'The Classified Protection lifecycle includes classification, filing, construction/rectification, level assessment, and supervision/inspection.')

add('multi', 'Network Security Concepts',
    'Which of the following are characteristics of network security? (Choose all that apply)',
    ['Confidentiality', 'Integrity', 'Availability', 'Controllability', 'Non-repudiation'],
    'A,B,C,D,E',
    'Network security commonly encompasses confidentiality, integrity, availability, controllability, and non-repudiation.')

add('multi', 'Network Security Standards',
    'Which are typical Classified Protection 2.0 lifecycle phases? (Choose all that apply)',
    ['Classification', 'Filing', 'Construction and rectification', 'Level assessment', 'Supervision and inspection'],
    'A,B,C,D,E',
    'The full lifecycle includes classification, filing, construction/rectification, level assessment, and supervision/inspection.')

add('tf', 'Network Security Concepts',
    'Network security in the narrow sense only refers to national cybersecurity laws.',
    ['True', 'False'], 'False',
    'Narrow-sense network security covers vendor solutions and enterprise network protection, not only national laws.')

add('tf', 'Network Security Concepts',
    'The CIA triad includes confidentiality, integrity, and availability.',
    ['True', 'False'], 'True',
    'Confidentiality, integrity, and availability are the three foundational goals of information security.')

add('tf', 'Network Security Standards',
    'ISO 27002 can be used to certify an enterprise information security system.',
    ['True', 'False'], 'False',
    'ISO 27001 is the certification standard; ISO 27002 is a code of practice with controls.')

add('tf', 'Network Security Standards',
    'Classified Protection 2.0 defines protection levels from Level 1 to Level 5.',
    ['True', 'False'], 'True',
    'Classified Protection 2.0 uses five levels, with higher levels requiring stronger controls and oversight.')

add('tf', 'Network Security Standards',
    'Network operators can always determine the final protection level on their own without review.',
    ['True', 'False'], 'False',
    'For Level 2 and above, expert review and approval are required; only Level 1 can be determined by the operator.')

add('tf', 'Network Security Concepts',
    'Building network security helps enterprises reduce losses from attacks.',
    ['True', 'False'], 'True',
    'Security controls reduce the impact of breaches, downtime, and data loss, thereby lowering financial losses.')


# =============================================================================
# CHAPTER 2: Network Fundamentals
# =============================================================================

add('single', 'OSI and TCP/IP Models',
    'How many layers does the OSI reference model have?',
    ['4', '5', '7', '9'], 'C',
    'The OSI model has seven layers: physical, data link, network, transport, session, presentation, and application.')

add('single', 'OSI and TCP/IP Models',
    'How many layers does the TCP/IP standard model have?',
    ['4', '5', '6', '7'], 'A',
    'The TCP/IP standard model has four layers: network interface, internet, transport, and application.')

add('single', 'OSI and TCP/IP Models',
    'Which layer is responsible for end-to-end communication and flow control?',
    ['Network layer', 'Transport layer', 'Data link layer', 'Physical layer'], 'B',
    'The transport layer provides end-to-end communication, reliability, and flow control (e.g., TCP).')

add('single', 'OSI and TCP/IP Models',
    'Which layer handles logical addressing and routing?',
    ['Transport layer', 'Network layer', 'Session layer', 'Presentation layer'], 'B',
    'The network layer uses logical addresses (IP) and routes packets between networks.')

add('single', 'OSI and TCP/IP Models',
    'Which layer is responsible for framing, MAC addressing, and error detection on a local link?',
    ['Network layer', 'Transport layer', 'Data link layer', 'Application layer'], 'C',
    'The data link layer handles framing, MAC addresses, and local link error detection.')

add('single', 'Network Protocols',
    'Which protocol uses ports 20 and 21 for file transfer?',
    ['HTTP', 'FTP', 'SMTP', 'DNS'], 'B',
    'FTP uses TCP port 21 for control and port 20 for data transfer.')

add('single', 'Network Protocols',
    'Which protocol resolves domain names to IP addresses?',
    ['DHCP', 'DNS', 'SNMP', 'NTP'], 'B',
    'DNS (Domain Name System) maps human-readable domain names to IP addresses.')

add('single', 'Network Protocols',
    'Which transport protocol is connection-oriented and reliable?',
    ['UDP', 'TCP', 'ICMP', 'IP'], 'B',
    'TCP provides connection-oriented, reliable, ordered delivery with flow and congestion control.')

add('single', 'Network Protocols',
    'Which transport protocol is connectionless and has low overhead?',
    ['TCP', 'UDP', 'HTTP', 'FTP'], 'B',
    'UDP is connectionless, offers low latency and overhead, but does not guarantee delivery.')

add('single', 'Network Devices',
    'Which device operates at Layer 2 and forwards frames based on MAC addresses?',
    ['Router', 'Switch', 'Hub', 'Firewall'], 'B',
    'A switch operates at the data link layer and forwards frames using MAC address tables.')

add('single', 'Network Devices',
    'Which device operates at Layer 3 and forwards packets based on IP addresses?',
    ['Switch', 'Router', 'Hub', 'Bridge'], 'B',
    'A router operates at the network layer and makes forwarding decisions based on IP routing tables.')

add('single', 'Network Devices',
    'Which device simply repeats signals to all connected ports?',
    ['Switch', 'Router', 'Hub', 'Firewall'], 'C',
    'A hub is a Layer 1 device that broadcasts signals to all connected devices.')

add('multi', 'OSI and TCP/IP Models',
    'Which layers are part of the OSI model? (Choose all that apply)',
    ['Physical', 'Data link', 'Network', 'Transport', 'Application'],
    'A,B,C,D,E',
    'The OSI model includes physical, data link, network, transport, session, presentation, and application layers.')

add('multi', 'Network Protocols',
    'Which protocols operate at the application layer? (Choose all that apply)',
    ['HTTP', 'FTP', 'DNS', 'SMTP'], 'A,B,C,D',
    'HTTP, FTP, DNS, and SMTP are all application-layer protocols.')

add('multi', 'Network Devices',
    'Which devices can operate at Layer 2? (Choose all that apply)',
    ['Switch', 'Bridge', 'Router', 'Hub'], 'A,B',
    'Switches and bridges operate at the data link layer; routers are Layer 3 and hubs are Layer 1.')

add('tf', 'OSI and TCP/IP Models',
    'The TCP/IP model combines the OSI session and presentation layers into the application layer.',
    ['True', 'False'], 'True',
    'The TCP/IP model does not have separate session and presentation layers; their functions are included in the application layer.')

add('tf', 'Network Protocols',
    'UDP guarantees ordered delivery of packets.',
    ['True', 'False'], 'False',
    'UDP is connectionless and does not guarantee delivery, ordering, or duplicate protection.')

add('tf', 'Network Devices',
    'A router forwards frames based on MAC addresses.',
    ['True', 'False'], 'False',
    'Routers forward packets based on IP addresses; switches forward frames based on MAC addresses.')

add('tf', 'Network Devices',
    'A switch creates a separate collision domain for each port.',
    ['True', 'False'], 'True',
    'Each switch port is its own collision domain, reducing collisions compared to a hub.')


# =============================================================================
# CHAPTER 3: Enterprise Network Security Threats
# =============================================================================

add('single', 'Security Threats Overview',
    'Which of the following is an example of a passive attack?',
    ['Modifying data', 'Eavesdropping', 'Deleting files', 'Denial of service'], 'B',
    'Eavesdropping/sniffing is a passive attack because it does not alter data or system state.')

add('single', 'Security Threats Overview',
    'Which of the following is an active attack?',
    ['Traffic sniffing', 'Data tampering', 'Port scanning only', 'Banner grabbing'], 'B',
    'Active attacks involve modifying, disrupting, or gaining unauthorized access to systems or data.')

add('single', 'Security Threats Overview',
    'What type of threat aims to make a service unavailable to legitimate users?',
    ['Malware', 'Denial of Service', 'Phishing', 'Spam'], 'B',
    'Denial of Service (DoS) and Distributed DoS (DDoS) attacks aim to exhaust resources and disrupt service.')

add('single', 'Security Threats Overview',
    'Which threat category includes viruses, worms, and Trojans?',
    ['Social engineering', 'Malware', 'Spoofing', 'Phishing'], 'B',
    'Malware is malicious software, including viruses, worms, Trojans, ransomware, and spyware.')

add('single', 'Communication Network Security',
    'Which threat involves intercepting data traveling across a network?',
    ['Eavesdropping', 'DoS', 'Phishing', 'Tailgating'], 'A',
    'Eavesdropping intercepts network communications to steal information.')

add('single', 'Zone Border Security',
    'What is the main purpose of a security zone?',
    ['Increase Internet speed', 'Group interfaces with similar security levels', 'Replace antivirus', 'Disable routing'], 'B',
    'Security zones group network interfaces with similar trust levels to enforce inter-zone policies.')

add('single', 'Zone Border Security',
    'Which device is typically deployed at a zone border to enforce access control?',
    ['Hub', 'Firewall', 'Repeater', 'Bridge'], 'B',
    'Firewalls are deployed at network boundaries to enforce security policies between zones.')

add('single', 'Computing Environment Security',
    'Which control helps protect endpoints from malware?',
    ['Antivirus/EDR', 'Physical locks only', 'Hub replacement', 'Disabling DNS'], 'A',
    'Antivirus and endpoint detection and response (EDR) protect hosts from malware and suspicious behavior.')

add('multi', 'Security Threats Overview',
    'Which are common network security threats? (Choose all that apply)',
    ['Malware', 'Phishing', 'DoS/DDoS', 'Data leakage', 'Insider threats'], 'A,B,C,D,E',
    'Common threats include malware, phishing, denial of service, data leakage, and insider threats.')

add('multi', 'Zone Border Security',
    'Which controls are typically applied at zone borders? (Choose all that apply)',
    ['Firewall policies', 'NAT', 'IPS/IDS', 'VPN termination'], 'A,B,C,D',
    'Zone borders commonly use firewalls, NAT, IPS/IDS, and VPN gateways for protection.')

add('tf', 'Security Threats Overview',
    'A passive attack modifies data in transit.',
    ['True', 'False'], 'False',
    'Passive attacks only monitor or capture data; active attacks modify or disrupt data.')

add('tf', 'Security Threats Overview',
    'Malware includes viruses, worms, and Trojans.',
    ['True', 'False'], 'True',
    'Malware is a broad category that includes viruses, worms, Trojans, ransomware, and spyware.')

add('tf', 'Communication Network Security',
    'Encryption is an effective way to protect data confidentiality over public networks.',
    ['True', 'False'], 'True',
    'Encryption ensures that intercepted data cannot be read without the proper key.')

add('tf', 'Zone Border Security',
    'A firewall at the zone border can enforce security policies between trusted and untrusted networks.',
    ['True', 'False'], 'True',
    'Firewalls inspect and control traffic crossing security zone boundaries based on policy.')


# =============================================================================
# CHAPTER 4: Firewall Basics
# =============================================================================

add('single', 'Security Zones',
    'What is the default priority of the Trust zone on a Huawei firewall?',
    ['5', '50', '85', '100'], 'C',
    'The Trust zone has a default priority of 85.')

add('single', 'Security Zones',
    'What is the default priority of the DMZ zone on a Huawei firewall?',
    ['5', '50', '85', '100'], 'B',
    'The DMZ zone has a default priority of 50.')

add('single', 'Security Zones',
    'What is the default priority of the Untrust zone on a Huawei firewall?',
    ['5', '50', '85', '100'], 'A',
    'The Untrust zone has a default priority of 5.')

add('single', 'Security Zones',
    'What is the default priority of the Local zone on a Huawei firewall?',
    ['5', '50', '85', '100'], 'D',
    'The Local zone represents the firewall itself and has the highest default priority of 100.')

add('single', 'Security Policies',
    'What is the default action of a Huawei firewall security policy if no rule matches?',
    ['Permit', 'Deny', 'Log only', 'Redirect'], 'B',
    'By default, unmatched traffic is denied.')

add('single', 'Security Policies',
    'Which components can be used as matching conditions in a security policy? (single best answer)',
    ['Source/destination zone, address, service, application, user, time',
     'Only source IP', 'Only destination port', 'Only protocol'], 'A',
    'Security policies can match on zones, addresses, users, services, applications, and time.')

add('single', 'Stateful Inspection',
    'What is a session table used for in a stateful firewall?',
    ['Storing user passwords', 'Tracking established connections', 'Routing packets', 'Encrypting traffic'], 'B',
    'The session table tracks connection state so return traffic can be permitted without a new policy lookup.')

add('single', 'Stateful Inspection',
    'Which type of firewall inspects packets individually without connection state?',
    ['Stateful firewall', 'Packet-filtering firewall', 'Proxy firewall', 'Next-generation firewall'], 'B',
    'Packet-filtering firewalls inspect each packet independently based on header information.')

add('single', 'ASPF',
    'What does ASPF stand for?',
    ['Advanced Stateful Packet Filtering', 'Application Specific Packet Filtering',
     'Automatic Security Policy Forwarding', 'Advanced Stateful Policy Firewall'], 'B',
    'ASPF is Application Specific Packet Filtering, used to inspect multi-channel protocols.')

add('single', 'ASPF',
    'Why is ASPF needed for protocols like FTP?',
    ['FTP only uses one port', 'FTP opens dynamic data channels', 'FTP encrypts all traffic', 'FTP does not use TCP'], 'B',
    'FTP opens a dynamic data channel, and ASPF inspects the control channel to permit the negotiated data channel.')

add('multi', 'Security Zones',
    'Which are default security zones on Huawei firewalls? (Choose all that apply)',
    ['Trust', 'Untrust', 'DMZ', 'Local'], 'A,B,C,D',
    'Huawei firewalls provide four default zones: Trust, Untrust, DMZ, and Local.')

add('multi', 'Security Policies',
    'Which elements can be referenced in a security policy? (Choose all that apply)',
    ['Security zones', 'IP addresses/address groups', 'Services', 'Users and user groups', 'Time ranges'], 'A,B,C,D,E',
    'Security policies can reference zones, addresses, services, users, applications, and time ranges.')

add('multi', 'Stateful Inspection',
    'Which are advantages of stateful inspection over simple packet filtering? (Choose all that apply)',
    ['Tracks connection state', 'Allows return traffic automatically', 'Better performance for established sessions', 'Can inspect application-layer payloads'], 'A,B,C',
    'Stateful inspection tracks connections, permits return traffic, and improves performance; deep payload inspection is more advanced.')

add('tf', 'Security Zones',
    'The Local zone represents traffic destined to or originated from the firewall itself.',
    ['True', 'False'], 'True',
    'Local zone traffic involves the firewall services and management interfaces.')

add('tf', 'Security Policies',
    'By default, Huawei firewalls permit all traffic unless a policy explicitly denies it.',
    ['True', 'False'], 'False',
    'The default action is to deny traffic unless a security policy explicitly permits it.')

add('tf', 'Stateful Inspection',
    'A stateful firewall can allow return traffic for an established session without a separate policy.',
    ['True', 'False'], 'True',
    'Return packets matching an existing session table entry are permitted automatically.')

add('tf', 'ASPF',
    'ASPF is used to support protocols that open secondary or dynamic connections.',
    ['True', 'False'], 'True',
    'ASPF inspects application-layer negotiation to dynamically permit related channels.')


# =============================================================================
# CHAPTER 5: NAT
# =============================================================================

add('single', 'NAT Basics',
    'What does NAT primarily translate?',
    ['MAC addresses', 'IP addresses', 'Port numbers only', 'Domain names'], 'B',
    'NAT translates IP addresses, typically between private and public addresses.')

add('single', 'Source NAT',
    'Which NAT type translates the source IP address of outgoing packets?',
    ['Source NAT', 'Destination NAT', 'Bidirectional NAT', 'NAT Server'], 'A',
    'Source NAT changes the source IP so internal hosts can use public addresses to access the Internet.')

add('single', 'Source NAT',
    'What is the main purpose of NAPT?',
    ['Translate many private addresses to one public IP using port multiplexing',
     'Hide the destination IP', 'Encrypt traffic', 'Provide VPN access'], 'A',
    'NAPT (Network Address and Port Translation) maps multiple private addresses to a single public IP using different ports.')

add('single', 'Destination NAT',
    'Which NAT type translates the destination IP address of incoming packets?',
    ['Source NAT', 'Destination NAT', 'Bidirectional NAT', 'NAT Server'], 'B',
    'Destination NAT rewrites the destination IP, often to expose internal servers to external users.')

add('single', 'NAT Server',
    'What is a NAT Server used for?',
    ['Hiding internal server IP addresses', 'Publishing internal services to the Internet',
     'Encrypting server traffic', 'Load balancing only'], 'B',
    'NAT Server maps public IPs/ports to private server IPs/ports so external users can access internal services.')

add('single', 'NAT ALG',
    'What is the purpose of NAT ALG?',
    ['Encrypt NAT traffic', 'Translate application-layer addresses embedded in protocol payloads',
     'Replace firewalls', 'Assign IP addresses'], 'B',
    'NAT Application Level Gateway inspects and rewrites IP addresses inside application-layer protocols (e.g., FTP, SIP).')

add('multi', 'NAT Basics',
    'Which are types of NAT supported by Huawei firewalls? (Choose all that apply)',
    ['Source NAT', 'Destination NAT', 'Bidirectional NAT', 'NAT Server'], 'A,B,C,D',
    'Huawei firewalls support source NAT, destination NAT, bidirectional NAT, and NAT server.')

add('multi', 'Source NAT',
    'Which are common source NAT modes? (Choose all that apply)',
    ['NAT No-PAT', 'NAPT', 'Easy-IP', 'NAT Server'], 'A,B,C',
    'Source NAT includes NAT No-PAT (one-to-one), NAPT (many-to-one), and Easy-IP (interface-based).')

add('multi', 'NAT ALG',
    'Which protocols may require NAT ALG? (Choose all that apply)',
    ['FTP', 'SIP', 'H.323', 'DNS'], 'A,B,C',
    'Protocols embedding address/port information in payloads (FTP, SIP, H.323) need NAT ALG.')

add('tf', 'NAT Basics',
    'NAT can conserve public IPv4 addresses.',
    ['True', 'False'], 'True',
    'NAT allows many private hosts to share a smaller number of public IP addresses.')

add('tf', 'Source NAT',
    'NAPT translates both IP addresses and port numbers.',
    ['True', 'False'], 'True',
    'NAPT multiplexes many private addresses onto one public IP by translating ports.')

add('tf', 'Destination NAT',
    'Destination NAT is typically used for outbound Internet access.',
    ['True', 'False'], 'False',
    'Destination NAT is used for inbound traffic to expose internal services.')

add('tf', 'NAT Server',
    'NAT Server maps public IP addresses to private server addresses.',
    ['True', 'False'], 'True',
    'NAT Server publishes internal services by mapping public IPs/ports to private servers.')

add('tf', 'NAT ALG',
    'NAT ALG is needed when protocols embed IP addresses inside application payloads.',
    ['True', 'False'], 'True',
    'ALG inspects application-layer data to update embedded addresses/ports.')


# =============================================================================
# CHAPTER 6: Firewall Hot Standby
# =============================================================================

add('single', 'VRRP',
    'What does VRRP stand for?',
    ['Virtual Router Redundancy Protocol', 'Virtual Routing Resolution Protocol',
     'Virtual Redundant Routing Path', 'Virtual Routing Relay Protocol'], 'A',
    'VRRP provides gateway redundancy by allowing multiple routers to share a virtual IP address.')

add('single', 'VRRP',
    'In VRRP, which router forwards traffic for the virtual IP?',
    ['Backup router', 'Master router', 'All routers simultaneously', 'Only the physical IP owner'], 'B',
    'The VRRP master router owns the virtual IP and forwards traffic; backups take over if it fails.')

add('single', 'VGMP',
    'What does VGMP manage on Huawei firewalls?',
    ['VRRP groups', 'NAT pools', 'Routing tables', 'DHCP scopes'], 'A',
    'VGMP (VRRP Group Management Protocol) manages the state of multiple VRRP groups consistently.')

add('single', 'HRP',
    'What is the primary purpose of HRP?',
    ['Encrypt traffic', 'Synchronize sessions and configurations between firewalls',
     'Assign IP addresses', 'Filter URLs'], 'B',
    'HRP (Huawei Redundancy Protocol) synchronizes sessions, configurations, and state between hot-standby firewalls.')

add('single', 'Firewall Hot Standby',
    'In active/standby mode, how many firewalls forward traffic at the same time?',
    ['One', 'Two', 'All', 'None'], 'A',
    'In active/standby mode, one firewall actively forwards while the other remains standby.')

add('single', 'Firewall Hot Standby',
    'In load-sharing mode, how many firewalls forward traffic?',
    ['One', 'Two or more', 'None', 'Only the backup'], 'B',
    'Load-sharing mode allows multiple firewalls to forward traffic simultaneously.')

add('multi', 'VRRP',
    'Which are VRRP roles? (Choose all that apply)',
    ['Master', 'Backup', 'Initialize', 'Failover'], 'A,B,C',
    'VRRP devices can be in master, backup, or initialize states.')

add('multi', 'HRP',
    'Which data does HRP synchronize? (Choose all that apply)',
    ['Session table', 'NAT entries', 'Server-map entries', 'Configurations'], 'A,B,C,D',
    'HRP synchronizes sessions, NAT entries, server-map entries, and configurations.')

add('tf', 'VRRP',
    'VRRP uses a virtual IP address shared between multiple physical routers.',
    ['True', 'False'], 'True',
    'VRRP allows multiple routers to present a single virtual gateway IP to hosts.')

add('tf', 'VGMP',
    'VGMP ensures that VRRP groups on a firewall switch state consistently.',
    ['True', 'False'], 'True',
    'VGMP prevents split-brain scenarios by managing all VRRP groups as a single entity.')

add('tf', 'HRP',
    'HRP only synchronizes configuration files, not session tables.',
    ['True', 'False'], 'False',
    'HRP synchronizes both configurations and runtime state such as session tables.')

add('tf', 'Firewall Hot Standby',
    'In active/standby mode, both firewalls actively forward the same traffic.',
    ['True', 'False'], 'False',
    'Only the active firewall forwards traffic; the standby takes over upon failure.')


# =============================================================================
# CHAPTER 7: Intrusion Prevention and Antivirus
# =============================================================================

add('single', 'Intrusion Overview',
    'What is an intrusion?',
    ['Authorized access', 'Unauthorized access or attack on a network/system',
     'A software patch', 'A backup operation'], 'B',
    'An intrusion is any unauthorized attempt to access, manipulate, or harm a system or network.')

add('single', 'Intrusion Prevention',
    'What is the main difference between IDS and IPS?',
    ['IDS only detects; IPS detects and blocks', 'IDS is faster', 'IPS cannot log', 'IDS operates inline'], 'A',
    'IDS detects intrusions and alerts; IPS can also take action to block malicious traffic.')

add('single', 'Intrusion Prevention',
    'Which detection method compares traffic against known attack signatures?',
    ['Anomaly detection', 'Signature detection', 'Behavioral analysis', 'Heuristic detection'], 'B',
    'Signature-based detection matches traffic patterns against a database of known attack signatures.')

add('single', 'Intrusion Prevention',
    'Which detection method builds a baseline of normal behavior and flags deviations?',
    ['Signature detection', 'Anomaly detection', 'Static analysis', 'Port scanning'], 'B',
    'Anomaly detection identifies traffic that deviates from a learned baseline.')

add('single', 'Intrusion Prevention',
    'Where is an IPS typically deployed?',
    ['Out-of-band only', 'Inline in the traffic path', 'On user desktops only', 'Inside a printer'], 'B',
    'IPS is deployed inline so it can block malicious traffic in real time.')

add('single', 'Antivirus',
    'What does antivirus software primarily detect and remove?',
    ['Routing loops', 'Malware', 'Cable faults', 'DNS errors'], 'B',
    'Antivirus detects and removes malware such as viruses, worms, and Trojans.')

add('single', 'Antivirus',
    'Which antivirus technique looks for known byte sequences of malware?',
    ['Heuristic analysis', 'Signature scanning', 'Sandboxing', 'Whitelisting'], 'B',
    'Signature scanning matches files/traffic against known malware signatures.')

add('single', 'Antivirus',
    'Which method executes suspicious files in an isolated environment to observe behavior?',
    ['Signature scanning', 'Heuristic analysis', 'Sandboxing', 'Whitelisting'], 'C',
    'Sandboxing runs files in an isolated environment to detect malicious behavior.')

add('multi', 'Intrusion Prevention',
    'Which are common IPS actions? (Choose all that apply)',
    ['Block', 'Permit', 'Reset connection', 'Alert/log'], 'A,C,D',
    'IPS can block malicious traffic, reset connections, and alert/log events.')

add('multi', 'Antivirus',
    'Which are antivirus detection techniques? (Choose all that apply)',
    ['Signature-based', 'Heuristic', 'Sandboxing', 'Behavioral analysis'], 'A,B,C,D',
    'Modern antivirus uses signatures, heuristics, sandboxing, and behavioral analysis.')

add('tf', 'Intrusion Prevention',
    'An IDS is typically deployed inline and can block attacks.',
    ['True', 'False'], 'False',
    'IDS is usually passive/out-of-band and only detects and alerts; IPS blocks inline.')

add('tf', 'Intrusion Prevention',
    'Signature-based IPS can detect zero-day attacks effectively.',
    ['True', 'False'], 'False',
    'Signatures require known attack patterns; zero-day attacks are unknown and often missed.')

add('tf', 'Antivirus',
    'Antivirus signature databases must be updated regularly to detect new malware.',
    ['True', 'False'], 'True',
    'New malware variants require updated signatures and detection engines.')

add('tf', 'Antivirus',
    'Sandboxing can detect unknown malware by observing its runtime behavior.',
    ['True', 'False'], 'True',
    'Sandboxing reveals malicious behavior of unknown samples in an isolated environment.')


# =============================================================================
# CHAPTER 8: AAA and User Authentication
# =============================================================================

add('single', 'AAA Basics',
    'What does AAA stand for?',
    ['Authentication, Authorization, Accounting', 'Access, Audit, Alert',
     'Attack, Analysis, Action', 'Application, Authorization, Audit'], 'A',
    'AAA provides authentication (who are you), authorization (what can you do), and accounting (what did you do).')

add('single', 'AAA Basics',
    'Which AAA component verifies a user identity?',
    ['Authentication', 'Authorization', 'Accounting', 'Auditing'], 'A',
    'Authentication verifies identity, for example, by username/password or certificate.')

add('single', 'AAA Basics',
    'Which AAA component determines what resources a user can access?',
    ['Authentication', 'Authorization', 'Accounting', 'Auditing'], 'B',
    'Authorization defines permissions and access rights after authentication.')

add('single', 'AAA Basics',
    'Which AAA component records user activities for billing or auditing?',
    ['Authentication', 'Authorization', 'Accounting', 'Auditing'], 'C',
    'Accounting logs user activities such as login time, data usage, and commands executed.')

add('single', 'Firewall User Authentication',
    'Which authentication method redirects a user to a web portal for login?',
    ['Local authentication', 'RADIUS authentication', 'Portal authentication', 'LDAP authentication'], 'C',
    'Portal authentication presents a web page to users for credential entry.')

add('single', 'Firewall User Authentication',
    'Which authentication method uses a client-side agent to authenticate users before network access?',
    ['Portal authentication', '802.1X authentication', 'Local authentication', 'Certificate authentication'], 'B',
    '802.1X uses a supplicant client to authenticate devices before granting network access.')

add('single', 'Firewall User Authentication',
    'Which protocol is commonly used for centralized authentication and accounting?',
    ['RADIUS', 'SMTP', 'SNMP', 'NTP'], 'A',
    'RADIUS is a widely used AAA protocol for centralized authentication, authorization, and accounting.')

add('single', 'Firewall User Authentication',
    'Which protocol provides authentication with stronger security and uses TCP?',
    ['RADIUS', 'TACACS+', 'LDAP', 'DHCP'], 'B',
    'TACACS+ uses TCP and separates authentication, authorization, and accounting functions.')

add('multi', 'AAA Basics',
    'Which are components of AAA? (Choose all that apply)',
    ['Authentication', 'Authorization', 'Accounting', 'Auditing'], 'A,B,C',
    'AAA consists of authentication, authorization, and accounting.')

add('multi', 'Firewall User Authentication',
    'Which are common firewall authentication methods? (Choose all that apply)',
    ['Local authentication', 'RADIUS', 'LDAP', 'HWTACACS'], 'A,B,C,D',
    'Firewalls support local, RADIUS, LDAP, and HWTACACS authentication.')

add('tf', 'AAA Basics',
    'Authorization determines whether an authenticated user is allowed to perform an action.',
    ['True', 'False'], 'True',
    'Authorization enforces access control decisions based on identity and policy.')

add('tf', 'AAA Basics',
    'Accounting in AAA records user activities and resource usage.',
    ['True', 'False'], 'True',
    'Accounting provides logs for auditing, billing, and forensic analysis.')

add('tf', 'Firewall User Authentication',
    'Portal authentication is commonly used for guest access and web-based login.',
    ['True', 'False'], 'True',
    'Portal authentication provides a convenient web-based login experience.')

add('tf', 'Firewall User Authentication',
    'RADIUS encrypts the entire authentication packet including the username.',
    ['True', 'False'], 'False',
    'RADIUS encrypts only the password field; the rest of the packet is not encrypted.')


# =============================================================================
# CHAPTER 9: Cryptography and PKI
# =============================================================================

add('single', 'Cryptography Basics',
    'Which encryption type uses the same key for encryption and decryption?',
    ['Symmetric encryption', 'Asymmetric encryption', 'Hashing', 'Steganography'], 'A',
    'Symmetric encryption uses a single shared key for both encryption and decryption.')

add('single', 'Cryptography Basics',
    'Which encryption type uses a key pair: public key and private key?',
    ['Symmetric encryption', 'Asymmetric encryption', 'Hashing', 'Encoding'], 'B',
    'Asymmetric encryption uses a public key to encrypt and a private key to decrypt (or vice versa).')

add('single', 'Cryptography Basics',
    'Which algorithm is a symmetric encryption standard?',
    ['RSA', 'AES', 'ECC', 'DSA'], 'B',
    'AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm.')

add('single', 'Cryptography Basics',
    'Which algorithm is an asymmetric encryption algorithm?',
    ['AES', 'DES', 'RSA', '3DES'], 'C',
    'RSA is an asymmetric algorithm used for encryption, digital signatures, and key exchange.')

add('single', 'Hash Algorithms',
    'What is a key property of a cryptographic hash function?',
    ['Reversible output', 'Fixed-length output regardless of input size', 'Requires a public key', 'Uses the same key for hashing and verification'], 'B',
    'Hash functions produce a fixed-length digest for any input size.')

add('single', 'Hash Algorithms',
    'Which hash algorithm produces a 256-bit digest?',
    ['MD5', 'SHA-1', 'SHA-256', 'SHA-512'], 'C',
    'SHA-256 produces a 256-bit hash digest.')

add('single', 'Hash Algorithms',
    'Which hash algorithm is considered broken and unsuitable for security use?',
    ['SHA-256', 'MD5', 'SHA-3', 'BLAKE2'], 'B',
    'MD5 is vulnerable to collision attacks and should not be used for security-sensitive applications.')

add('single', 'Digital Signatures',
    'What is the purpose of a digital signature?',
    ['Encrypt all data', 'Verify authenticity and integrity', 'Compress files', 'Hide sender identity'], 'B',
    'Digital signatures verify the sender identity and ensure data has not been altered.')

add('single', 'PKI',
    'What does PKI stand for?',
    ['Public Key Infrastructure', 'Private Key Interface', 'Packet Knowledge Index', 'Policy Key Identifier'], 'A',
    'PKI provides a framework for managing public keys, certificates, and trust relationships.')

add('single', 'PKI',
    'Which entity issues digital certificates in a PKI?',
    ['Registration Authority', 'Certificate Authority', 'End user', 'Repository'], 'B',
    'A Certificate Authority (CA) issues and signs digital certificates.')

add('single', 'PKI',
    'Which PKI component validates an applicant identity before certificate issuance?',
    ['Certificate Authority', 'Registration Authority', 'Repository', 'CRL'], 'B',
    'A Registration Authority (RA) verifies identities and forwards requests to the CA.')

add('single', 'PKI',
    'What is a CRL used for?',
    ['Storing public keys', 'Listing revoked certificates', 'Encrypting emails', 'Generating hash values'], 'B',
    'A Certificate Revocation List (CRL) contains certificates that have been revoked before expiration.')

add('multi', 'Cryptography Basics',
    'Which are symmetric encryption algorithms? (Choose all that apply)',
    ['AES', 'DES', '3DES', 'RSA'], 'A,B,C',
    'AES, DES, and 3DES are symmetric; RSA is asymmetric.')

add('multi', 'PKI',
    'Which are core PKI components? (Choose all that apply)',
    ['Certificate Authority', 'Registration Authority', 'Certificate repository', 'CRL/OCSP'], 'A,B,C,D',
    'PKI includes CAs, RAs, repositories, and revocation mechanisms such as CRL and OCSP.')

add('tf', 'Cryptography Basics',
    'Symmetric encryption is generally faster than asymmetric encryption.',
    ['True', 'False'], 'True',
    'Symmetric algorithms are faster and suitable for bulk data encryption.')

add('tf', 'Cryptography Basics',
    'Asymmetric encryption is ideal for encrypting large amounts of data directly.',
    ['True', 'False'], 'False',
    'Asymmetric encryption is slower; it is often used for key exchange and signatures, while symmetric encryption handles bulk data.')

add('tf', 'Hash Algorithms',
    'A hash function can be reversed to recover the original input.',
    ['True', 'False'], 'False',
    'Hash functions are one-way; the original input cannot be derived from the digest.')

add('tf', 'PKI',
    'A digital certificate binds a public key to an identity.',
    ['True', 'False'], 'True',
    'Certificates contain a public key and identity information, signed by a trusted CA.')

add('tf', 'PKI',
    'A CRL lists certificates that are still valid.',
    ['True', 'False'], 'False',
    'A CRL lists certificates that have been revoked and should no longer be trusted.')


# =============================================================================
# CHAPTER 10: VPN
# =============================================================================

add('single', 'VPN Overview',
    'What does VPN stand for?',
    ['Virtual Private Network', 'Virtual Public Network', 'Verified Private Node', 'Virtual Protocol Network'], 'A',
    'A VPN extends a private network across a public network using encryption and tunneling.')

add('single', 'VPN Overview',
    'Which benefit does a VPN provide over the public Internet?',
    ['Higher physical speed', 'Confidentiality and secure remote access', 'Free bandwidth', 'No encryption needed'], 'B',
    'VPNs provide confidentiality, integrity, and secure access over untrusted networks.')

add('single', 'VPN Overview',
    'Which VPN type connects individual remote users to a corporate network?',
    ['Site-to-site VPN', 'Remote-access VPN', 'Intranet VPN', 'Extranet VPN'], 'B',
    'Remote-access VPNs allow individual users to securely connect to a corporate network.')

add('single', 'GRE VPN',
    'Which protocol does GRE use as its transport protocol?',
    ['TCP', 'UDP', 'IP protocol 47', 'IP protocol 50'], 'C',
    'GRE encapsulates packets using IP protocol number 47.')

add('single', 'GRE VPN',
    'Which statement about GRE is correct?',
    ['GRE provides encryption by default', 'GRE is a simple tunneling protocol without built-in encryption',
     'GRE cannot tunnel multicast', 'GRE uses UDP port 500'], 'B',
    'GRE provides encapsulation and tunneling but does not provide encryption or authentication by itself.')

add('single', 'IPsec VPN',
    'Which IPsec protocol provides encryption and confidentiality?',
    ['AH', 'ESP', 'IKE', 'GRE'], 'B',
    'ESP (Encapsulating Security Payload) provides encryption, authentication, and integrity.')

add('single', 'IPsec VPN',
    'Which IPsec protocol provides authentication and integrity but not encryption?',
    ['AH', 'ESP', 'IKE', 'L2TP'], 'A',
    'AH (Authentication Header) provides source authentication and integrity but does not encrypt payloads.')

add('single', 'IPsec VPN',
    'Which protocol is used to establish and manage IPsec security associations?',
    ['AH', 'ESP', 'IKE', 'GRE'], 'C',
    'IKE (Internet Key Exchange) negotiates keys and Security Associations for IPsec.')

add('single', 'IPsec VPN',
    'Which IPsec mode encrypts the entire original IP packet and adds a new IP header?',
    ['Transport mode', 'Tunnel mode', 'Gre mode', 'Bridge mode'], 'B',
    'Tunnel mode encapsulates and encrypts the entire original packet, adding a new IP header.')

add('single', 'IPsec VPN',
    'Which IPsec mode encrypts only the payload and is used for host-to-host communications?',
    ['Transport mode', 'Tunnel mode', 'Bridge mode', 'Trunk mode'], 'A',
    'Transport mode encrypts only the IP payload, leaving the original IP header intact.')

add('single', 'L2TP VPN',
    'Which layer-2 tunneling protocol is often combined with IPsec for encryption?',
    ['PPTP', 'L2TP', 'GRE', 'MPLS'], 'B',
    'L2TP provides tunneling and is commonly paired with IPsec to provide encryption.')

add('single', 'SSL VPN',
    'Which VPN type is commonly accessed through a web browser without a dedicated client?',
    ['IPsec VPN', 'SSL VPN', 'GRE VPN', 'L2TP VPN'], 'B',
    'SSL VPN can be accessed via a web browser, making it convenient for remote users.')

add('single', 'SSL VPN',
    'Which SSL VPN mode provides access to specific web applications through a browser?',
    ['Web proxy mode', 'Network extension mode', 'File sharing mode', 'Full tunnel mode'], 'A',
    'Web proxy mode allows browser-based access to internal web applications.')

add('multi', 'VPN Overview',
    'Which are common VPN types? (Choose all that apply)',
    ['Site-to-site VPN', 'Remote-access VPN', 'Intranet VPN', 'Extranet VPN'], 'A,B,C,D',
    'VPNs can be site-to-site, remote-access, intranet, or extranet based on deployment.')

add('multi', 'IPsec VPN',
    'Which are IPsec protocols? (Choose all that apply)',
    ['AH', 'ESP', 'IKE', 'GRE'], 'A,B,C',
    'AH, ESP, and IKE are part of IPsec; GRE is a separate tunneling protocol.')

add('multi', 'SSL VPN',
    'Which are common SSL VPN access modes? (Choose all that apply)',
    ['Web proxy', 'File sharing', 'Network extension', 'Port forwarding'], 'A,B,C,D',
    'SSL VPN can offer web proxy, file sharing, network extension, and port forwarding.')

add('tf', 'GRE VPN',
    'GRE provides strong encryption by default.',
    ['True', 'False'], 'False',
    'GRE only encapsulates traffic; encryption must be added separately, often with IPsec.')

add('tf', 'IPsec VPN',
    'ESP provides both encryption and authentication.',
    ['True', 'False'], 'True',
    'ESP can encrypt payloads and authenticate packets.')

add('tf', 'IPsec VPN',
    'AH provides payload encryption.',
    ['True', 'False'], 'False',
    'AH provides authentication and integrity but does not encrypt the payload.')

add('tf', 'L2TP VPN',
    'L2TP alone does not provide encryption.',
    ['True', 'False'], 'True',
    'L2TP provides tunneling but relies on IPsec or other mechanisms for encryption.')

add('tf', 'SSL VPN',
    'SSL VPN typically uses TCP port 443.',
    ['True', 'False'], 'True',
    'SSL/TLS VPNs commonly use HTTPS/TCP 443, which is usually allowed through firewalls.')


# =============================================================================
# BULK QUESTION POOLS
# =============================================================================

# Helper to add many questions from compact tuple lists
# single/multi tuples: (topic, question, [options], answer, explanation)
# tf tuples: (topic, question, answer, explanation)

bulk_single = [
    # Chapter 1 extra
    ('Network Security Concepts', 'Which term describes the practice of protecting networks and data from unauthorized access?', ['Cybersecurity', 'Marketing', 'Accounting', 'Logistics'], 'A', 'Cybersecurity protects networks, devices, and data from unauthorized access or attack.'),
    ('Network Security Concepts', 'Which of the following best defines a vulnerability?', ['A weakness that can be exploited', 'A security patch', 'A firewall rule', 'A network diagram'], 'A', 'A vulnerability is a weakness in a system that a threat actor can exploit.'),
    ('Network Security Concepts', 'What is an exploit?', ['A software patch', 'A method to take advantage of a vulnerability', 'A type of firewall', 'A routing protocol'], 'B', 'An exploit is a technique or code that leverages a vulnerability.'),
    ('Network Security Concepts', 'Which term describes a potential danger to an asset?', ['Risk', 'Threat', 'Vulnerability', 'Control'], 'B', 'A threat is any potential danger that could exploit a vulnerability.'),
    ('Network Security Concepts', 'Which term describes the likelihood and impact of a threat exploiting a vulnerability?', ['Threat', 'Risk', 'Asset', 'Control'], 'B', 'Risk measures the probability and impact of a security incident.'),
    ('Network Security Concepts', 'Future security architecture is moving toward:', ['Single perimeter defense', 'Zero-trust and dynamic trust models', 'Open anonymous access', 'No logging'], 'B', 'Zero trust assumes no implicit trust and verifies every access request dynamically.'),
    ('Network Security Concepts', 'Which technology is increasingly used to detect unknown threats?', ['Signature-only antivirus', 'Artificial intelligence and machine learning', 'Hub-based networks', 'Plaintext protocols'], 'B', 'AI/ML helps analyze behavior and detect anomalies and unknown threats.'),
    ('Network Security Concepts', 'What does confidentiality ensure?', ['Only speed', 'Information is accessible only to authorized users', 'Unlimited access', 'Data duplication'], 'B', 'Confidentiality ensures that information is disclosed only to authorized individuals.'),
    ('Network Security Concepts', 'What does integrity ensure?', ['Fast transmission', 'Information is not tampered with during transmission/storage', 'Free access', 'Unencrypted storage'], 'B', 'Integrity ensures data is not altered or destroyed in an unauthorized manner.'),
    ('Network Security Concepts', 'What does availability ensure?', ['Authorized users can access information when needed', 'All users can access', 'Systems are offline', 'Data is hidden'], 'A', 'Availability guarantees reliable and timely access to information for authorized users.'),
    ('Network Security Concepts', 'What does controllability mean in information security?', ['No monitoring', 'Ability to monitor and control information/systems', 'Unlimited downloads', 'No access controls'], 'B', 'Controllability enables organizations to monitor, manage, and protect information and systems.'),
    ('Network Security Concepts', 'What does non-repudiation prevent?', ['Fast data transfer', 'Senders or receivers from denying their actions', 'Encryption', 'Backups'], 'B', 'Non-repudiation provides proof of origin and delivery so parties cannot deny participation.'),
    ('Network Security Standards', 'Which ISO standard family addresses information security management?', ['ISO 9000', 'ISO 27000', 'ISO 14000', 'ISO 20000'], 'B', 'The ISO/IEC 27000 family covers information security management systems and controls.'),
    ('Network Security Standards', 'Which Chinese regulation is the basis for Classified Protection?', ['Cybersecurity Law', 'GDPR', 'HIPAA', 'PCI DSS'], 'A', 'China Cybersecurity Law underpins the Classified Protection compliance framework.'),
    ('Network Security Standards', 'ISO 27001 uses which methodology for risk management?', ['Ignore risks', 'Plan-Do-Check-Act (PDCA)', 'Random patching', 'No reviews'], 'B', 'ISO 27001 follows the PDCA cycle for continuous improvement of the ISMS.'),
    ('Network Security Standards', 'Which document in ISO 27000 family provides implementation guidance for controls?', ['ISO 27001', 'ISO 27002', 'ISO 27003', 'ISO 27005'], 'B', 'ISO 27002 lists security controls and implementation guidance.'),
    ('Network Security Standards', 'Which is a key principle of Classified Protection 2.0?', ['Security synchronization with construction', 'Security as an afterthought', 'No auditing', 'Anonymous access'], 'A', 'Classified Protection requires security to be planned, constructed, and used simultaneously with information systems.'),
    ('Network Security Standards', 'In Classified Protection 2.0, the security protection level is preliminarily determined by the network operator, but when the level reaches which level or above, expert review and approval are required?', ['Level 1', 'Level 2', 'Level 3', 'Level 4'], 'B', 'For protection Level 2 and above, the preliminary determination must be reviewed and approved; Level 1 can be determined by the operator.'),
    # Chapter 2 extra
    ('Network Fundamentals', 'What is the default subnet mask for a Class C IPv4 address?', ['255.0.0.0', '255.255.0.0', '255.255.255.0', '255.255.255.255'], 'C', 'Class C networks use a default /24 subnet mask: 255.255.255.0.'),
    ('Network Fundamentals', 'Which protocol is used to automatically assign IPv6 addresses using MAC addresses?', ['DHCPv6', 'SLAAC', 'ARP', 'DNS'], 'B', 'SLAAC can generate IPv6 addresses from MAC addresses.'),
    ('Network Fundamentals', 'Which layer-2 protocol prevents loops in redundant Ethernet topologies?', ['VTP', 'STP', 'RSTP', 'Both STP and RSTP'], 'D', 'Spanning Tree Protocol and Rapid STP prevent Layer 2 loops.'),
    ('Network Fundamentals', 'What does VLAN stand for?', ['Virtual Local Area Network', 'Virtual Large Area Network', 'Verified Local Access Node', 'Virtual Link Aggregation Network'], 'A', 'VLANs logically segment a switch into separate broadcast domains.'),
    ('Network Fundamentals', 'Which device interconnects VLANs at Layer 3?', ['Layer 2 switch', 'Router or Layer 3 switch', 'Hub', 'Bridge'], 'B', 'Routers or Layer 3 switches perform inter-VLAN routing.'),
    ('Network Fundamentals', 'Which OSI layer is responsible for reliable data transfer between hosts?', ['Network', 'Transport', 'Data link', 'Physical'], 'B', 'The transport layer manages end-to-end reliability, flow control, and error recovery.'),
    ('Network Fundamentals', 'In the TCP/IP model, which layer corresponds to the OSI network layer?', ['Internet layer', 'Network interface layer', 'Transport layer', 'Application layer'], 'A', 'The TCP/IP internet layer maps to the OSI network layer and handles IP routing.'),
    ('Network Fundamentals', 'Which layer handles encryption and data format conversion?', ['Application', 'Presentation', 'Session', 'Transport'], 'B', 'The presentation layer handles syntax, encryption, compression, and character encoding.'),
    ('Network Fundamentals', 'Which layer establishes, manages, and terminates application dialogs?', ['Application', 'Presentation', 'Session', 'Transport'], 'C', 'The session layer controls dialog establishment, maintenance, and termination.'),
    ('Network Fundamentals', 'Which protocol is used to send email between servers?', ['HTTP', 'SMTP', 'POP3', 'IMAP'], 'B', 'SMTP is used to send and relay email.'),
    ('Network Fundamentals', 'Which protocol is used by clients to retrieve email from a server while keeping messages on the server?', ['POP3', 'IMAP', 'SMTP', 'SNMP'], 'B', 'IMAP allows clients to access and manage email while messages remain on the server.'),
    ('Network Fundamentals', 'Which protocol dynamically assigns IP addresses to hosts?', ['DNS', 'DHCP', 'ARP', 'FTP'], 'B', 'DHCP dynamically assigns IP addresses and network configuration parameters.'),
    ('Network Fundamentals', 'Which protocol maps IP addresses to MAC addresses on a local network?', ['DNS', 'ARP', 'DHCP', 'ICMP'], 'B', 'ARP resolves IP addresses to MAC addresses.'),
    ('Network Fundamentals', 'Which protocol is used for network management and monitoring?', ['SNMP', 'SMTP', 'FTP', 'Telnet'], 'A', 'SNMP manages and monitors network devices.'),
    ('Network Fundamentals', 'What does ICMP primarily provide?', ['File transfer', 'Error reporting and diagnostics', 'Email delivery', 'Web browsing'], 'B', 'ICMP reports errors and provides diagnostic functions such as ping and traceroute.'),
    ('Network Fundamentals', 'Which port does HTTP use by default?', ['20', '21', '80', '443'], 'C', 'HTTP uses TCP port 80 by default.'),
    ('Network Fundamentals', 'Which port does HTTPS use by default?', ['80', '443', '22', '25'], 'B', 'HTTPS uses TCP port 443 by default, providing encrypted web traffic.'),
    ('Network Fundamentals', 'Which port does SSH use by default?', ['21', '22', '23', '25'], 'B', 'SSH uses TCP port 22 for secure remote access.'),
    ('Network Fundamentals', 'Telnet uses which port and is considered insecure because it transmits data in plaintext?', ['21', '22', '23', '25'], 'C', 'Telnet uses TCP port 23 and sends data, including credentials, in plaintext.'),
    ('Network Fundamentals', 'Which address is a Layer 2 address?', ['IP address', 'MAC address', 'Port number', 'Domain name'], 'B', 'A MAC address is a hardware address used at the data link layer.'),
    ('Network Fundamentals', 'A router forwards packets based on:', ['MAC address', 'IP address', 'Port number', 'VLAN ID'], 'B', 'Routers use IP addresses to make forwarding decisions.'),
    ('Network Fundamentals', 'What is a subnet mask used for?', ['MAC address', 'IP address class', 'Network and host portions of an IP address', 'DNS server'], 'C', 'A subnet mask divides an IP address into network and host portions.'),
    # Chapter 3 extra
    ('Enterprise Security Threats', 'Which attack sends an overwhelming amount of traffic from many sources?', ['DoS', 'DDoS', 'Phishing', 'Spoofing'], 'B', 'DDoS uses multiple distributed sources to flood a target.'),
    ('Enterprise Security Threats', 'Which attack falsifies the source address of packets?', ['Phishing', 'Spoofing', 'Sniffing', 'Spamming'], 'B', 'Spoofing impersonates a trusted source by falsifying addresses or identities.'),
    ('Enterprise Security Threats', 'Which type of malware replicates itself across networks without user action?', ['Virus', 'Worm', 'Trojan', 'Spyware'], 'B', 'Worms can self-replicate and spread across networks, often without user interaction.'),
    ('Enterprise Security Threats', 'Which malware disguises itself as legitimate software?', ['Virus', 'Worm', 'Trojan', 'Adware'], 'C', 'A Trojan horse masquerades as legitimate software to trick users into executing it.'),
    ('Enterprise Security Threats', 'Ransomware primarily does what?', ['Steals credentials', 'Encrypts data and demands payment', 'Deletes logs', 'Monitors traffic'], 'B', 'Ransomware encrypts files and demands a ransom for decryption.'),
    ('Enterprise Security Threats', 'Which attack intercepts communications between two parties without their knowledge?', ['Man-in-the-middle', 'DoS', 'Phishing', 'Tailgating'], 'A', 'A man-in-the-middle attack intercepts and possibly alters communication between parties.'),
    ('Enterprise Security Threats', 'Which protocol can help prevent man-in-the-middle attacks by verifying server identity?', ['HTTP', 'HTTPS', 'FTP', 'Telnet'], 'B', 'HTTPS uses TLS/SSL to encrypt traffic and authenticate the server.'),
    ('Enterprise Security Threats', 'Which wireless security protocol is more secure than WEP?', ['WPA2/WPA3', 'WEP', 'WPA (TKIP only)', 'Open network'], 'A', 'WPA2 and WPA3 provide stronger encryption and authentication than WEP.'),
    ('Enterprise Security Threats', 'What is a DMZ typically used for?', ['Hosting internal databases only', 'Hosting public-facing servers', 'User workstations', 'Printer sharing'], 'B', 'A DMZ hosts public-facing services between the Internet and internal network.'),
    ('Enterprise Security Threats', 'Which security zone usually has the highest priority in Huawei firewalls?', ['Untrust', 'Trust', 'DMZ', 'Local'], 'D', 'The Local zone (firewall itself) has priority 100, the highest default priority.'),
    ('Enterprise Security Threats', 'Which practice limits the damage from compromised accounts?', ['Least privilege', 'Sharing admin passwords', 'Disabling logs', 'Open shares'], 'A', 'Least privilege gives users only the access they need, limiting blast radius.'),
    ('Enterprise Security Threats', 'What is the purpose of host-based intrusion prevention?', ['Route packets', 'Detect and block malicious host activity', 'Assign IP addresses', 'Synchronize time'], 'B', 'Host-based IPS monitors and blocks suspicious activity on an endpoint.'),
    ('Enterprise Security Threats', 'Which technology collects and analyzes security logs centrally?', ['SIEM', 'SNMP', 'DHCP', 'ARP'], 'A', 'SIEM centralizes log collection and analysis.'),
    ('Enterprise Security Threats', 'What is a key benefit of centralized security management?', ['Reduced visibility', 'Unified policy and monitoring', 'More complex passwords', 'Faster malware spread'], 'B', 'Centralized management provides unified visibility, policy control, and monitoring.'),
    ('Enterprise Security Threats', 'What is an insider threat?', ['An attack from outside the network', 'A security risk originating from within the organization', 'A hardware vendor', 'A natural disaster'], 'B', 'Insider threats come from employees, contractors, or partners with internal access.'),
    ('Enterprise Security Threats', 'Which attack sends oversized ICMP packets to crash a target?', ['Ping of death', 'Ping sweep', 'ARP spoofing', 'DNS hijacking'], 'A', 'Ping of death sends ICMP packets larger than the maximum allowed size.'),
    ('Enterprise Security Threats', 'Which attack uses broadcast pings to amplify traffic?', ['Smurf attack', 'SYN flood', 'Fraggle', 'Session hijacking'], 'A', 'Smurf attacks send ICMP echo requests to broadcast addresses with a spoofed source.'),
    ('Enterprise Security Threats', 'Which attack intercepts ARP messages to redirect traffic?', ['ARP spoofing', 'DNS spoofing', 'IP spoofing', 'MAC flooding'], 'A', 'ARP spoofing sends forged ARP replies to associate an attacker MAC with another IP.'),
    # Chapter 4 extra
    ('Firewall Basics', 'Which firewall feature inspects application-layer data to detect attacks?', ['Packet filtering', 'Application inspection', 'Hub forwarding', 'NAT'], 'B', 'Application inspection examines payload content for malicious patterns.'),
    ('Firewall Basics', 'Which Huawei firewall command mode is used for system-level configuration?', ['User view', 'System view', 'Interface view', 'Policy view'], 'B', 'System view allows global-level configuration on Huawei devices.'),
    ('Firewall Basics', 'Which view is entered after the system-view command?', ['User view', 'System view', 'Interface view', 'None'], 'B', 'The system-view command enters system view from user view.'),
    ('Firewall Basics', 'What is the purpose of a security profile in NGFW?', ['Physical installation', 'Applying advanced security features such as IPS/AV/URL filtering', 'Layer 1 forwarding', 'DHCP relay'], 'B', 'Security profiles group advanced inspection features applied to policies.'),
    ('Firewall Basics', 'Which firewall generation combines traditional firewall functions with application awareness and intrusion prevention?', ['Packet-filtering firewall', 'Next-generation firewall', 'Stateful firewall', 'Proxy firewall'], 'B', 'Next-generation firewalls integrate application awareness, IPS, antivirus, and user identity.'),
    ('Firewall Basics', 'What is the purpose of a default security policy deny action?', ['Improve performance', 'Ensure least-privilege access', 'Enable logging', 'Allow management'], 'B', 'Default deny enforces least privilege by blocking unspecified traffic.'),
    ('Firewall Basics', 'Which zone would typically contain public web servers?', ['Trust', 'Untrust', 'DMZ', 'Local'], 'C', 'Public-facing servers are placed in the DMZ for isolation.'),
    ('Firewall Basics', 'What does policy hit counting help with?', ['Routing optimization', 'Verifying policy usage and troubleshooting', 'MAC learning', 'DHCP assignment'], 'B', 'Hit counts show which policies are triggered, aiding auditing and troubleshooting.'),
    ('Firewall Basics', 'Which of the following is NOT a firewall deployment mode?', ['Routing mode', 'Transparent mode', 'Hybrid mode', 'Broadcast mode'], 'D', 'Firewalls deploy in routing, transparent (bridge), or hybrid modes; broadcast mode is not standard.'),
    ('Firewall Basics', 'What happens when traffic moves from a higher-priority zone to a lower-priority zone?', ['Inbound traffic', 'Outbound traffic', 'No traffic allowed', 'Always dropped'], 'B', 'Traffic from a higher-priority zone to a lower-priority zone is considered outbound.'),
    ('Firewall Basics', 'What is the priority range for custom security zones on Huawei firewalls?', ['0-50', '1-100', '1-99 excluding defaults', '0-100'], 'C', 'Custom zone priorities range from 1 to 99, avoiding reserved default values.'),
    ('Firewall Basics', 'Which action in a security policy can log permitted or denied traffic?', ['Permit', 'Deny', 'Both permit and deny', 'Neither'], 'C', 'Security policies can enable logging for both permit and deny actions.'),
    ('Firewall Basics', 'Which security policy action is typically applied to suspicious traffic for further inspection?', ['Permit', 'Deny', 'Block', 'Redirect'], 'B', 'Suspicious traffic is commonly denied or blocked by policy.'),
    ('Firewall Basics', 'When a return packet arrives, what does a stateful firewall check first?', ['Routing table', 'Session table', 'MAC table', 'ARP table'], 'B', 'A stateful firewall first checks the session table to find a matching connection.'),
    ('Firewall Basics', 'What happens if a return packet does not match any session table entry?', ['Forwarded normally', 'Dropped or inspected against policies', 'Always permitted', 'Sent to DMZ'], 'B', 'Without a matching session, the firewall treats the packet as a new connection and applies policies.'),
    ('Firewall Basics', 'Which protocol commonly requires ASPF support due to dynamic port negotiation?', ['HTTP', 'FTP', 'DNS', 'NTP'], 'B', 'FTP negotiates dynamic data ports in its control channel, requiring ASPF.'),
    ('Firewall Basics', 'ASPF primarily inspects traffic at which layer?', ['Network layer only', 'Application layer', 'Physical layer', 'Data link layer'], 'B', 'ASPF performs application-layer inspection to identify negotiated connections.'),
    # Chapter 5 extra
    ('NAT', 'Which NAT type is also called many-to-one NAT?', ['Static NAT', 'Dynamic NAT', 'NAPT', 'NAT Server'], 'C', 'NAPT maps multiple private addresses to one public IP using port numbers.'),
    ('NAT', 'Which NAT type preserves a one-to-one mapping between public and private addresses?', ['Static NAT', 'NAPT', 'Easy-IP', 'Dynamic PAT'], 'A', 'Static NAT maps one public IP to one private IP consistently.'),
    ('NAT', 'Which NAT type uses the outbound interface IP as the public address?', ['NAPT', 'NAT No-PAT', 'Easy-IP', 'Destination NAT'], 'C', 'Easy-IP uses the firewall egress interface IP for translation.'),
    ('NAT', 'Which source NAT mode maps one private address to one public address without port translation?', ['NAPT', 'NAT No-PAT', 'Easy-IP', 'NAT Server'], 'B', 'NAT No-PAT performs one-to-one address translation without changing port numbers.'),
    ('NAT', 'When many internal hosts access the Internet using one public IP, which NAT is used?', ['NAT No-PAT', 'NAPT', 'NAT Server', 'Static NAT'], 'B', 'NAPT allows many-to-one address translation using port numbers.'),
    ('NAT', 'Destination NAT is also known as:', ['Static NAT', 'Port forwarding / virtual IP', 'PAT', 'Proxy ARP'], 'B', 'Destination NAT maps external destinations to internal hosts, commonly called port forwarding or virtual IP.'),
    ('NAT', 'Which NAT type maps a public IP/port to a private server IP/port?', ['Source NAT', 'NAT Server', 'NAPT', 'Bidirectional NAT'], 'B', 'NAT Server publishes internal services to external networks.'),
    ('NAT', 'Bidirectional NAT is useful when:', ['Only source address translation is needed', 'Both source and destination must be rewritten', 'No NAT is needed', 'Only DNS traffic is involved'], 'B', 'It translates both source and destination addresses in a single flow.'),
    ('NAT', 'Which problem can occur if NAT ALG is disabled for FTP?', ['FTP control channel fails', 'FTP data channel may fail because dynamic ports are not opened', 'FTP becomes encrypted', 'FTP speeds up'], 'B', 'Without ALG, the firewall cannot open the negotiated FTP data channel.'),
    ('NAT', 'Which address type is preserved by NAT No-PAT?', ['Source port', 'Destination port', 'Both source and destination ports', 'No ports'], 'C', 'NAT No-PAT translates only IP addresses, preserving port numbers.'),
    ('NAT', 'What is a major benefit of NAPT?', ['One-to-one address mapping', 'Conserves public IP addresses', 'Full protocol transparency', 'No ALG needed'], 'B', 'NAPT conserves public IPs by sharing one address across many internal hosts.'),
    ('NAT', 'A NAT Server entry is typically:', ['Bidirectional and persistent', 'Temporary and random', 'Encrypted', 'Only for outbound traffic'], 'A', 'NAT Server entries are configured statically and persist for inbound access.'),
    ('NAT', 'NAT ALG is often enabled together with:', ['ASPF', 'Routing', 'DHCP', 'DNS'], 'A', 'ALG and ASPF work together to inspect dynamic application channels.'),
    ('NAT', 'Which RFC defines private IPv4 address space?', ['RFC 1918', 'RFC 2328', 'RFC 793', 'RFC 959'], 'A', 'RFC 1918 defines the private IPv4 address ranges.'),
    ('NAT', 'Hairpin NAT allows internal users to access an internal server using:', ['The server private IP only', 'The server public NAT address', 'A VPN tunnel', 'Broadcast address'], 'B', 'Hairpin NAT lets internal hosts reach an internal server via its public NAT address.'),
]

for topic, q, opts, ans, exp in bulk_single:
    add('single', topic, q, opts, ans, exp)


bulk_multi = [
    ('Network Security Concepts', 'Which are stages in the development history of network security? (Choose all that apply)', ['Communication security period', 'Information security period', 'Information assurance period', 'Cyberspace security period'], 'A,B,C,D', 'Network security has evolved through communication security, information security, information assurance, and cyberspace security periods.'),
    ('Network Security Standards', 'Which are benefits of implementing ISO 27001? (Choose all that apply)', ['Systematic risk management', 'Improved stakeholder confidence', 'Legal/regulatory compliance', 'Guaranteed zero attacks'], 'A,B,C', 'ISO 27001 helps manage risk, build confidence, and comply with regulations, but cannot guarantee zero attacks.'),
    ('Network Security Standards', 'Which are typical Classified Protection 2.0 security extension requirements? (Choose all that apply)', ['Cloud computing', 'Mobile Internet', 'Internet of Things', 'Industrial control systems'], 'A,B,C,D', 'Classified Protection 2.0 extends coverage to cloud, mobile Internet, IoT, and industrial control scenarios.'),
    ('Network Fundamentals', 'Which layers are included in the TCP/IP equivalent model? (Choose all that apply)', ['Application', 'Transport', 'Network', 'Data link', 'Physical'], 'A,B,C,D,E', 'The TCP/IP equivalent model includes application, transport, network, data link, and physical layers.'),
    ('Network Fundamentals', 'Which are connectionless protocols? (Choose all that apply)', ['UDP', 'IP', 'ICMP', 'TCP'], 'A,B,C', 'UDP, IP, and ICMP are connectionless; TCP is connection-oriented.'),
    ('Network Fundamentals', 'Which fields are in a TCP header? (Choose all that apply)', ['Source port', 'Destination port', 'Sequence number', 'Acknowledgment number'], 'A,B,C,D', 'TCP headers include source/destination ports, sequence and acknowledgment numbers, flags, window size, etc.'),
    ('Network Fundamentals', 'Which devices operate primarily at Layer 1? (Choose all that apply)', ['Hub', 'Repeater', 'Switch', 'Router'], 'A,B', 'Hubs and repeaters operate at the physical layer.'),
    ('Network Fundamentals', 'Which protocols use TCP? (Choose all that apply)', ['HTTP', 'FTP', 'SMTP', 'DNS (sometimes)'], 'A,B,C,D', 'HTTP, FTP, and SMTP use TCP; DNS primarily uses UDP but can use TCP for zone transfers and large responses.'),
    ('Network Fundamentals', 'Which protocols use UDP? (Choose all that apply)', ['DNS', 'TFTP', 'SNMP', 'DHCP'], 'A,B,C,D', 'DNS, TFTP, SNMP, and DHCP commonly use UDP.'),
    ('Network Fundamentals', 'Which are valid IPv4 private address ranges? (Choose all that apply)', ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '224.0.0.0/4'], 'A,B,C', 'RFC 1918 private ranges are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.'),
    ('Enterprise Security Threats', 'Which are examples of malware? (Choose all that apply)', ['Virus', 'Worm', 'Trojan', 'Ransomware', 'Spyware'], 'A,B,C,D,E', 'All listed items are types of malware.'),
    ('Enterprise Security Threats', 'Which are social engineering attacks? (Choose all that apply)', ['Phishing', 'Pretexting', 'Baiting', 'Tailgating'], 'A,B,C,D', 'Social engineering manipulates people through phishing, pretexting, baiting, tailgating, etc.'),
    ('Enterprise Security Threats', 'Which protect communication confidentiality? (Choose all that apply)', ['Encryption', 'VPN', 'TLS/SSL', 'MAC filtering'], 'A,B,C', 'Encryption, VPNs, and TLS/SSL protect confidentiality; MAC filtering controls device access.'),
    ('Enterprise Security Threats', 'Which are typical security zones? (Choose all that apply)', ['Trust', 'Untrust', 'DMZ', 'Local'], 'A,B,C,D', 'Huawei firewalls define Trust, Untrust, DMZ, and Local security zones by default.'),
    ('Enterprise Security Threats', 'Which are endpoint security controls? (Choose all that apply)', ['Antivirus', 'Host firewall', 'Application whitelisting', 'Full-disk encryption'], 'A,B,C,D', 'Endpoint security includes antivirus, host firewalls, whitelisting, and encryption.'),
    ('Firewall Basics', 'Which are Huawei firewall default security zones? (Choose all that apply)', ['Trust', 'Untrust', 'DMZ', 'Local'], 'A,B,C,D', 'Huawei firewalls provide Trust, Untrust, DMZ, and Local zones by default.'),
    ('Firewall Basics', 'Which actions can a security policy perform? (Choose all that apply)', ['Permit', 'Deny', 'Log', 'Redirect'], 'A,B,C', 'Policies can permit, deny, and log traffic; redirect may be available in specific features.'),
    ('Firewall Basics', 'Which are common firewall deployment modes? (Choose all that apply)', ['Routing mode', 'Transparent mode', 'Hybrid mode', 'Bridge mode'], 'A,B,C', 'Firewalls commonly deploy in routing, transparent (bridge), and hybrid modes.'),
    ('Firewall Basics', 'Which conditions can be matched in a security policy? (Choose all that apply)', ['Source zone', 'Destination zone', 'Source IP', 'Destination port', 'User'], 'A,B,C,D,E', 'Policies can match zones, IPs, ports, users, applications, services, and time.'),
    ('NAT', 'Which are private IPv4 address ranges? (Choose all that apply)', ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '127.0.0.0/8'], 'A,B,C', 'RFC 1918 private ranges are 10/8, 172.16/12, and 192.168/16.'),
    ('NAT', 'Which are valid uses of NAT Server? (Choose all that apply)', ['Publishing a web server', 'Publishing an email server', 'Remote access to an internal host', 'Hiding internal topology'], 'A,B,C,D', 'NAT Server can publish services, enable remote access, and obscure internal addressing.'),
]

for topic, q, opts, ans, exp in bulk_multi:
    add('multi', topic, q, opts, ans, exp)


bulk_tf = [
    ('Network Security Concepts', 'Non-repudiation ensures that senders or receivers cannot deny their actions.', 'True', 'Non-repudiation provides evidence to prevent denial of participation.'),
    ('Network Security Concepts', 'Availability means anyone can access the system at any time.', 'False', 'Availability means authorized users can access information when required, not unlimited access.'),
    ('Network Security Standards', 'ISO 27001 provides a list of security controls but is not certifiable.', 'False', 'ISO 27001 is the certifiable standard specifying ISMS requirements; ISO 27002 provides controls.'),
    ('Network Security Standards', 'Classified Protection 2.0 requires security and informatization to be planned together.', 'True', 'The framework emphasizes synchronized planning, construction, and use of security.'),
    ('Network Security Concepts', 'Zero trust means everything inside the network is trusted by default.', 'False', 'Zero trust never assumes trust based on network location and verifies every request.'),
    ('Network Security Concepts', 'Integrity ensures that data is not tampered with during transmission.', 'True', 'Integrity protects against unauthorized modification or destruction of data.'),
    ('Network Security Standards', 'Level assessment is part of the Classified Protection lifecycle.', 'True', 'After construction, a level assessment verifies that protection measures meet the required level.'),
    ('Network Fundamentals', 'The OSI model was developed before the TCP/IP model.', 'False', 'TCP/IP was developed earlier and became the de facto standard; OSI was later as a reference model.'),
    ('Network Fundamentals', 'DNS always uses TCP port 53.', 'False', 'DNS primarily uses UDP port 53; TCP port 53 is used for zone transfers and large responses.'),
    ('Network Fundamentals', 'A switch forwards packets based on IP addresses.', 'False', 'A switch forwards frames based on MAC addresses; routers forward packets based on IP addresses.'),
    ('Network Fundamentals', 'IPv4 addresses are 32 bits long.', 'True', 'IPv4 addresses are 32-bit binary numbers, usually written in dotted-decimal notation.'),
    ('Network Fundamentals', 'ICMP is a transport-layer protocol.', 'False', 'ICMP is a network-layer protocol used for diagnostics and error reporting.'),
    ('Enterprise Security Threats', 'A worm requires a host program to spread.', 'False', 'Worms are standalone malware that can self-replicate; viruses require host programs.'),
    ('Enterprise Security Threats', 'Phishing attacks target human psychology rather than software vulnerabilities.', 'True', 'Phishing uses deception and social engineering to trick users.'),
    ('Enterprise Security Threats', 'Using HTTP instead of HTTPS improves confidentiality.', 'False', 'HTTP sends data in plaintext; HTTPS encrypts data to protect confidentiality.'),
    ('Enterprise Security Threats', 'The DMZ zone is typically more trusted than the Untrust zone but less trusted than the Trust zone.', 'True', 'DMZ has an intermediate trust level for public-facing servers.'),
    ('Enterprise Security Threats', 'Patch management helps eliminate known vulnerabilities on hosts.', 'True', 'Applying patches closes security holes that attackers could exploit.'),
    ('Enterprise Security Threats', 'All security threats originate from external attackers.', 'False', 'Threats can be external or internal, accidental or malicious.'),
    ('Firewall Basics', 'Security policies on Huawei firewalls are matched from bottom to top by default.', 'False', 'Policies are matched from top to bottom based on configured order/priority.'),
    ('Firewall Basics', 'A packet-filtering firewall tracks the state of every connection.', 'False', 'Only stateful firewalls maintain connection state; packet filters inspect packets individually.'),
    ('Firewall Basics', 'ASPF can generate temporary server-map entries for dynamic protocols.', 'True', 'ASPF creates server-map entries to permit negotiated secondary connections.'),
    ('Firewall Basics', 'Next-generation firewalls can identify applications regardless of port.', 'True', 'NGFWs use application-layer inspection to identify applications beyond simple port numbers.'),
    ('Firewall Basics', 'Traffic between interfaces in the same security zone is always allowed.', 'False', 'Even intra-zone traffic can be controlled by policies, though default behavior may vary by configuration.'),
    ('Firewall Basics', 'A deny action in a security policy can generate logs.', 'True', 'Both permit and deny actions can be configured to log traffic.'),
    ('NAT', 'NAT can hide internal network topology from external observers.', 'True', 'NAT translates private addresses, making internal topology invisible from outside.'),
    ('NAT', 'Easy-IP uses a fixed public IP address pool.', 'False', 'Easy-IP uses the firewall egress interface IP address dynamically.'),
    ('NAT', 'NAT ALG is required for HTTP because HTTP embeds IP addresses in payloads.', 'False', 'HTTP generally does not embed IP addresses in payloads, so ALG is not required.'),
    ('NAT', 'NAPT conserves public IPv4 addresses by using port multiplexing.', 'True', 'NAPT maps many private addresses to one public IP using unique port numbers.'),
    ('NAT', 'FTP data channel failure can be caused by disabled NAT ALG.', 'True', 'Without ALG, the firewall cannot identify and permit the negotiated FTP data channel.'),
]

for topic, q, ans, exp in bulk_tf:
    add('tf', topic, q, ['True', 'False'], ans, exp)
