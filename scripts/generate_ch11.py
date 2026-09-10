# scripts/generate_ch11.py
"""
Generates Chapter 11 data: 40 Single Choice, 30 Multiple Choice, 32 True/False.
Chapter 11: Encryption Technology Applications (IPsec VPN, IKEv1/v2, L2TP, GRE, and SSL VPN)
"""
import json

CHAPTER_NAMES = {
    11: "Encryption Technology Applications (IPsec & SSL VPN)"
}

def get_ch11_questions():
    single = []
    multi = []
    tf = []

    # ==========================================
    # CHAPTER 11 SINGLE CHOICE (40 questions)
    # ==========================================
    s_data = [
        ("VPN Core Value", "What is the primary motivation for an enterprise to deploy Virtual Private Network (VPN) technology across the public Internet instead of leasing dedicated physical leased lines?",
         ["VPNs eliminate the need for routing protocols and IP addressing",
          "VPNs provide secure, encrypted virtual communication channels over low-cost public Internet infrastructure, drastically reducing connectivity costs and providing flexible scalability",
          "VPNs guarantee 100 Gbps physical throughput over standard telephone twisted-pair wires",
          "VPNs eliminate the need for enterprise firewalls and host endpoint protection"], "B",
         "Leasing private telecommunication circuits (such as dedicated TDM/SDH or MPLS leased lines) is extremely expensive and rigid. VPN technology creates encrypted, authenticated virtual tunnels over public networks (like the Internet), providing high security at significantly reduced costs with rapid deployment flexibility."),

        ("VPN Classification by Topology", "Which VPN deployment model is specifically designed for mobile employees, teleworkers, and roaming business travelers who need secure remote access into internal enterprise servers?",
         ["Site-to-Site VPN",
          "Client-to-Site (Remote Access) VPN",
          "Layer 2 Carrier Backbone Interconnect",
          "Hub-and-Spoke Leased Ring"], "B",
         "A Client-to-Site VPN (also known as Remote Access VPN or Client-Initiated VPN) enables roaming or telecommuting users to initiate dial-up or encrypted tunnel sessions from laptop/mobile endpoints to an enterprise VPN gateway."),

        ("Site-to-Site VPN Scenario", "Which scenario represents a typical application of a Site-to-Site VPN?",
         ["An executive accessing corporate email from an airport Wi-Fi using a smartphone",
          "Connecting the corporate headquarters network directly to a remote branch office LAN across the Internet",
          "A home user connecting to an online gaming server",
          "A customer browsing a public e-commerce web storefront"], "B",
         "Site-to-Site VPN securely interconnects two fixed, static local area networks (LANs)—such as an enterprise headquarters and a branch office—via their edge VPN gateways across an untrusted WAN or Internet."),

        ("VPN Tunneling Concept", "In VPN terminology, what is 'tunneling technology'?",
         ["A physical excavation method used when installing underground fiber optic cables",
          "A technology that encapsulates packets of one network protocol (passenger protocol) inside the packets of another delivery protocol (encapsulating protocol) to traverse intermediate networks",
          "A protocol that compresses video files to reduce bandwidth usage",
          "A method of bypassing network firewalls without packet inspection"], "B",
         "Tunneling encapsulates the original passenger packets (including original private IP headers and payloads) inside an encapsulating protocol header with outer routable IP headers, enabling private network traffic to transit across public intermediate transit networks."),

        ("GRE Protocol Number", "In the IPv4 packet header, which Protocol field value uniquely identifies Generic Routing Encapsulation (GRE)?",
         ["50", "51", "47", "6"], "C",
         "IP protocol numbers: GRE is protocol 47; ESP is protocol 50; AH is protocol 51; TCP is protocol 6; UDP is protocol 17."),

        ("GRE Primary Limitation", "What is the fundamental security limitation of standard Generic Routing Encapsulation (GRE) tunnels?",
         ["GRE does not support tunneling multicast or dynamic routing protocols like OSPF",
          "GRE provides no native encryption or cryptographic data integrity authentication, transmitting passenger payloads in cleartext",
          "GRE is strictly limited to 10 hops across any IP network",
          "GRE requires an active web browser and SSL client installation"], "B",
         "Standard GRE provides tunneling and supports heterogeneous protocols (including multicast and dynamic routing protocols like OSPF/RIP), but it provides zero cryptographic security: no data encryption and no data integrity verification. Therefore, GRE is frequently combined with IPsec (GRE over IPsec)."),

        ("IPsec Architecture Definition", "What is IPsec (IP Security)?",
         ["A standalone hardware routing switch manufactured by Huawei",
          "An open, standardized framework developed by the IETF operating at the Network Layer (Layer 3) to provide confidentiality, integrity, and origin authentication for IP communications",
          "A proprietary application-layer software program running only on Windows desktops",
          "An asymmetric public key management standard defined by ITU-T"], "B",
         "IPsec is an open suite of protocols defined by the IETF operating at Layer 3 (Network Layer) of the OSI model. It secures IP communications by providing data confidentiality (encryption), data integrity (tamper-proofing), data origin authentication, and anti-replay protection."),

        ("IPsec Protocol Suite Components", "Which two core security encapsulation protocols form the foundation of the IPsec architecture?",
         ["TCP and UDP",
          "AH (Authentication Header) and ESP (Encapsulating Security Payload)",
          "PAP and CHAP",
          "RIP and OSPF"], "B",
         "The IPsec protocol suite is anchored by two primary security protocols: AH (Authentication Header, IP protocol 51) and ESP (Encapsulating Security Payload, IP protocol 50), coordinated by the Internet Key Exchange (IKE) protocol."),

        ("AH Security Capabilities", "Which security services are provided by the Authentication Header (AH) protocol?",
         ["Data encryption only",
          "Data origin authentication, data integrity verification, and anti-replay protection, but NO data confidentiality (no encryption)",
          "Full payload encryption and SSL certificate enrollment",
          "Port forwarding and web proxying"], "B",
         "AH (IP protocol 51) provides strong data origin authentication, message integrity verification (via ICV hash), and anti-replay protection. Crucially, AH does NOT encrypt data; the packet payload remains completely visible in cleartext."),

        ("AH and NAT Incompatibility", "Why is the AH protocol fundamentally incompatible with Network Address Translation (NAT)?",
         ["AH packets exceed the standard Ethernet MTU limit of 1500 bytes",
          "AH calculates its Integrity Check Value (ICV) over the entire IP packet, including the outer IP header; modifying IP addresses/ports in NAT alters the header and causes the receiver's ICV verification to fail",
          "AH uses UDP port 4500 which is blocked by NAT devices",
          "AH only supports IPv6 addressing and cannot operate in IPv4 environments"], "B",
         "AH calculates the ICV covering non-mutable fields of the IP header (such as source and destination IP addresses). When a NAT device rewrites the IP addresses, the outer header changes; the receiving IPsec peer recalculates the ICV, detects a mismatch, and drops the packet as tampered."),

        ("ESP Security Capabilities", "Which security services does the Encapsulating Security Payload (ESP) protocol provide?",
         ["Only packet compression without integrity verification",
          "Data confidentiality (encryption), data origin authentication, data integrity verification, and anti-replay protection",
          "Only Layer 2 VLAN tag encapsulation",
          "Dynamic routing updates across BGP peers without encryption"], "B",
         "ESP (IP protocol 50) provides both data confidentiality (symmetric encryption of the payload) and optional data origin authentication, data integrity verification (ICV), and anti-replay protection. It is the most widely deployed IPsec security protocol."),

        ("IPsec Transport Mode Scope", "In IPsec Transport Mode, what portion of the packet is protected by ESP?",
         ["The entire IP packet including the original IP header",
          "Only the upper-layer payload (e.g., TCP/UDP segment), retaining the original IP header without adding a new outer IP header",
          "Only the Ethernet frame trailer and preamble",
          "The hardware MAC address table of the ingress switch"], "B",
         "In Transport Mode, IPsec protects only the upper-layer transport payload. The original IP header remains intact and serves as the routing header; no new outer IP header is added. Transport mode is primarily used for host-to-host or end-to-end communication."),

        ("IPsec Tunnel Mode Scope", "In IPsec Tunnel Mode, what happens to the original IP packet?",
         ["The original IP header is discarded and replaced permanently by a MAC address",
          "The entire original IP packet (including original private IP header and payload) is protected and encapsulated inside a brand-new outer IP header",
          "The packet is stripped down to raw ASCII text without headers",
          "The packet is converted into an MPLS label stack"], "B",
         "In Tunnel Mode, the entire original IP packet (original IP header + payload) is encapsulated as the security payload, and a brand-new outer IP header is prepended. The outer header routes the packet between the two VPN gateway endpoints, hiding private internal IP topologies."),

        ("Transport vs Tunnel Mode Application", "Which statement correctly describes the primary deployment application of IPsec Tunnel Mode?",
         ["Direct communication between two end-user PCs within the same VLAN",
          "Gateway-to-Gateway (Site-to-Site) VPN communication where private subnets behind edge firewalls communicate across an untrusted public WAN",
          "Managing a local Ethernet switch via console cable",
          "Assigning IP addresses to clients via DHCP"], "B",
         "Tunnel Mode is universally used in Gateway-to-Gateway (Site-to-Site) deployments because the gateways encapsulate internal private enterprise packets inside public outer headers, allowing two isolated private LANs to communicate securely across the Internet."),

        ("IPsec Security Association (SA) Concept", "What is an IPsec Security Association (SA)?",
         ["A physical cable connecting two security gateways",
          "A unidirectional, logical agreement between two communicating endpoints specifying the security parameters (algorithms, keys, SPI, protocol) used to protect traffic",
          "A digital certificate issued by a root CA to an individual user",
          "A user account registered in the local firewall database"], "B",
         "An IPsec SA is a unidirectional logical connection that defines the specific security attributes negotiated between peers, including the encryption algorithm, authentication algorithm, shared keys, lifetime, and Security Parameter Index (SPI)."),

        ("Bidirectional Communication SAs", "How many IPsec Security Associations (SAs) are required to support full-duplex, bidirectional communication between two IPsec peers using ESP?",
         ["1 SA", "2 SAs (one inbound and one outbound)", "4 SAs", "8 SAs"], "B",
         "Because an IPsec SA is strictly unidirectional (simplex), bidirectional communication between two endpoints requires at least two SAs: one outbound SA for encrypting transmitting traffic, and one inbound SA for decrypting received traffic."),

        ("Security Parameter Index (SPI)", "What is the function of the Security Parameter Index (SPI) in the IPsec AH/ESP header?",
         ["It indicates the physical interface speed in megabits per second",
          "It is a 32-bit value that uniquely identifies a specific Security Association (SA) at the receiving endpoint when combined with the destination IP address and security protocol",
          "It defines the maximum transmission unit (MTU) of the VPN link",
          "It counts the number of dropped packets during transmission"], "B",
         "The SPI is a 32-bit field in AH/ESP headers. Together with the destination IP address and the security protocol (AH or ESP), the SPI forms a unique triplet that allows the receiver to locate the exact inbound SA and cryptographic keys from its SADB (Security Association Database)."),

        ("IKE Role in IPsec", "What is the primary role of the Internet Key Exchange (IKE) protocol in an IPsec deployment?",
         ["To route packets dynamically using the Bellman-Ford algorithm",
          "To automate identity authentication, securely exchange key material via Diffie-Hellman, and negotiate Security Associations (SAs) dynamically",
          "To translate private IPv4 addresses into public IPv4 addresses",
          "To act as a web server delivering HTML login pages"], "B",
         "While IPsec SAs can theoretically be configured manually, manual key management is error-prone and unscalable. IKE automates peer identity authentication, uses Diffie-Hellman (DH) to derive symmetric session keys over an untrusted medium, and dynamically negotiates/refreshes SAs."),

        ("IKE Protocol and Port", "Which transport layer protocol and default port does IKE use for negotiation messages?",
         ["TCP port 80", "UDP port 500", "TCP port 443", "UDP port 1701"], "B",
         "IKE uses UDP port 500 for standard Phase 1 and Phase 2 negotiations. (When NAT Traversal is detected, traffic switches to UDP port 4500)."),

        ("IKEv1 Phase 1 Purpose", "What is the objective of IKEv1 Phase 1 negotiation?",
         ["To negotiate the IPsec SAs used directly for encrypting user data traffic",
          "To establish a secure, authenticated communication channel (the IKE SA / ISAKMP SA) to protect subsequent Phase 2 negotiations",
          "To allocate DHCP IP addresses to client endpoints",
          "To download antivirus signature database files"], "B",
         "IKEv1 Phase 1 establishes an authenticated and encrypted management channel known as the IKE SA (or ISAKMP SA). This secure control channel is then used to safely negotiate the actual IPsec SAs in Phase 2."),

        ("IKEv1 Phase 1 Modes", "Which two exchange modes can be configured for IKEv1 Phase 1 negotiation?",
         ["Client Mode and Server Mode",
          "Main Mode and Aggressive Mode",
          "Tunnel Mode and Transport Mode",
          "Active Mode and Passive Mode"], "B",
         "IKEv1 Phase 1 supports two operating modes: Main Mode (Identity Protection Exchange, consisting of 6 messages) and Aggressive Mode (consisting of 3 messages)."),

        ("IKEv1 Main Mode Message Count", "How many messages are exchanged between the initiator and responder in IKEv1 Phase 1 Main Mode?",
         ["2 messages", "3 messages", "4 messages", "6 messages"], "D",
         "IKEv1 Phase 1 Main Mode strictly requires 6 messages: Messages 1 & 2 negotiate security policies (proposals); Messages 3 & 4 perform Diffie-Hellman public value exchange and exchange nonces; Messages 5 & 6 perform encrypted identity authentication."),

        ("IKEv1 Main Mode Identity Protection", "In IKEv1 Phase 1 Main Mode, which messages transmit the peer identity information, and in what state?",
         ["Messages 1 and 2 in cleartext",
          "Messages 3 and 4 in cleartext",
          "Messages 5 and 6, encrypted using the negotiated IKE key material",
          "Messages 7 and 8 in cleartext"], "C",
         "In Main Mode, peer identities (such as IP addresses or digital certificates) are transmitted in Messages 5 and 6, which are fully encrypted by the session keys derived during Messages 3 and 4. This provides identity protection against eavesdropping."),

        ("IKEv1 Aggressive Mode Message Count", "How many messages are exchanged in IKEv1 Phase 1 Aggressive Mode?",
         ["3 messages", "4 messages", "6 messages", "8 messages"], "A",
         "Aggressive Mode trades identity privacy for speed, completing Phase 1 in only 3 messages: Message 1 sends proposals, DH public value, and ID; Message 2 responds with selected proposal, DH value, ID, and authentication; Message 3 confirms authentication."),

        ("IKEv1 Aggressive Mode Trade-off", "What is the primary security drawback of IKEv1 Phase 1 Aggressive Mode compared to Main Mode?",
         ["Aggressive Mode does not support Diffie-Hellman key exchange",
          "Peer identity information is transmitted in cleartext in the first two messages, making it vulnerable to eavesdropping and identity reconnaissance",
          "Aggressive Mode only supports 3DES encryption and cannot run AES",
          "Aggressive Mode cannot establish IPsec tunnels"], "B",
         "In Aggressive Mode, peer identities (IDs) are sent in cleartext in Messages 1 and 2 before encryption keys are established. Attackers intercepting these packets can discover the identity and IP address of the participating peers."),

        ("IKEv1 Aggressive Mode Dynamic IP Scenario", "Why is IKEv1 Aggressive Mode typically used when a branch office connects with a dynamically assigned IP address using pre-shared key (PSK) authentication?",
         ["Because Main Mode cannot run on Huawei USG firewalls",
          "In Main Mode with PSK, the responder must lookup the PSK using the initiator's source IP address before Messages 5/6; with dynamic IP, the responder cannot determine which PSK to use, whereas Aggressive Mode transmits the Name ID in Message 1",
          "Because Aggressive Mode uses TCP instead of UDP",
          "Because Aggressive Mode bypasses firewall security policies automatically"], "B",
         "In Main Mode with PSK, the responder must decrypt Message 5 using the PSK, so it must know the peer identity before decrypting. If the initiator has a dynamic IP, the responder cannot identify which PSK to load. In Aggressive Mode, the Name ID is sent in plaintext in Message 1, allowing the responder to locate the matching pre-shared key."),

        ("IKEv1 Phase 2 Mode Name", "What is the exchange mode used in IKEv1 Phase 2 to negotiate IPsec SAs?",
         ["Main Mode", "Aggressive Mode", "Quick Mode", "Passive Mode"], "C",
         "IKEv1 Phase 2 uses Quick Mode (consisting of 3 encrypted messages) to negotiate the IPsec SAs (security parameters, proxy IDs/ACLs, lifetimes) and generate keys for ESP/AH data protection."),

        ("PFS in Quick Mode", "What does Perfect Forward Secrecy (PFS) achieve when enabled in IKEv1 Phase 2 Quick Mode?",
         ["It prevents the firewall from restarting",
          "It forces an additional independent Diffie-Hellman exchange during Phase 2 so that compromising the Phase 1 master key does not compromise Phase 2 IPsec data keys",
          "It converts ESP packets into cleartext GRE packets",
          "It permanently disables IKE rekeying"], "B",
         "Without PFS, Phase 2 keys are derived directly from the Phase 1 keying material. If an attacker later compromises the Phase 1 master key, all past Phase 2 keys are compromised. PFS forces a new, independent DH key exchange in Quick Mode, guaranteeing that future or past session keys cannot be decrypted if the master key is compromised."),

        ("IKEv2 Message Count for Initial Negotiation", "How many messages does IKEv2 require during its initial exchange to establish both the IKE SA and the initial IPsec Child SA?",
         ["2 messages", "4 messages (two round trips: IKE_SA_INIT and IKE_AUTH)", "6 messages", "9 messages"], "B",
         "IKEv2 drastically streamlines negotiation: it requires only 4 messages (two request-response pairs): IKE_SA_INIT (2 messages to negotiate IKE SA parameters and DH keys) and IKE_AUTH (2 encrypted messages to authenticate identities and establish the first Child SA)."),

        ("IKEv2 CREATE_CHILD_SA Exchange", "In IKEv2, which exchange is used to negotiate additional Child SAs or perform SA rekeying?",
         ["IKE_SA_INIT", "IKE_AUTH", "CREATE_CHILD_SA", "INFORMATIONAL"], "C",
         "In IKEv2, CREATE_CHILD_SA (a 2-message exchange) is used to create additional Child SAs (IPsec SAs) or to rekey existing IKE SAs or Child SAs without tearing down the connection."),

        ("NAT Traversal (NAT-T) Port", "When an IPsec gateway detects the presence of a NAT device along the communication path during IKE negotiation, which UDP port is used to encapsulate ESP traffic in NAT-T?",
         ["UDP port 500", "UDP port 4500", "TCP port 443", "UDP port 1701"], "B",
         "When NAT is detected, IKE and subsequent ESP traffic transition from UDP 500 to UDP port 4500 (NAT Traversal / NAT-T). ESP packets are wrapped inside an outer UDP header, enabling them to traverse standard PAT/NAPT gateways."),

        ("Dead Peer Detection (DPD)", "What is the purpose of the Dead Peer Detection (DPD) mechanism in IPsec VPNs?",
         ["To prevent routing loops in OSPF networks",
          "To periodically check the liveness and responsiveness of the remote IPsec peer, allowing the gateway to quickly reclaim SA resources and re-establish tunnels if the peer fails",
          "To scan remote endpoints for malware infections",
          "To authenticate user passwords via LDAP"], "B",
         "DPD uses keepalive messages (or sends periodic DPD inquiries) to detect whether the remote VPN peer is still active. If the peer crashes or the path breaks, DPD detects the outage, deletes stale SAs, and frees system resources."),

        ("L2TP Port and Protocol", "Which transport protocol and destination port does the Layer 2 Tunneling Protocol (L2TP) use?",
         ["TCP port 22", "UDP port 1701", "UDP port 500", "TCP port 443"], "B",
         "L2TP encapsulates Layer 2 PPP frames into UDP packets using UDP port 1701. To ensure confidentiality, L2TP is almost universally paired with IPsec (L2TP over IPsec)."),

        ("L2TP Architecture Components", "What are the two primary structural endpoint roles in an L2TP VPN deployment?",
         ["Master and Slave",
          "LAC (L2TP Access Concentrator) and LNS (L2TP Network Server)",
          "Root and Leaf",
          "Client and Proxy"], "B",
         "An L2TP network consists of the LAC (L2TP Access Concentrator), which initiates or terminates calls from users, and the LNS (L2TP Network Server), which terminates the tunnel and authenticates users against internal directories."),

        ("SSL VPN Working Layer", "At which layer of the network model does SSL/TLS VPN primarily operate, and what client requirement differentiates it from traditional IPsec VPNs?",
         ["Data Link Layer, requiring specialized hardware transceivers",
          "Transport/Application Layer, allowing users to connect using a standard web browser without installing complex client software for basic services",
          "Physical Layer, requiring fiber optic modems",
          "Network Layer only, requiring kernel-level device drivers on every smartphone"], "B",
         "SSL/TLS VPN operates at the Transport and Application layers (Layers 4-7). Its greatest advantage is clientless or light-client access: users can securely access corporate resources from any standard web browser over HTTPS (port 443) without pre-installing complex VPN software."),

        ("SSL VPN Service - Web Proxy", "Which SSL VPN service allows mobile users to access internal enterprise HTTP/HTTPS web intranet servers directly through their web browser without any local agent installation?",
         ["Port Forwarding", "Web Proxy (Web Browsing)", "File Sharing", "Network Extension"], "B",
         "Web Proxy allows remote users to access internal intranet websites (HTTP/HTTPS) using a standard web browser. The SSL VPN gateway acts as a reverse proxy, translating external HTTPS browser requests into internal web requests."),

        ("SSL VPN Service - File Sharing", "Which file access protocols does the Huawei USG SSL VPN File Sharing service support natively via the browser?",
         ["NFS and SMB/CIFS", "BGP and OSPF", "TFTP and Telnet", "SNMP and NTP"], "A",
         "The File Sharing service enables users to access enterprise file servers running SMB/CIFS (Windows file sharing) and NFS (UNIX/Linux file sharing) protocols directly through the SSL VPN web portal without installing network shares."),

        ("SSL VPN Service - Port Forwarding", "What type of applications is the SSL VPN Port Forwarding service primarily designed to support?",
         ["Dynamic routing protocols running on raw IP",
          "Static, TCP-based enterprise client-server applications (such as Telnet, SSH, RDP, VNC, and POP3/SMTP)",
          "UDP-based real-time broadcast audio streaming",
          "ICMP ping echo testing only"], "B",
         "Port Forwarding is designed for static TCP-based services. A lightweight control (ActiveX or Java or local agent) listens on a local loopback port and tunnels application TCP connections through the secure SSL session to internal target servers."),

        ("SSL VPN Service - Network Extension", "Which SSL VPN service provides full, transparent Layer 3 IP-level network access to internal resources, assigning the remote client a virtual IP address from a private address pool?",
         ["Web Proxy", "Port Forwarding", "File Sharing", "Network Extension"], "D",
         "Network Extension installs a virtual network adapter (virtual NIC) on the client PC. The virtual gateway assigns the client an intranet IP address from a designated IP pool, granting full Layer 3 access to corporate subnets as if the user were physically connected to the office LAN."),

        ("SSL VPN Virtual Gateway Concept", "In Huawei USG firewalls, what is the role of an 'SSL VPN Virtual Gateway'?",
         ["A physical backup firewall deployed in cold standby",
          "An independent, logically isolated virtual security instance with dedicated authentication policies, user databases, access permissions, and resource allocations",
          "An external DNS server managed by an ISP",
          "A hardware Ethernet switch module inside the chassis"], "B",
         "A Virtual Gateway is an independent logical entity within the USG firewall. Multiple virtual gateways can be hosted on a single physical firewall to serve distinct corporate departments, subsidiaries, or external partners with customized domains, branding, authentication methods, and security policies.")
    ]

    for item in s_data:
        single.append({
            "chapter_num": 11,
            "chapter_title": CHAPTER_NAMES[11],
            "topic": item[0],
            "type": "Single Choice",
            "stem": item[1],
            "options": item[2],
            "answer": item[3],
            "explanation": item[4]
        })

    # ==========================================
    # CHAPTER 11 MULTIPLE CHOICE (30 questions)
    # ==========================================
    m_data = [
        ("VPN Advantages", "Compared with traditional leased lines, what are the major operational and technical advantages of deploying VPNs? (Select all that apply)",
         ["Significantly lower operational deployment and maintenance costs",
          "High flexibility and scalability for adding new branch sites and mobile users",
          "Robust cryptographic protection including data confidentiality, integrity, and identity authentication",
          "Elimination of the need for all internal IP addresses and subnet masks"], "ABC",
         "VPNs leverage low-cost public networks, reduce infrastructure expenses, support rapid expansion of branches and remote workers, and utilize robust cryptography (encryption, integrity, authentication). They do not eliminate IP addressing; internal IP subnets remain fundamental."),

        ("VPN Classification Criteria", "By which criteria can VPN technologies be classified in enterprise networking? (Select all that apply)",
         ["By network layer: Layer 2 VPN (e.g. L2TP, PPTP), Layer 3 VPN (e.g. GRE, IPsec), Application Layer VPN (e.g. SSL VPN)",
          "By business application model: Site-to-Site VPN and Client-to-Site (Remote Access) VPN",
          "By operational model: Customer-provisioned VPN and Provider-provisioned VPN",
          "By color of the firewall front bezel and LED status lights"], "ABC",
         "VPNs are categorized by protocol layer (L2VPN, L3VPN, Application/L4-7 VPN), business deployment architecture (Site-to-Site, Client-to-Site/Remote Access), and service provisioning ownership (Customer-managed vs Carrier-managed)."),

        ("Key VPN Security Technologies", "Which core security technologies work together in a secure VPN framework like IPsec? (Select all that apply)",
         ["Tunneling encapsulation technology",
          "User identity authentication technology",
          "Cryptographic data encryption technology",
          "Data integrity verification and anti-replay technology"], "ABCD",
         "A complete secure VPN architecture integrates tunneling (packet encapsulation), identity authentication (certificates, PSKs), confidentiality (symmetric encryption like AES), and data integrity verification (hash functions and anti-replay windowing)."),

        ("IPsec Protocol Suite Architecture", "Which protocols and components belong to the standardized IPsec architecture? (Select all that apply)",
         ["Authentication Header (AH)",
          "Encapsulating Security Payload (ESP)",
          "Internet Key Exchange (IKE)",
          "Simple Network Management Protocol (SNMP)"], "ABC",
         "The standardized IPsec framework comprises AH (protocol 51), ESP (protocol 50), and IKE (UDP 500/4500) for key management. SNMP is a network monitoring protocol, not an IPsec security protocol."),

        ("AH Header Fields", "Which fields are present in the Authentication Header (AH) format? (Select all that apply)",
         ["Next Header",
          "Payload Length",
          "Security Parameter Index (SPI)",
          "Sequence Number",
          "Integrity Check Value (ICV)"], "ABCDE",
         "An AH header contains: Next Header (identifies the following protocol), Payload Length, Reserved, Security Parameter Index (SPI), Sequence Number (for anti-replay protection), and the Integrity Check Value (ICV)."),

        ("ESP Packet Structure", "Which components are part of an ESP encapsulated packet? (Select all that apply)",
         ["ESP Header (containing SPI and Sequence Number)",
          "Encrypted Payload Data (e.g. transport segment or inner IP packet)",
          "ESP Trailer (containing Padding, Pad Length, and Next Header)",
          "ESP Authentication Data (Integrity Check Value - ICV)"], "ABCD",
         "An ESP packet consists of the ESP Header (SPI, Sequence Number), the encrypted Payload, the ESP Trailer (Padding, Pad Length, Next Header), and trailing ESP Authentication Data (ICV)."),

        ("AH vs ESP Comparison", "In comparing AH and ESP protocols, which statements are TRUE? (Select all that apply)",
         ["AH does NOT support payload encryption, whereas ESP supports payload encryption",
          "AH authenticates the outer IP header (excluding mutable fields), while ESP does NOT authenticate the outer IP header",
          "AH is incompatible with NAT traversal, whereas ESP (with NAT-T) can traverse NAT gateways",
          "ESP can provide both confidentiality and integrity authentication simultaneously"], "ABCD",
         "All statements accurately compare AH and ESP: AH lacks encryption, protects outer IP headers, and breaks under NAT; ESP provides encryption, leaves outer IP headers unauthenticated, supports NAT-T, and can perform both encryption and integrity checking."),

        ("IPsec Operating Modes", "Which two operating encapsulation modes are supported by IPsec? (Select all that apply)",
         ["Transport Mode",
          "Tunnel Mode",
          "Promiscuous Mode",
          "Bridging Mode"], "AB",
         "IPsec operates in two encapsulation modes: Transport Mode (protects payload only, original IP header remains outer header) and Tunnel Mode (encapsulates entire original IP packet into a new outer IP header)."),

        ("IPsec Tunnel Mode Characteristics", "Which characteristics apply to IPsec Tunnel Mode? (Select all that apply)",
         ["A new outer IP header is generated and added in front of the AH/ESP header",
          "The source and destination IP addresses in the outer header represent the IPsec peer gateway interfaces",
          "The internal private IP addresses of host endpoints are concealed across the public WAN",
          "It is the standard mode for Site-to-Site VPN connections between enterprise firewalls"], "ABCD",
         "In Tunnel Mode, gateways add a new outer IP header with their own public IPs as source/destination, encapsulating and encrypting the original private IP packet. This conceals internal topologies and facilitates Site-to-Site connectivity across untrusted networks."),

        ("IPsec Transport Mode Applications", "In which scenarios is IPsec Transport Mode typically selected? (Select all that apply)",
         ["Host-to-Host secure communication where both end systems terminate IPsec directly",
          "GRE over IPsec, where GRE already encapsulates private packets and IPsec provides encryption without needing another redundant IP header",
          "Site-to-Site VPN between two branch offices where gateways conceal internal private IP schemes",
          "Secure management access (e.g., SNMP or SSH) directly to a specific firewall interface"], "ABD",
         "Transport Mode is ideal when end systems communicate directly (Host-to-Host), when securing management sessions directly to a gateway, or in GRE over IPsec (since GRE already adds an outer routing header, avoiding double outer headers). Site-to-Site subnet interconnects use Tunnel Mode."),

        ("Security Association (SA) Triplet", "An incoming IPsec packet is matched to a specific Security Association (SA) in the SADB using which three parameters? (Select all that apply)",
         ["Security Parameter Index (SPI)",
          "Destination IP address",
          "Security Protocol identifier (AH or ESP)",
          "Source MAC address of the switch"], "ABC",
         "Under RFC standard IPsec, an SA is uniquely indexed in the Security Association Database (SADB) by the triplet: {SPI, Destination IP Address, Security Protocol (AH or ESP)}."),

        ("SA Establishment Methods", "Through which methods can IPsec Security Associations be established on Huawei firewalls? (Select all that apply)",
         ["Manual configuration (hardcoding keys, SPIs, and algorithms statically on both ends)",
          "IKE dynamic negotiation (using IKEv1 or IKEv2 to automatically negotiate parameters and refresh keys)",
          "Automatic assignment via DHCP Option 43",
          "Physical USB key insertion on boot"], "AB",
         "IPsec SAs can be established manually (manual mode, suitable for simple testing or static point-to-point links with no IKE) or dynamically via IKE (IKEv1/IKEv2, recommended for production networks due to automatic rekeying and scalability)."),

        ("IKE Phase 1 Main Mode Steps", "In IKEv1 Phase 1 Main Mode, what is accomplished across the 6 message exchanges? (Select all that apply)",
         ["Messages 1 and 2 negotiate the IKE security proposal (encryption algorithm, hash algorithm, authentication method, DH group, SA lifetime)",
          "Messages 3 and 4 perform Diffie-Hellman public key exchange and exchange random nonces to generate keying material",
          "Messages 5 and 6 exchange encrypted peer identities and authentication signatures/hashes",
          "Messages 1 through 6 transmit all user data packets across the VPN"], "ABC",
         "Main Mode executes in 3 distinct 2-message pairs: (1-2) Proposal negotiation; (3-4) DH exchange and nonce distribution; (5-6) Encrypted identity verification. User data is never transmitted in Phase 1; user data is transmitted after Phase 2 establishes IPsec SAs."),

        ("IKEv1 Authentication Methods", "Which authentication methods are supported in IKEv1 Phase 1? (Select all that apply)",
         ["Pre-Shared Key (PSK) authentication",
          "Digital Signature (RSA / X.509 Certificate) authentication",
          "Kerberos token authentication",
          "Cleartext PAP password over HTTP"], "AB",
         "IKEv1 Phase 1 primarily supports Pre-Shared Key (PSK) authentication and Digital Signature (PKI / X.509 certificates) authentication."),

        ("IKEv1 Main vs Aggressive Mode", "Which statements correctly highlight the differences between IKEv1 Main Mode and Aggressive Mode? (Select all that apply)",
         ["Main Mode uses 6 messages, whereas Aggressive Mode uses only 3 messages",
          "Main Mode encrypts peer identities (in messages 5 and 6), whereas Aggressive Mode transmits peer identities in cleartext (in messages 1 and 2)",
          "Aggressive Mode negotiates faster than Main Mode",
          "Aggressive Mode can be deployed with PSK when the initiator has a dynamic IP address and uses Name IDs"], "ABCD",
         "All four statements are correct. Aggressive Mode completes in 3 messages without identity encryption, trading confidentiality of identities for faster speed and compatibility with dynamic-IP initiators using PSK."),

        ("IKEv1 Phase 2 Quick Mode Functions", "Which tasks are carried out during IKEv1 Phase 2 Quick Mode? (Select all that apply)",
         ["Negotiating IPsec SA security proposals (encapsulation protocol, encryption, authentication, encapsulation mode)",
          "Exchanging traffic selectors (Proxy IDs / ACLs) defining which traffic is protected",
          "Optionally executing an additional Diffie-Hellman exchange if Perfect Forward Secrecy (PFS) is enabled",
          "Establishing the IKE SA control channel"], "ABC",
         "Quick Mode negotiates IPsec SAs, exchanges proxy IDs (data flows), and derives fresh session keys (with optional PFS DH exchange). The IKE SA is established earlier during Phase 1, not Phase 2."),

        ("Diffie-Hellman (DH) Groups", "Which statements regarding Diffie-Hellman (DH) key exchange in IPsec are TRUE? (Select all that apply)",
         ["DH allows two parties to securely establish a shared secret over an insecure channel without transmitting the secret itself",
          "Higher DH group numbers (such as Group 14, 19, 20) provide larger key lengths and stronger security than older Group 1 or Group 2",
          "DH groups directly encrypt the user data packets flowing through the IPsec tunnel",
          "DH calculations rely on mathematically difficult discrete logarithm problems or elliptic curves"], "ABD",
         "DH is a key agreement algorithm (not a symmetric bulk data encryption algorithm). It allows peers to derive shared secrets over untrusted links based on discrete logarithms or elliptic curves, with higher groups offering stronger resistance against cryptanalysis."),

        ("IKEv2 Improvements over IKEv1", "What advantages and architectural improvements does IKEv2 provide over IKEv1? (Select all that apply)",
         ["Significantly faster negotiation: initial negotiation completes in 4 messages instead of 9",
          "Native support for NAT Traversal (NAT-T) without requiring proprietary draft extensions",
          "Built-in support for EAP (Extensible Authentication Protocol) allowing diverse user authentication schemes",
          "Elimination of the complex separation into Main Mode, Aggressive Mode, and Quick Mode"], "ABCD",
         "IKEv2 consolidates multiple exchange modes into a streamlined 4-message initial exchange (IKE_SA_INIT and IKE_AUTH), natively integrates NAT-T and DPD, and natively supports EAP for enterprise identity integration."),

        ("NAT Traversal (NAT-T) Mechanism", "Which statements regarding NAT Traversal (NAT-T) in IPsec are TRUE? (Select all that apply)",
         ["NAT-T detects the presence of NAT devices by comparing hash values of IP addresses and ports in vendor-specific payloads",
          "When NAT is detected, traffic switches to UDP port 4500",
          "ESP packets are encapsulated inside a UDP header to allow port translation by PAT devices",
          "NAT-T allows AH protocol packets to successfully traverse NAT gateways without ICV errors"], "ABC",
         "NAT-T encapsulates ESP in UDP port 4500 so PAT devices can track translation sessions via UDP ports. AH cannot traverse NAT even with NAT-T because AH protects the outer IP header itself, which NAT inescapably alters."),

        ("IPsec Policy Configuration Elements", "When configuring an IPsec Policy (`ipsec policy`) on a Huawei USG firewall, which parameters must typically be referenced or configured? (Select all that apply)",
         ["An ACL (Access Control List) defining the interesting traffic (data flow to protect)",
          "An IPsec Proposal defining security encapsulation, encryption, and authentication algorithms",
          "An IKE Peer specifying remote peer address, pre-shared key, and IKE version (in IKE-negotiated policies)",
          "The color depth of the firewall web interface"], "ABC",
         "An IPsec policy binds together: (1) ACL identifying interesting traffic; (2) IPsec proposal specifying data plane crypto; and (3) IKE peer specifying control plane negotiation parameters."),

        ("L2TP VPN Architecture Features", "Which statements regarding L2TP VPNs are TRUE? (Select all that apply)",
         ["L2TP operates over UDP port 1701",
          "L2TP encapsulates PPP frames to transport Layer 2 protocols across IP networks",
          "L2TP provides strong built-in encryption and hashing by default without requiring any other protocol",
          "L2TP is commonly combined with IPsec (L2TP over IPsec) to provide robust data confidentiality and integrity"], "ABD",
         "L2TP uses UDP 1701 and encapsulates PPP frames, but it lacks native data encryption. Therefore, it is paired with IPsec (L2TP over IPsec) to secure remote access dial-up connections."),

        ("SSL VPN Service Types", "Which four major service modules are provided by the SSL VPN solution on Huawei USG firewalls? (Select all that apply)",
         ["Web Proxy (Web Browsing)",
          "File Sharing",
          "Port Forwarding",
          "Network Extension"], "ABCD",
         "Huawei USG firewalls provide four core SSL VPN service categories: Web Proxy, File Sharing (SMB/NFS), Port Forwarding (TCP applications), and Network Extension (Layer 3 virtual adapter IP access)."),

        ("SSL VPN Web Proxy Characteristics", "Which characteristics describe the SSL VPN Web Proxy service? (Select all that apply)",
         ["Requires no client software or browser plug-in installation",
          "Allows remote users to access internal HTTP and HTTPS web resources",
          "The virtual gateway rewrites internal links and handles proxy requests securely",
          "Allows raw UDP audio broadcasts to stream directly without proxying"], "ABC",
         "Web Proxy is entirely clientless, running natively inside any standard browser to provide access to internal HTTP/HTTPS web applications. The gateway acts as a reverse proxy, rewriting URLs to keep internal servers hidden."),

        ("SSL VPN Port Forwarding Characteristics", "Which statements describe the SSL VPN Port Forwarding service? (Select all that apply)",
         ["It is designed for non-web, TCP-based client-server applications like Telnet, SSH, Remote Desktop (RDP), and VNC",
          "A lightweight local agent (ActiveX, Java, or standalone control) intercepts traffic destined for a local loopback port",
          "It natively supports dynamic multi-channel UDP streaming media protocols without special agents",
          "Traffic is multiplexed and encrypted over the existing SSL tunnel to the virtual gateway"], "ABD",
         "Port Forwarding forwards static TCP client-server connections via local port listening over the SSL tunnel. It does not natively support dynamic UDP or raw IP protocols."),

        ("SSL VPN Network Extension Features", "Which features characterize the SSL VPN Network Extension service? (Select all that apply)",
         ["It installs a virtual network interface card (virtual NIC) on the client operating system",
          "The client PC is assigned an internal IP address from an IP address pool configured on the virtual gateway",
          "It provides full Layer 3 IP connectivity, enabling support for both TCP and UDP protocols",
          "It requires the client to replace its physical router with a Huawei hardware firewall"], "ABC",
         "Network Extension delivers complete Layer 3 IP networking via a virtual NIC and private IP pool, supporting TCP, UDP, ICMP, and complex enterprise software. It runs entirely in software on the user's existing PC/laptop."),

        ("SSL VPN Network Extension Routing Modes", "Which routing/tunneling modes can be configured for SSL VPN Network Extension on Huawei firewalls? (Select all that apply)",
         ["Manual Mode (routes are manually defined by the administrator)",
          "Split Tunnel Mode (only traffic destined for enterprise intranet subnets passes through the SSL tunnel, while general Internet traffic routes directly via the local gateway)",
          "Full Tunnel Mode (all client traffic, including public Internet browsing, is forced through the SSL VPN tunnel to the enterprise gateway)",
          "Infinite Broadcast Mode"], "ABC",
         "Network Extension supports Manual, Split Tunnel (efficient bandwidth usage: only enterprise traffic uses the tunnel), and Full Tunnel (strict security: all traffic routes through the enterprise firewall for inspection and logging)."),

        ("SSL VPN User Authentication Methods", "Which authentication methods can be used to verify remote users logging into an SSL VPN virtual gateway? (Select all that apply)",
         ["Local authentication on the USG firewall",
          "RADIUS server authentication",
          "LDAP / Active Directory (AD) authentication",
          "Digital certificate (PKI / USB token) authentication"], "ABCD",
         "Huawei SSL VPN virtual gateways support flexible authentication mechanisms: local database, external AAA/RADIUS, enterprise LDAP/AD directories, and PKI digital certificates (including dual-factor certificate + password authentication)."),

        ("GRE over IPsec Value", "Why is GRE over IPsec frequently implemented in enterprise wide-area networks? (Select all that apply)",
         ["GRE can encapsulate multicast packets and dynamic routing protocol hello/update packets (such as OSPF)",
          "Standard IPsec unicast tunnels cannot directly transport multicast or dynamic routing protocol traffic",
          "IPsec provides strong encryption and integrity protection for the GRE encapsulated packets",
          "GRE eliminates the need for any IPsec Security Associations"], "ABC",
         "IPsec does not natively encrypt broadcast or multicast packets (used by dynamic routing protocols like OSPF). By encapsulating multicast in GRE first, and then encapsulating GRE inside an IPsec tunnel (GRE over IPsec), the network achieves secure dynamic routing across the WAN."),

        ("IPsec Anti-Replay Mechanism", "How does the IPsec anti-replay mechanism protect against replay attacks? (Select all that apply)",
         ["The sender assigns a monotonically increasing 32-bit or 64-bit Sequence Number to each AH/ESP packet",
          "The receiver maintains a sliding anti-replay window to track received sequence numbers",
          "Packets with duplicate sequence numbers or sequence numbers falling behind the left edge of the window are discarded",
          "Sequence numbers are reset to 0 every 10 seconds automatically"], "ABC",
         "Anti-replay uses strictly increasing sequence numbers and a receiver sliding window. Replayed (duplicate) packets or expired packets falling outside the window are immediately dropped. Sequence numbers do not cycle or reset automatically without a complete SA rekey."),

        ("SSL VPN vs IPsec VPN Comparison", "Which operational comparisons between SSL VPN and IPsec VPN are ACCURATE? (Select all that apply)",
         ["SSL VPN is typically preferred for mobile remote access users due to ease of clientless/browser deployment",
          "IPsec VPN is typically preferred for Site-to-Site LAN interconnects between corporate offices due to high throughput and transparency to endpoints",
          "SSL VPN operates primarily across TCP port 443, easily traversing firewalls and NAT without special port forwarding",
          "IPsec VPN requires lower CPU utilization than cleartext HTTP"], "ABC",
         "SSL VPN excels at remote worker access over standard HTTPS (port 443), effortlessly traversing NAT and guest firewalls. IPsec VPN excels at high-speed, transparent Site-to-Site LAN interconnection between branch routers/firewalls.")
    ]

    for item in m_data:
        multi.append({
            "chapter_num": 11,
            "chapter_title": CHAPTER_NAMES[11],
            "topic": item[0],
            "type": "Multiple Choice",
            "stem": item[1],
            "options": item[2],
            "answer": item[3],
            "explanation": item[4]
        })

    # ==========================================
    # CHAPTER 11 TRUE / FALSE (32 questions)
    # ==========================================
    t_data = [
        ("VPN Public Infrastructure", "A Virtual Private Network (VPN) builds a logical private network on top of a shared public network infrastructure.",
         "A",
         "True. VPN leverages public shared transmission networks (such as the Internet) to establish logically isolated, private, and encrypted communication tunnels."),

        ("GRE Encryption Capability", "Standard Generic Routing Encapsulation (GRE) natively provides strong AES-256 encryption to protect payload data.",
         "B",
         "False. Standard GRE provides no native encryption or integrity protection whatsoever. All passenger data inside standard GRE tunnels is transmitted in cleartext."),

        ("GRE Multicast Support", "GRE tunnels support encapsulating multicast and broadcast packets, enabling dynamic routing protocols like OSPF to establish neighbor relationships across the tunnel.",
         "A",
         "True. Unlike raw IPsec tunnels, GRE can encapsulate broadcast, multicast, and non-IP protocols, making it suitable for running dynamic routing protocols over WAN links."),

        ("AH Header Encryption", "The Authentication Header (AH) protocol encrypts the packet payload so that unauthorized eavesdroppers cannot inspect the data.",
         "B",
         "False. AH does not provide any encryption (confidentiality). Its function is strictly limited to data origin authentication, data integrity verification (via ICV), and anti-replay protection."),

        ("AH and NAT Conflict", "Deploying the AH protocol across a Network Address Translation (NAT) router will result in packet drop because NAT modifies the IP header, causing ICV integrity check failure at the receiver.",
         "A",
         "True. AH computes its ICV over the immutable fields of the IP header. When NAT translates IP addresses, the header changes, causing the receiver's ICV verification to fail and drop the packet."),

        ("ESP Header Encryption", "The ESP protocol can encrypt user data and optionally authenticate both the payload and the outer IP header.",
         "B",
         "False. ESP encrypts the payload and can authenticate the payload and ESP header, but ESP NEVER authenticates the outer IP header. Authenticating the outer IP header is an AH feature."),

        ("IPsec Transport Mode Outer Header", "In IPsec Transport Mode, the gateway generates and prepends a new outer IP header in front of the AH or ESP header.",
         "B",
         "False. Transport mode does NOT add a new IP header; it keeps the original IP header and inserts the AH/ESP header between the IP header and the transport payload."),

        ("IPsec Tunnel Mode Scope", "In IPsec Tunnel Mode, the entire original IP packet, including its original IP header and payload, is encapsulated and protected.",
         "A",
         "True. Tunnel mode encapsulates the complete original IP packet inside an AH/ESP header and prepends a brand-new outer IP header for routing across the intermediate transit network."),

        ("IPsec SA Directionality", "An IPsec Security Association (SA) is bidirectional, meaning a single SA handles both inbound and outbound traffic between two peers.",
         "B",
         "False. IPsec SAs are strictly unidirectional (simplex). Bidirectional communication requires at least two distinct SAs: one inbound and one outbound."),

        ("SPI Uniqueness", "The Security Parameter Index (SPI) is a 32-bit identifier in the AH/ESP header that helps the receiver identify the appropriate inbound Security Association.",
         "A",
         "True. The SPI, combined with the destination IP address and security protocol (AH/ESP), uniquely indexes the exact inbound SA in the receiver's Security Association Database (SADB)."),

        ("IKE Port Number", "The Internet Key Exchange (IKE) protocol negotiates Security Associations over UDP port 500 by default.",
         "A",
         "True. IKE uses UDP port 500 for standard message negotiations. (It switches to UDP port 4500 when NAT Traversal is engaged)."),

        ("IKEv1 Phase Count", "IKEv1 negotiation is divided into two distinct phases: Phase 1 establishes the IKE SA, and Phase 2 establishes the IPsec SAs.",
         "A",
         "True. IKEv1 strictly divides negotiation into Phase 1 (establishing a secure IKE SA control channel) and Phase 2 (negotiating the actual data-protecting IPsec SAs via Quick Mode)."),

        ("IKEv1 Main Mode Packet Total", "IKEv1 Phase 1 Main Mode exchanges exactly four packets to complete negotiation.",
         "B",
         "False. IKEv1 Phase 1 Main Mode strictly requires 6 packets (3 pairs of request/response messages) to negotiate proposals, perform DH exchange, and verify encrypted identities."),

        ("IKEv1 Main Mode Identity Privacy", "In IKEv1 Main Mode, peer identity information is protected by encryption during transmission.",
         "A",
         "True. In Main Mode, identity information is exchanged in messages 5 and 6, which are encrypted using the session key derived during messages 3 and 4."),

        ("IKEv1 Aggressive Mode Packet Total", "IKEv1 Phase 1 Aggressive Mode completes its negotiation using only three packets.",
         "A",
         "True. Aggressive Mode completes Phase 1 in 3 messages: Message 1 (initiator to responder), Message 2 (responder to initiator), and Message 3 (initiator confirmation)."),

        ("IKEv1 Aggressive Mode Privacy", "IKEv1 Aggressive Mode encrypts the peer identity information in the first message.",
         "B",
         "False. In Aggressive Mode, peer identities are sent in cleartext in the first two messages because the shared secret has not yet been computed."),

        ("IKEv1 Quick Mode Function", "IKEv1 Phase 2 Quick Mode is used to negotiate IPsec SAs and user data encryption parameters under the protection of the Phase 1 IKE SA.",
         "A",
         "True. Quick Mode operates inside the encrypted Phase 1 tunnel to negotiate IPsec SAs, proxy IDs (ACLs), and session keys for user data protection."),

        ("Perfect Forward Secrecy Benefit", "Perfect Forward Secrecy (PFS) ensures that if an attacker compromises an IKE Phase 1 key in the future, past and future IPsec Phase 2 session keys cannot be decrypted.",
         "A",
         "True. PFS forces an independent Diffie-Hellman exchange during Phase 2 Quick Mode, breaking the mathematical link between Phase 1 keys and Phase 2 data keys."),

        ("IKEv2 Packet Efficiency", "IKEv2 requires only 4 messages in its initial exchange to establish both the IKE SA and the initial IPsec Child SA.",
         "A",
         "True. IKEv2 consolidates Phase 1 and Phase 2 into two 2-message exchanges: IKE_SA_INIT (negotiating IKE SA) and IKE_AUTH (authenticating identity and creating the first Child SA)."),

        ("IKEv2 Main and Aggressive Modes", "IKEv2 retains the separate Main Mode and Aggressive Mode negotiation options from IKEv1.",
         "B",
         "False. IKEv2 completely eliminated the confusing distinction between Main Mode and Aggressive Mode, replacing them with a unified initial exchange."),

        ("NAT-T UDP Port 4500", "When NAT Traversal (NAT-T) is active, ESP packets are encapsulated within UDP packets using destination port 4500.",
         "A",
         "True. NAT-T wraps ESP packets in a UDP header using port 4500, enabling stateful PAT routers to translate and track the session using UDP port mappings."),

        ("Dead Peer Detection Keepalives", "Dead Peer Detection (DPD) sends keepalive probes to confirm the operational status of the remote IPsec gateway.",
         "A",
         "True. DPD actively monitors the responsiveness of the peer gateway, cleaning up stale SAs and initiating failover if the remote peer stops responding."),

        ("L2TP Native Encryption", "L2TP protocol natively includes strong symmetric data encryption algorithms such as 3DES and AES.",
         "B",
         "False. L2TP only provides Layer 2 frame tunneling and user authentication; it has no native encryption. Data confidentiality must be provided by pairing it with IPsec (L2TP over IPsec)."),

        ("SSL VPN Port Traversal", "SSL VPN primarily operates over TCP port 443 (HTTPS), allowing it to easily pass through most corporate firewalls and NAT gateways without modifying port forwarding rules.",
         "A",
         "True. Because HTTPS (TCP 443) is almost universally permitted through enterprise firewalls and proxy servers, SSL VPN traffic traverses intermediate networks with minimal friction."),

        ("SSL VPN Web Proxy Client Requirement", "The SSL VPN Web Proxy service requires users to install a dedicated software client with administrator privileges on their local computers.",
         "B",
         "False. Web Proxy is clientless; remote users access internal web servers entirely through standard web browsers without installing local software or needing administrator privileges."),

        ("SSL VPN File Sharing Protocols", "The SSL VPN File Sharing service enables users to access SMB/CIFS and NFS shares via a web browser interface.",
         "A",
         "True. The USG firewall converts browser requests into internal SMB/CIFS or NFS file transactions, displaying files and folders directly in the user's web browser."),

        ("SSL VPN Port Forwarding Scope", "The SSL VPN Port Forwarding service is designed to forward static, TCP-based enterprise applications such as Telnet, SSH, and RDP.",
         "A",
         "True. Port Forwarding intercepts and forwards connections for preconfigured TCP client-server applications via local port listening."),

        ("SSL VPN Network Extension IP Assignment", "In SSL VPN Network Extension mode, the remote client receives a virtual IP address from a private address pool configured on the SSL VPN virtual gateway.",
         "A",
         "True. Network Extension operates at Layer 3, installing a virtual NIC and leasing an internal private IP address to the remote endpoint to enable full intranet routing."),

        ("SSL VPN Split Tunneling Bandwidth", "Split Tunnel mode in SSL VPN Network Extension sends only enterprise-bound intranet traffic through the VPN tunnel, conserving corporate gateway bandwidth.",
         "A",
         "True. Under Split Tunneling, only packets destined for corporate subnets traverse the SSL VPN tunnel; regular Internet traffic exits directly via the user's local ISP connection."),

        ("SSL VPN Full Tunnel Security", "Full Tunnel mode in SSL VPN Network Extension forces all user network traffic, including public Internet browsing, through the enterprise SSL VPN gateway.",
         "A",
         "True. Full Tunneling ensures all outbound traffic passes through corporate firewalls for unified security inspection, DLP auditing, and content filtering."),

        ("SSL VPN Virtual Gateway Multi-Tenancy", "A single Huawei USG physical firewall can be partitioned into multiple independent SSL VPN Virtual Gateways to serve distinct user groups or tenant organizations.",
         "A",
         "True. Huawei USG firewalls support virtual gateways, allowing multiple isolated virtual VPN instances on a single physical appliance with independent branding, user bases, and security policies."),

        ("GRE over IPsec Multicast Routing", "GRE over IPsec combines the routing flexibility of GRE (multicast and dynamic routing support) with the security features of IPsec (encryption and authentication).",
         "A",
         "True. GRE over IPsec encapsulates multicast/dynamic routing traffic inside GRE, which is then encrypted by IPsec, achieving both routing capability and high-grade data protection.")
    ]

    for item in t_data:
        tf.append({
            "chapter_num": 11,
            "chapter_title": CHAPTER_NAMES[11],
            "topic": item[0],
            "type": "True/False",
            "stem": item[1],
            "options": ["True", "False"],
            "answer": item[2],
            "explanation": item[3]
        })

    return single, multi, tf

if __name__ == "__main__":
    s, m, t = get_ch11_questions()
    print(f"Chapter 11 generated: {len(s)} Single, {len(m)} Multi, {len(t)} TF. Total = {len(s)+len(m)+len(t)}")
