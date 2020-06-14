FULL_GET_CONFIG_ELEMENTS = ["cli-config-data-block"]

FULL_GET_CONFIG_RESULT = """<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101"><data><cli-config-data-block>!
TIMESTAMP
!
version 16.4
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
platform console serial
!
hostname csr1000v
!
boot-start-marker
boot-end-marker
!
!
enable secret 5 $1$cNYL$3oAI.iROunn/e7EidARR10
!
no aaa new-model
!
!
!
!
!
!
!
!
!
ip domain name example.com
!
!
!
!
!
!
!
!
!
!
subscriber templating
!
!
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
!
!
!
!
license udi pid CSR1000V sn 9FKLJWM5EB0
diagnostic bootup level minimal
archive
 path bootflash:
!
spanning-tree extend system-id
netconf-yang cisco-odm actions ACL
netconf-yang cisco-odm actions BGP
netconf-yang cisco-odm actions OSPF
netconf-yang cisco-odm actions Archive
netconf-yang cisco-odm actions IPRoute
netconf-yang cisco-odm actions EFPStats
netconf-yang cisco-odm actions IPSLAStats
netconf-yang cisco-odm actions Interfaces
netconf-yang cisco-odm actions Environment
netconf-yang cisco-odm actions FlowMonitor
netconf-yang cisco-odm actions MemoryStats
netconf-yang cisco-odm actions BFDNeighbors
netconf-yang cisco-odm actions BridgeDomain
netconf-yang cisco-odm actions CPUProcesses
netconf-yang cisco-odm actions LLDPNeighbors
netconf-yang cisco-odm actions VirtualService
netconf-yang cisco-odm actions MemoryProcesses
netconf-yang cisco-odm actions EthernetCFMStats
netconf-yang cisco-odm actions MPLSLDPNeighbors
netconf-yang cisco-odm actions PlatformSoftware
netconf-yang cisco-odm actions MPLSStaticBinding
netconf-yang cisco-odm actions MPLSForwardingTable
netconf-yang
!
restconf
!
username vrnetlab privilege 15 password 0 VR-netlab9
!
redundancy
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet1
 ip address 10.0.0.15 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet3
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet5
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet6
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet7
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet8
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet9
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet10
 no ip address
 shutdown
 negotiation auto
 no mop enabled
 no mop sysid
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
ip ssh pubkey-chain
  username vrnetlab
   key-hash ssh-rsa 5CC74A68B18B026A1709FB09D1F44E2F
ip scp server enable
!
!
!
!
!
!
control-plane
!
 !
 !
 !
 !
!
!
!
!
!
line con 0
 stopbits 1
line vty 0 4
 login local
 transport input all
line vty 5 15
 login local
 transport input all
!
netconf ssh
!
!
!
!
!
end</cli-config-data-block></data></rpc-reply>"""

CONFIG_FILTER_SINGLE = """
<config-format-text-cmd>
    <text-filter-spec>
        interface GigabitEthernet1
    </text-filter-spec>
</config-format-text-cmd> 
"""

CONFIG_FILTER_SINGLE_GET_CONFIG_ELEMENTS = ["cli-config-data"]

CONFIG_FILTER_SINGLE_GET_CONFIG_RESULT = """<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101"><data><cli-config-data><cmd>!</cmd>
<cmd>interface GigabitEthernet1</cmd>
<cmd> ip address 10.0.0.15 255.255.255.0</cmd>
<cmd> negotiation auto</cmd>
<cmd> no mop enabled</cmd>
<cmd> no mop sysid</cmd>
<cmd>end</cmd></cli-config-data></data></rpc-reply>"""
