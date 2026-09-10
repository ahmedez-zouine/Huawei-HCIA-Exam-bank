# scripts/bank_part1.py
"""
Part 1: Single-Answer Questions (Single Choice) - 420 Questions
Covering Chapters 1 to 11 of HCIA-Security V3.0
"""

def get_part1_questions():
    questions = []
    
    # We will populate 420 questions across all 11 chapters.
    # Helper to add question
    def add_q(ch, topic, stem, options, ans, exp):
        qid = len(questions) + 1
        questions.append({
            "id": qid,
            "chapter": ch,
            "topic": topic,
            "type": "Single Choice",
            "stem": stem,
            "options": options,
            "answer": ans,
            "explanation": exp
        })

    # =========================================================================
    # CHAPTER 1: Network Security Concepts and Specifications (Q1 - Q36)
    # =========================================================================
    add_q(1, "CIA Triad - Confidentiality",
          "Which of the following security attributes ensures that sensitive information is not disclosed to unauthorized entities or eavesdropped during transmission?",
          ["Integrity", "Confidentiality", "Availability", "Non-repudiation"],
          "B",
          "Confidentiality ensures that information can be accessed and viewed only by authorized personnel. Even if data packets are intercepted across untrusted networks, encryption prevents unauthorized parties from reading the plaintext contents.")

    add_q(1, "CIA Triad - Integrity",
          "Which security property guarantees that transmitted data has not been altered, deleted, or forged in transit?",
          ["Availability", "Integrity", "Confidentiality", "Authenticity"],
          "B",
          "Integrity guarantees that data has not been tampered with or modified during transit or storage. Cryptographic hash functions (such as SHA-256) and message authentication codes are primary mechanisms to verify integrity.")

    add_q(1, "CIA Triad - Availability",
          "An enterprise web service is taken down by a volumetric SYN flood attack, preventing legitimate clients from accessing their accounts. Which principle of the CIA triad has been violated?",
          ["Confidentiality", "Integrity", "Availability", "Controllability"],
          "C",
          "Availability ensures that authorized users have prompt and reliable access to information assets and network services. DoS/DDoS attacks specifically target availability by exhausting network bandwidth or server compute resources.")

    add_q(1, "Security History - Eras",
          "In the evolution of information security, what was the primary characteristic of the 'Communication Security' era during the 1940s?",
          ["Focus on cyberspace sovereignty and IoT devices",
           "Protection was primarily confined to physical security and cipher-based transmission (e.g., stream ciphers)",
           "Emphasis on multi-dimensional active defense and SIEM orchestration",
           "Standardization of enterprise security architectures such as ISO 27001"],
          "B",
          "During the 1940s Communication Security era, communication technologies were underdeveloped. Information security focused on physical security and point-to-point cipher transmission (primarily stream ciphers) to protect confidential military/diplomatic telegrams.")

    add_q(1, "Security History - 1990s Information Assurance",
          "During the 1990s Information Assurance period, which two new security principles were emphasized alongside the traditional CIA triad?",
          ["Simplicity and Scalability", "Controllability and Non-repudiation", "Virtualization and Micro-segmentation", "Resilience and Fault-tolerance"],
          "B",
          "In the 1990s Information Assurance era, as the Internet expanded rapidly, Controllability (ability to monitor and control information and systems) and Non-repudiation (inability to deny transmitted actions/data) joined the CIA triad to form the five core security principles.")

    add_q(1, "Non-repudiation",
          "Which cryptographic technology is primarily utilized to provide non-repudiation in electronic transactions?",
          ["Symmetric block ciphers like AES-256", "Pre-shared keys (PSK)", "Digital signatures using asymmetric private keys", "Stream ciphers like RC4"],
          "C",
          "Non-repudiation prevents a sender from denying having sent a message. It is achieved through digital signatures, where only the sender possesses the unique private key required to generate the signature.")

    add_q(1, "Information Security Standards - ISO 27001 vs ISO 27002",
          "Which of the following standards specifies requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS) and is used for organizational certification?",
          ["ISO/IEC 27002", "ISO/IEC 27001", "ISO/IEC 27005", "RFC 1918"],
          "B",
          "ISO/IEC 27001 provides the formal normative specification for an enterprise Information Security Management System (ISMS) and serves as the certification benchmark. ISO 27002 provides guidance and codes of practice for implementing security controls.")

    add_q(1, "Information Security Standards - ISO 27002 Purpose",
          "What is the primary role of ISO/IEC 27002 within the ISO 27000 series?",
          ["A formal audit standard against which an enterprise receives an accredited certificate",
           "A code of practice containing reference control objectives and actionable security controls",
           "A hardware encryption standard for high-speed fiber communications",
           "A regulatory framework for national critical infrastructure penal sanctions"],
          "B",
          "ISO/IEC 27002 provides a comprehensive code of practice and implementation guidelines for information security controls, helping organizations select and implement controls defined in Annex A of ISO 27001.")

    add_q(1, "Cybersecurity Classified Protection 2.0 - Levels",
          "Under Cybersecurity Classified Protection 2.0 (China's National Standard MLPS 2.0), how many security protection levels are defined?",
          ["Three levels", "Four levels", "Five levels", "Seven levels"],
          "C",
          "Classified Protection 2.0 defines five security levels: Level 1 (User Autonomy), Level 2 (System Audit), Level 3 (Supervised Protection), Level 4 (Mandatory Protection), and Level 5 (Special Control Protection).")

    add_q(1, "Cybersecurity Classified Protection 2.0 - Level 3",
          "In Classified Protection 2.0, Level 3 protection applies to information systems whose compromise would cause which severity of impact?",
          ["Slight harm to legitimate rights of citizens, but no harm to social order or public interest",
           "Serious harm to social order and public interest, or harm to national security",
           "Extremely serious harm to national security directly causing collapse of state governance",
           "General harm to enterprise profitability without any public impact"],
          "B",
          "Level 3 (Supervised Protection) applies to critical networks where security incidents cause serious harm to social order and public interests, or significant harm to national security. Most government and financial online systems require Level 3 compliance.")

    add_q(1, "TCSEC - Orange Book Levels",
          "In the Trusted Computer System Evaluation Criteria (TCSEC, Orange Book), which division represents the highest level of security evaluation?",
          ["Division D", "Division C", "Division B", "Division A"],
          "D",
          "TCSEC categorizes systems into four divisions: D (Minimal protection), C (Discretionary protection: C1, C2), B (Mandatory protection: B1, B2, B3), and A (Verified protection: A1), where Division A is the highest verified security level.")

    add_q(1, "TCSEC - C2 Level",
          "Which TCSEC division and class introduced individual user identification and auditing requirements (Discretionary Access Control)?",
          ["Class D", "Class C2", "Class B2", "Class A1"],
          "B",
          "Class C2 (Controlled Access Protection) enforces individual login accountability, discretionary access control (DAC), and comprehensive audit trail logging, making it the historical baseline for commercial operating systems.")

    add_q(1, "Advanced Persistent Threat (APT)",
          "Which of the following is a prominent characteristic of an Advanced Persistent Threat (APT)?",
          ["Uncoordinated, short-duration high-volume automated ping sweeps",
           "Highly organized, stealthy, customized, and persistent attack targeting high-value assets over an extended period",
           "Purely accidental misconfigurations caused by novice network operators",
           "Public Wi-Fi packet sniffing without target selection"],
          "B",
          "An APT is characterized by advanced attack techniques, persistent reconnaissance, stealthy lateral movement, and evasion of conventional defenses, sustained over long durations to extract intellectual property or sabotage operations.")

    add_q(1, "Zero Trust Architecture",
          "What is the foundational philosophy of the Zero Trust security model?",
          ["Trust internal network traffic by default; inspect only perimeter traffic",
           "Never trust, always verify; inspect and authenticate every request regardless of network location",
           "Rely solely on hardware border firewalls to defend the trusted core",
           "Grant unrestricted administrative privileges once user identity is validated at login"],
          "B",
          "Zero Trust operates under the tenet 'Never Trust, Always Verify'. It assumes breaches are inevitable, eliminating implicit trust based on network locality and requiring continuous verification of identity, device, and context.")

    add_q(1, "Software-Defined Perimeter (SDP)",
          "In a Software-Defined Perimeter (SDP) framework, how is network connectivity established?",
          ["Servers broadcast their IP and open ports publicly to allow direct client discovery",
           "The infrastructure remains invisible ('dark') until an SDP controller validates user and device identity",
           "Static security policies are permanently mapped to physical switch ports",
           "All communications bypass encryption to accelerate line-rate throughput"],
          "B",
          "SDP follows a 'Need-to-Know' paradigm where protected servers and services remain invisible behind Gateways. Connectivity is dynamically granted only after the centralized SDP Controller verifies client identity and device posture.")

    add_q(1, "Cybersecurity Legal Framework",
          "What is the primary objective of national cybersecurity laws and data security regulations?",
          ["To eliminate the need for enterprise firewalls and antivirus software",
           "To safeguard cyberspace sovereignty, national security, public interest, and lawful citizen data rights",
           "To mandate that all enterprise networks use unencrypted communication protocols",
           "To replace internal enterprise security audits with foreign third-party certification"],
          "B",
          "National cybersecurity regulations establish statutory obligations for network operators to protect critical infrastructure, maintain operational continuity, prevent cybercrimes, and protect citizens' personal privacy.")

    add_q(1, "Social Engineering",
          "An attacker posing as an IT support engineer contacts an employee to obtain their domain credentials under the guise of an urgent security upgrade. What attack type is this?",
          ["Port scanning", "Smurf attack", "Social engineering / Phishing", "Buffer overflow"],
          "C",
          "Social engineering exploits human psychology rather than software vulnerabilities. Attackers use impersonation, pretexts, urgency, or deception to trick authorized personnel into disclosing credentials or sensitive data.")

    add_q(1, "Defense-in-Depth Principle",
          "What is the fundamental benefit of implementing a 'Defense-in-Depth' architecture?",
          ["It guarantees 100% immunity against zero-day malware without software updates",
           "If a single defensive mechanism fails, multiple subsequent layers continue to protect critical assets",
           "It eliminates the need for user authentication and authorization",
           "It consolidates all security functions onto a single border router"],
          "B",
          "Defense-in-Depth deploys multiple overlapping security controls across physical, perimeter, network, host, application, and data tiers, ensuring that compromise of any single layer does not compromise the entire enterprise.")

    add_q(1, "Security Policy Lifecycle",
          "Which sequence correctly describes the continuous improvement lifecycle for enterprise security management?",
          ["Execute -> Terminate -> Delete -> Ignore",
           "Plan -> Do -> Check -> Act (PDCA)",
           "Attack -> Defend -> Forget -> Re-install",
           "Inspect -> Block -> Allow -> Reset"],
          "B",
          "The PDCA (Plan-Do-Check-Act) Deming cycle is the standard management framework adopted by ISO 27001 for establishing, maintaining, and continually optimizing organizational information security policies.")

    add_q(1, "Classified Protection 2.0 - Technical Requirements",
          "Which of the following is NOT one of the four general technical requirement domains in Classified Protection 2.0?",
          ["Physical and Environmental Security", "Network and Communication Security", "Equipment and Computing Security", "Marketing and Public Relations Security"],
          "D",
          "The four core technical requirement areas in Classified Protection 2.0 are: Physical and Environmental Security, Network and Communication Security, Equipment and Computing Security, and Application and Data Security.")

    add_q(1, "Classified Protection 2.0 - Management Requirements",
          "Which of the following belongs to the general security management requirements in Classified Protection 2.0?",
          ["Security Management System, Organization, Personnel, Construction, and Operation",
           "Hardware BIOS Flashing and CPU Overclocking",
           "External Advertising and Social Media Marketing",
           "Quarterly Revenue Reporting and Tax Filing"],
          "A",
          "The five management requirement domains under Classified Protection 2.0 comprise: Security Management System, Security Management Organization, Security Management Personnel, Security Construction Management, and Security Operation Management.")

    add_q(1, "Threat Intelligence",
          "What is the primary function of a Security Intelligence Center (such as Huawei Cloud Security Intelligence)?",
          ["To remotely format local enterprise hard drives during high load",
           "To aggregate global threat feeds, analyze zero-day exploits, and distribute real-time signature updates",
           "To replace local enterprise network switches with software emulators",
           "To permanently assign public IPv4 addresses to unauthorized mobile devices"],
          "B",
          "Security Intelligence Centers analyze global telemetry, malware binaries, and emerging exploits using big data analytics and AI, producing up-to-date threat feeds, IPS/AV signatures, and malicious IP/domain blacklists.")

    add_q(1, "Cyberspace Domain Characteristics",
          "Why is cyberspace considered an artificial, man-made operational domain compared to land, sea, air, and space?",
          ["It exists purely as a natural physical phenomenon without hardware",
           "It is built upon physical microelectronics, logical network protocols, and software created by human engineering",
           "It operates entirely without electrical power or telecommunication links",
           "It is governed solely by international maritime law"],
          "B",
          "Cyberspace is an engineered domain consisting of physical network infrastructure, logical software architectures, and cognitive human interaction, making it inherently dynamic and constantly evolving.")

    add_q(1, "Controllability Definition",
          "Under the five-pillar information security framework, what does 'Controllability' refer to?",
          ["Ensuring the network bandwidth is throttled to 56 kbps at all times",
           "Controlling information dissemination and maintaining administrative authority over information systems",
           "Preventing any user from ever accessing external web servers",
           "Eliminating all logging and auditing mechanisms on border firewalls"],
          "B",
          "Controllability ensures that security administrators can monitor, audit, and regulate the lifecycle, flow, content, and system access of information assets, preventing unauthorized operations and policy violations.")

    add_q(1, "Ransomware Threat Mechanism",
          "What is the primary economic extortion technique utilized by modern ransomware families?",
          ["Flooding target routers with ICMP echo requests until bandwidth saturation occurs",
           "Silently modifying website HTML source code to display jokes without data loss",
           "Encrypting critical organizational files with strong ciphers and demanding cryptocurrency for the private key",
           "Stealing physical server chassis from locked enterprise datacenter racks"],
          "C",
          "Ransomware uses high-grade symmetric and asymmetric cryptographic algorithms (e.g., AES-256 + RSA-2048) to encrypt user data in place, coercing victims into paying ransoms to obtain the decryption key.")

    add_q(1, "Vulnerability vs Exploit",
          "What is the technical distinction between a 'Vulnerability' and an 'Exploit'?",
          ["A vulnerability is malicious software code, whereas an exploit is a security standard",
           "A vulnerability is a defect/weakness in software or hardware; an exploit is code or technique used to take advantage of it",
           "A vulnerability only affects physical cables, while an exploit only affects web browsers",
           "There is no distinction; both terms are exact synonyms in network engineering"],
          "B",
          "A vulnerability is a flaw, bug, or design weakness present in software, protocols, or firmware. An exploit is a crafted payload, tool, or sequence of commands specifically constructed to take advantage of that vulnerability.")

    add_q(1, "Residual Risk",
          "What is 'Residual Risk' in enterprise risk management?",
          ["The initial risk measured before any security countermeasures are considered",
           "The remaining risk that persists after appropriate security controls have been implemented",
           "The risk that only affects obsolete hardware discarded in storage rooms",
           "Risk that has been 100% eliminated through cyber insurance"],
          "B",
          "Residual risk is the remaining risk level after security controls, safeguards, and mitigation policies have been deployed. An organization must determine whether residual risk falls within its acceptable risk appetite.")

    add_q(1, "Security Awareness Training",
          "Why is regular security awareness training considered a critical component of enterprise security?",
          ["It completely replaces the need for technical controls like firewalls and IPS",
           "Human errors and social engineering remain major attack vectors; user awareness mitigates phishing and policy violations",
           "It guarantees that network equipment will never experience hardware power outages",
           "It allows regular employees to rewrite firewall kernel code without supervision"],
          "B",
          "Humans are frequently the weakest link in the security perimeter. Attackers leverage phishing and social engineering to bypass perimeter defenses; continuous training develops vigilance and adherence to security protocols.")

    add_q(1, "Asset Classification",
          "What is the first fundamental step in conducting an enterprise information security risk assessment?",
          ["Purchasing the most expensive firewall available on the market",
           "Identifying and classifying organizational information assets based on business value and sensitivity",
           "Disabling all incoming and outgoing Internet traffic across all branch offices",
           "Assigning equal public administrative access to all internal and external users"],
          "B",
          "Before risks can be assessed or mitigated, an organization must identify and catalog its critical assets (hardware, software, data, personnel) and categorize them according to confidentiality, integrity, and availability impact.")

    add_q(1, "National Cyberspace Sovereignty",
          "How does the concept of national cyberspace sovereignty apply to digital communications?",
          ["Nation-states have independent jurisdiction over network infrastructure, data, and cyber activities within their sovereign territory",
           "No government has the authority to regulate or protect domestic telecommunication systems",
           "All data packets traversing global fiber optics are owned exclusively by international software vendors",
           "Cyber activities are strictly exempt from domestic legal compliance"],
          "A",
          "Cyberspace sovereignty reflects a state's independent jurisdiction and authority over its sovereign territory's cyber infrastructure, facilities, data governance, and legal accountability in cyberspace.")

    add_q(1, "Risk Treatment Strategies",
          "An enterprise decides to purchase cyber insurance to compensate for potential financial losses from data breaches. Which risk treatment strategy is being applied?",
          ["Risk Avoidance", "Risk Mitigation", "Risk Transfer", "Risk Acceptance"],
          "C",
          "Risk Transfer involves shifting financial liability or risk consequences to an external third party, commonly accomplished through cyber insurance policies or contractual outsourcing.")

    add_q(1, "Risk Acceptance",
          "When an organization formally decides to take no further action regarding an identified low-impact vulnerability because the cost of fixing it exceeds potential loss, this strategy is called:",
          ["Risk Avoidance", "Risk Acceptance", "Risk Transfer", "Risk Exploitation"],
          "B",
          "Risk Acceptance occurs when management formally acknowledges an identified risk and decides not to deploy countermeasures because the risk falls within acceptable tolerance or mitigation costs exceed the value of the asset.")

    add_q(1, "Defense in Depth - Identity Tier",
          "In a multi-tier defense architecture, which security mechanism operates at the identity and access management layer?",
          ["Fiber optic intrusion detection sensor", "Multi-Factor Authentication (MFA) and Least Privilege RBAC", "BGP Route Reflector filtering", "Shielded twisted pair copper grounding"],
          "B",
          "Identity and Access Management (IAM) controls operate at the logical user tier, employing Multi-Factor Authentication (MFA), role-based access control (RBAC), and least privilege to enforce access boundaries.")

    add_q(1, "Information Security Management System (ISMS)",
          "What is the core purpose of establishing an ISMS according to ISO 27001?",
          ["To build a systematic, ongoing management framework that identifies, manages, and minimizes security risks to corporate data",
           "To replace all human employees with automated AI bots",
           "To mandate the exclusive use of proprietary networking hardware",
           "To produce marketing materials for social media advertising"],
          "A",
          "An ISMS is a systematic framework comprising policies, processes, procedures, organizational structures, and software/hardware controls designed to manage and protect an organization's sensitive information assets.")

    add_q(1, "TCSEC B1 Level",
          "What significant capability was introduced at the TCSEC Division B (specifically B1) level compared to Division C?",
          ["Elimination of all password authentication mechanisms",
           "Mandatory Access Control (MAC) based on security labels and sensitivity levels",
           "Unrestricted file sharing across all military networks without classification",
           "Use of wireless Ethernet transmission without authentication"],
          "B",
          "TCSEC Division B introduced Mandatory Access Control (MAC), where data objects and subjects carry formal security labels (e.g., Unclassified, Confidential, Secret, Top Secret), enforcing the Bell-LaPadula mathematical security model.")

    add_q(1, "Physical Security Importance",
          "Why does Classified Protection 2.0 list 'Physical and Environmental Security' as a mandatory technical domain?",
          ["Because physical access to server hardware bypasses logical controls, allowing direct storage extraction or hardware compromise",
           "Because physical cables are immune to eavesdropping and environmental fire hazards",
           "Because physical security replaces the necessity of IP routing protocols",
           "Because server racks cannot operate unless painted in certified colors"],
          "A",
          "Physical security is the bedrock of information assurance. If an adversary gains physical access to a server or network switch, logical controls (passwords, firewalls) can be circumvented via local console access, hardware implants, or direct drive extraction.")

    # =========================================================================
    # CHAPTER 2: Network Basics (Q37 - Q80) - 44 Questions
    # =========================================================================
    add_q(2, "OSI Model - Layer Count",
          "How many layers are defined in the Open Systems Interconnection (OSI) reference model?",
          ["4 layers", "5 layers", "7 layers", "8 layers"],
          "C",
          "The OSI reference model defines 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.")

    add_q(2, "OSI Model - Layer 3 PDU",
          "What is the Protocol Data Unit (PDU) called at Layer 3 (Network Layer) of the OSI model?",
          ["Bit", "Frame", "Packet", "Segment"],
          "C",
          "PDUs across OSI layers: Layer 1 (Physical) = Bit; Layer 2 (Data Link) = Frame; Layer 3 (Network) = Packet; Layer 4 (Transport) = Segment; Layers 5-7 = Data.")

    add_q(2, "OSI vs TCP/IP Model Mapping",
          "Which OSI layers are consolidated into the single Application layer of the 4-layer TCP/IP model?",
          ["Physical and Data Link layers", "Data Link and Network layers", "Session, Presentation, and Application layers", "Transport and Session layers"],
          "C",
          "The TCP/IP model consolidates the functions of OSI Layer 5 (Session), Layer 6 (Presentation), and Layer 7 (Application) into a single unified Application Layer.")

    add_q(2, "Ethernet Frame - Structure",
          "In a standard Ethernet II frame, what is the length in bytes of the Destination MAC address field?",
          ["4 bytes", "6 bytes", "8 bytes", "16 bytes"],
          "B",
          "Ethernet MAC addresses are 48 bits (6 bytes) long. An Ethernet II frame header contains a 6-byte Destination MAC followed by a 6-byte Source MAC and a 2-byte Type field.")

    add_q(2, "Ethernet Frame - EtherType for IPv4",
          "What is the hexadecimal EtherType value indicating that the payload of an Ethernet II frame is an IPv4 packet?",
          ["0x0806", "0x0800", "0x86DD", "0x8100"],
          "B",
          "EtherType values: 0x0800 indicates IPv4; 0x0806 indicates ARP; 0x86DD indicates IPv6; 0x8100 indicates an IEEE 802.1Q VLAN tagged frame.")

    add_q(2, "Ethernet Frame - EtherType for ARP",
          "Which EtherType value indicates an Address Resolution Protocol (ARP) frame?",
          ["0x0800", "0x0806", "0x86DD", "0x8847"],
          "B",
          "EtherType 0x0806 is dedicated to the Address Resolution Protocol (ARP).")

    add_q(2, "Ethernet MTU",
          "What is the standard default Maximum Transmission Unit (MTU) size for an Ethernet interface payload?",
          ["576 bytes", "1480 bytes", "1500 bytes", "9000 bytes"],
          "C",
          "The standard default MTU for Ethernet is 1500 bytes. This defines the maximum size of the Layer 3 packet (IP header + payload) that can be encapsulated into an Ethernet frame without fragmentation.")

    add_q(2, "IPv4 Header - Minimum Size",
          "What is the minimum length of an IPv4 packet header when no optional fields are included?",
          ["16 bytes", "20 bytes", "32 bytes", "40 bytes"],
          "B",
          "The standard base IPv4 header with no options contains 5 rows of 32 bits (4 bytes) each, resulting in a minimum length of 20 bytes.")

    add_q(2, "IPv4 Header - IHL Field",
          "In an IPv4 header, the Internet Header Length (IHL) field has a value of 5. How many total bytes does the IP header contain?",
          ["5 bytes", "10 bytes", "20 bytes", "25 bytes"],
          "C",
          "The IHL field specifies the IP header length in 32-bit (4-byte) words. Therefore, an IHL of 5 represents 5 * 4 = 20 bytes.")

    add_q(2, "IPv4 Header - TTL Field Purpose",
          "What is the primary function of the Time to Live (TTL) field in an IPv4 header?",
          ["To record the exact timestamp when the packet was created",
           "To prevent packets from circulating endlessly in routing loops",
           "To calculate the round-trip latency between source and destination hosts",
           "To negotiate the maximum TCP sliding window buffer size"],
          "B",
          "The TTL field is decremented by 1 at each router hop. When TTL reaches 0, the packet is discarded and an ICMP Time Exceeded (Type 11) message is generated, preventing persistent routing loops.")

    add_q(2, "IPv4 Header - Protocol Field Values",
          "In the IPv4 header, what protocol value in the 'Protocol' field designates TCP?",
          ["1", "6", "17", "47"],
          "B",
          "Common IP Protocol numbers: 1 = ICMP; 6 = TCP; 17 = UDP; 47 = GRE; 50 = ESP; 51 = AH; 89 = OSPF.")

    add_q(2, "IPv4 Header - Protocol Field for UDP",
          "Which value in the IPv4 Protocol field identifies the payload as a User Datagram Protocol (UDP) segment?",
          ["6", "17", "1", "88"],
          "B",
          "Protocol number 17 designates UDP, while 6 designates TCP and 1 designates ICMP.")

    add_q(2, "IPv4 Header - Fragmentation Flags",
          "Which flag in the IPv4 header instructs intermediate routers NOT to fragment the packet?",
          ["MF (More Fragments)", "DF (Don't Fragment)", "URG (Urgent)", "SYN (Synchronize)"],
          "B",
          "The DF (Don't Fragment) flag, when set to 1, instructs routers to drop the packet and send an ICMP Destination Unreachable (Fragmentation Needed, Type 3 Code 4) message if the packet exceeds the outgoing link's MTU.")

    add_q(2, "IPv4 Addressing - Private IP Ranges",
          "Which of the following IPv4 address blocks is designated as a private address space under RFC 1918?",
          ["100.64.0.0/10", "172.16.0.0/12", "192.0.2.0/24", "169.254.0.0/16"],
          "B",
          "RFC 1918 defines three private IPv4 address blocks: 10.0.0.0/8 (10.0.0.0 - 10.255.255.255), 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), and 192.168.0.0/16 (192.168.0.0 - 192.168.255.255).")

    add_q(2, "IPv4 Addressing - Class C Private Range",
          "What is the valid RFC 1918 private IPv4 range for Class C addresses?",
          ["10.0.0.0 - 10.255.255.255", "172.16.0.0 - 172.31.255.255", "192.168.0.0 - 192.168.255.255", "192.168.1.0 - 192.168.1.255"],
          "C",
          "The Class C private address space defined in RFC 1918 is 192.168.0.0/16, spanning from 192.168.0.0 to 192.168.255.255.")

    add_q(2, "IPv4 Addressing - Loopback Address",
          "Which IPv4 address block is reserved by IANA for host internal loopback testing?",
          ["0.0.0.0/8", "127.0.0.0/8", "169.254.0.0/16", "224.0.0.0/4"],
          "B",
          "The entire 127.0.0.0/8 block is reserved for loopback operations. Traffic sent to 127.0.0.1 (or any address in 127.0.0.0/8) is looped back internally within the host IP stack without reaching physical media.")

    add_q(2, "Subnetting - Usable Hosts in /27",
          "How many usable host IP addresses are available in an IPv4 subnet with a /27 prefix (subnet mask 255.255.255.224)?",
          ["14", "30", "32", "62"],
          "B",
          "A /27 subnet has 32 - 27 = 5 host bits. Total addresses = 2^5 = 32. Subtracting the network address and directed broadcast address yields 32 - 2 = 30 usable host IP addresses.")

    add_q(2, "Subnetting - Broadcast Address of 192.168.1.64/26",
          "What is the directed broadcast address for the subnet 192.168.1.64/26?",
          ["192.168.1.64", "192.168.1.127", "192.168.1.128", "192.168.1.255"],
          "B",
          "A /26 subnet has block size 256 - 192 = 64. Subnet range: 192.168.1.64 to 192.168.1.127. The first address (.64) is network ID, and the last (.127) is the directed broadcast address.")

    add_q(2, "ARP - Request Transmission Mode",
          "How is an initial ARP Request frame transmitted across a local broadcast domain to resolve a target IP address?",
          ["Unicast to the default gateway", "Broadcast (Destination MAC FF:FF:FF:FF:FF:FF)", "Multicast to 224.0.0.1", "Anycast across all router ports"],
          "B",
          "Because the sending host does not know the destination MAC address, it broadcasts the ARP Request with Destination MAC FF:FF:FF:FF:FF:FF so all hosts on the local link process it.")

    add_q(2, "ARP - Reply Transmission Mode",
          "How does the target host respond to an ARP Request?",
          ["It broadcasts the ARP Reply to all hosts", "It transmits a unicast ARP Reply directly to the requester's MAC address", "It transmits an ICMP Echo Reply", "It registers its MAC address with the DNS server"],
          "B",
          "The target host learned the requester's MAC and IP addresses from the ARP Request header. Thus, it responds with a unicast ARP Reply directly addressed to the requester.")

    add_q(2, "Gratuitous ARP - Function",
          "What is a primary purpose of transmitting a Gratuitous ARP packet?",
          ["To query the DNS root server for top-level domains",
           "To detect duplicate IP address conflicts and update neighbors' ARP mapping caches",
           "To authenticate the user credentials against a RADIUS server",
           "To establish an encrypted IPsec tunnel across the WAN"],
          "B",
          "A host broadcasts a Gratuitous ARP (where source IP and target IP are its own address) upon interface activation to check if another device is already using that IP address (conflict detection) and to update MAC-to-IP tables on switches and neighbors.")

    add_q(2, "Proxy ARP - Concept",
          "What is the function of Proxy ARP on a router or firewall interface?",
          ["To encrypt all ARP queries using AES-128",
           "To respond with its own MAC address to an ARP request on behalf of a target host located on another subnet",
           "To permanently block all ARP traffic entering the interface",
           "To translate IPv4 addresses to IPv6 addresses"],
          "B",
          "Proxy ARP allows a router or firewall to reply with its own MAC address to an ARP Request sent by a local host seeking a destination host on a different subnet/network, enabling communication without configuring default gateways on legacy hosts.")

    add_q(2, "ICMP - Protocol Layer",
          "At which OSI layer does the Internet Control Message Protocol (ICMP) logically operate, and how is it encapsulated?",
          ["Layer 2, encapsulated directly inside Ethernet frames",
           "Layer 3, encapsulated directly inside IPv4 packets (Protocol 1)",
           "Layer 4, encapsulated inside TCP segments",
           "Layer 7, encapsulated inside HTTP requests"],
          "B",
          "ICMP is an integral part of the Network Layer (Layer 3). Its messages are encapsulated directly within IP datagrams with the IP header Protocol field set to 1.")

    add_q(2, "ICMP - Ping Echo Request Type and Code",
          "What are the ICMP Type and Code values for an ICMP Echo Request (Ping request)?",
          ["Type 0, Code 0", "Type 8, Code 0", "Type 3, Code 1", "Type 11, Code 0"],
          "B",
          "An ICMP Echo Request utilizes Type 8, Code 0. The responding device replies with an ICMP Echo Reply using Type 0, Code 0.")

    add_q(2, "ICMP - Destination Unreachable Type",
          "Which ICMP Type indicates that a destination network, host, port, or protocol is unreachable?",
          ["Type 0", "Type 3", "Type 8", "Type 11"],
          "B",
          "ICMP Type 3 represents 'Destination Unreachable'. Specific codes include Code 0 (Network Unreachable), Code 1 (Host Unreachable), Code 3 (Port Unreachable), and Code 4 (Fragmentation Needed and DF set).")

    add_q(2, "ICMP - Traceroute Mechanism",
          "Which ICMP message is generated by intermediate routers when their TTL counter reaches zero, enabling the 'tracert' / 'traceroute' command?",
          ["Type 0 Echo Reply", "Type 3 Destination Unreachable", "Type 11 Time Exceeded", "Type 5 Redirect"],
          "C",
          "Traceroute transmits packets with incrementing TTL values starting at 1. When a router decrements TTL to 0, it drops the packet and sends an ICMP Type 11 (Time Exceeded) message back to the source, revealing that hop's IP address.")

    add_q(2, "TCP - Characteristics",
          "Which of the following is a key operational characteristic of Transmission Control Protocol (TCP)?",
          ["Connectionless, best-effort delivery without acknowledgments",
           "Connection-oriented, reliable byte-stream service with error recovery and flow control",
           "Stateless broadcast transmission across local networks",
           "Fixed 8-byte header size with no options"],
          "B",
          "TCP (RFC 793) is a connection-oriented, reliable transport protocol that provides sequencing, acknowledgments, sliding-window flow control, congestion avoidance, and retransmission of lost segments.")

    add_q(2, "TCP 3-Way Handshake - Sequence",
          "What is the correct sequence of TCP flag exchanges during connection establishment?",
          ["ACK -> SYN -> FIN", "SYN -> SYN-ACK -> ACK", "SYN -> ACK-FIN -> RST", "RST -> SYN -> ACK"],
          "B",
          "The TCP 3-way handshake begins with the client sending a SYN segment, the server responding with SYN-ACK, and the client confirming with an ACK segment, transitioning the connection to the ESTABLISHED state.")

    add_q(2, "TCP 4-Way Handshake - Termination",
          "How many segments are typically exchanged to gracefully close a bidirectional TCP connection?",
          ["2 segments", "3 segments", "4 segments (FIN -> ACK -> FIN -> ACK)", "6 segments"],
          "C",
          "Because TCP is full-duplex, each direction of data transfer closes independently. Host A sends FIN, Host B sends ACK (closing A->B); then Host B sends FIN, and Host A sends ACK (closing B->A), totaling 4 segments.")

    add_q(2, "TCP - TIME_WAIT State Purpose",
          "What is the primary reason the TCP active close endpoint remains in the TIME_WAIT state for 2 MSL (Maximum Segment Lifetime)?",
          ["To immediately renegotiate encryption keys for the next connection",
           "To ensure the final ACK is received by the peer and allow old duplicate segments to expire in the network",
           "To allow the server to recharge its hardware interface buffers",
           "To force the client to restart its operating system"],
          "B",
          "The 2 MSL TIME_WAIT state ensures that if the final ACK is lost, the retransmitted FIN can be acknowledged. It also guarantees that all delayed segments from the closed connection expire and cannot corrupt future connections using the same socket pair.")

    add_q(2, "TCP Flags - RST Meaning",
          "What is the function of the RST (Reset) flag in a TCP header?",
          ["To request dynamic routing table updates from adjacent firewalls",
           "To abort an abnormal connection immediately and reject invalid connection attempts",
           "To initiate the graceful 3-way handshake",
           "To indicate that urgent out-of-band data is present"],
          "B",
          "The RST flag resets an invalid connection, aborts an active session due to errors, or rejects an incoming SYN directed to an inactive/closed port.")

    add_q(2, "UDP - Header Length",
          "What is the fixed header size of a standard User Datagram Protocol (UDP) segment?",
          ["8 bytes", "16 bytes", "20 bytes", "32 bytes"],
          "A",
          "A UDP header contains exactly four 16-bit fields: Source Port (2 bytes), Destination Port (2 bytes), Length (2 bytes), and Checksum (2 bytes), totaling 8 bytes.")

    add_q(2, "UDP - Suitable Applications",
          "Why is UDP preferred over TCP for real-time voice and video streaming (e.g., VoIP, video conferencing)?",
          ["UDP provides stronger encryption algorithms than TCP",
           "UDP has low latency and no retransmission delays, prioritizing timely delivery over perfect reliability",
           "UDP guarantees 100% loss-free packet delivery across congested links",
           "UDP automatically modifies router forwarding tables to prevent jitter"],
          "B",
          "Real-time media applications prioritize low latency and predictable jitter. Retransmitting dropped audio/video frames via TCP causes noticeable lag and freezes; dropping occasional packets is preferable.")

    add_q(2, "DNS - Default Port and Transport",
          "Which transport protocol and port number are predominantly used by standard DNS client queries?",
          ["TCP port 25", "UDP port 53", "TCP port 80", "UDP port 67"],
          "B",
          "Standard DNS queries and responses utilize UDP port 53 for speed. DNS uses TCP port 53 for responses exceeding 512 bytes (or EDNS0 limits) and for zone transfers between DNS servers.")

    add_q(2, "DNS - Record Types",
          "Which DNS resource record type maps a fully qualified domain name (FQDN) to an IPv4 address?",
          ["AAAA record", "A record", "CNAME record", "PTR record"],
          "B",
          "An 'A' record maps a hostname to an IPv4 address. 'AAAA' maps to IPv6; 'CNAME' maps an alias to a canonical name; 'PTR' provides reverse resolution from IP to domain name.")

    add_q(2, "HTTP vs HTTPS - Port Numbers",
          "What are the default standard TCP ports for unencrypted HTTP and encrypted HTTPS, respectively?",
          ["HTTP: 21, HTTPS: 22", "HTTP: 80, HTTPS: 443", "HTTP: 8080, HTTPS: 8443", "HTTP: 25, HTTPS: 587"],
          "B",
          "Standard HTTP communicates over cleartext TCP port 80, whereas HTTPS encrypts HTTP traffic inside TLS/SSL over TCP port 443.")

    add_q(2, "FTP - Control vs Data Ports",
          "In traditional Active Mode File Transfer Protocol (FTP), which port is used for control commands and which for data transfer?",
          ["Port 21 for Control; Port 20 for Data", "Port 22 for Control; Port 21 for Data", "Port 80 for Control; Port 443 for Data", "Port 69 for Control; Port 68 for Data"],
          "A",
          "FTP separates control commands from data transfer. Port 21 is the command/control port, while the FTP server initiates data connections from port 20 in Active FTP mode.")

    add_q(2, "FTP Active Mode - NAT Challenge",
          "Why does Active FTP fail when the FTP client is located behind a standard NAT router/firewall?",
          ["The client refuses to communicate with servers running Linux",
           "The FTP server initiates an inbound connection from port 20 to the client's high port, which the client firewall blocks",
           "Active FTP requires uncompressed video streaming bandwidth",
           "NAT devices are physically prohibited from handling TCP port 21"],
          "B",
          "In Active FTP, the client sends a PORT command specifying its internal IP and high port, then listens. The server initiates an incoming connection from port 20 to that port. A stateful firewall or NAT device at the client border blocks this unsolicited incoming connection unless an FTP ALG/ASPF is active.")

    add_q(2, "FTP Passive Mode - Mechanism",
          "How does Passive FTP (PASV) resolve client-side firewall and NAT traversal issues?",
          ["The server initiates the data connection directly to port 80",
           "The server opens a random high port and the client initiates the outbound data connection to that port",
           "Passive FTP disables encryption and authentication entirely",
           "The client and server communicate exclusively over ICMP echo packets"],
          "B",
          "In Passive FTP, the client sends the PASV command. The server opens a random unprivileged high port and returns the IP and port to the client. The client then initiates the outbound data connection, which client firewalls permit as outbound traffic.")

    add_q(2, "Telnet vs SSH - Security Difference",
          "Why is SSH (TCP port 22) universally recommended over Telnet (TCP port 23) for device management?",
          ["Telnet is restricted to connecting only to printers",
           "Telnet transmits usernames, passwords, and commands in cleartext, vulnerable to packet sniffing; SSH encrypts all session data",
           "Telnet requires hardware dongles for terminal emulation",
           "SSH uses connectionless UDP broadcast frames to reach remote routers"],
          "B",
          "Telnet transmits all data, including administrative credentials, in unencrypted plaintext across the network. Anyone intercepting traffic with a packet sniffer can read passwords. SSH encrypts the entire channel and authenticates server and client.")

    add_q(2, "DHCP - DORA Process",
          "What is the correct sequence of the four DHCP broadcast/unicast messages exchanged during dynamic host IP address allocation?",
          ["Discover -> Offer -> Request -> Acknowledge (DORA)",
           "Request -> Offer -> Discover -> Acknowledge",
           "Dial -> Open -> Ready -> Accept",
           "Detect -> Order -> Receive -> Authenticate"],
          "A",
          "The four-step DHCP process is DORA: 1. DHCP Discover (client broadcasts looking for a server); 2. DHCP Offer (server proposes IP configuration); 3. DHCP Request (client formally requests the offered IP); 4. DHCP ACK (server confirms lease).")

    add_q(2, "DHCP - UDP Ports",
          "Which UDP ports are utilized by DHCP servers and DHCP clients, respectively?",
          ["Server: UDP 67, Client: UDP 68", "Server: UDP 68, Client: UDP 67", "Server: UDP 53, Client: UDP 53", "Server: UDP 161, Client: UDP 162"],
          "A",
          "DHCP server listens on UDP port 67, and DHCP client listens on UDP port 68.")

    add_q(2, "DHCP Relay Agent",
          "When DHCP clients and the DHCP server reside in different IP subnets, which device feature must be configured on the local router/switch interface?",
          ["DNS Dynamic Update", "DHCP Relay Agent", "ARP Proxy", "NAT ALG"],
          "B",
          "Because initial DHCP Discover messages are Layer 2 broadcasts (255.255.255.255), routers drop them by default. A DHCP Relay agent intercepts these broadcasts and forwards them as unicast packets across routers to the centralized DHCP server.")

    add_q(2, "VLAN - IEEE 802.1Q Tag Size",
          "What is the size in bytes of the IEEE 802.1Q VLAN tag inserted into an Ethernet frame?",
          ["2 bytes", "4 bytes", "6 bytes", "8 bytes"],
          "B",
          "An 802.1Q tag is 4 bytes (32 bits) long, comprising a 2-byte Tag Protocol Identifier (TPID = 0x8100) and a 2-byte Tag Control Information (TCI, which contains 3-bit Priority, 1-bit CFI/DEI, and 12-bit VLAN ID).")

    return questions
