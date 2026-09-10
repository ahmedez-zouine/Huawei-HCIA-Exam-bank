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
