#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import RemoteController 

class CustomTopo( Topo ):
	def __init__(self):
		
		Topo.__init__( self )
		
		S1 = self.addSwitch('S1')
		S2 = self.addSwitch('S2')
		S3 = self.addSwitch('S3')
		S4 = self.addSwitch('S4')
		S5 = self.addSwitch('S5')

		H1 = self.addHost('H1')
		H2 = self.addHost('H2')
		
		L1 = self.addLink(H1,S1)
		L2 = self.addLink(S2,S1)
		L3 = self.addLink(S2,S3)
		L4 = self.addLink(S2,S4)
		L5 = self.addLink(S3,S4)
		L6 = self.addLink(S4,S5)
		L7 = self.addLink(S5,H2)
		
def main():
    setLogLevel( 'info' )
    topo = CustomTopo()
    
    net = Mininet(topo=topo, link=TCLink,controller=lambda name: RemoteController( name, ip='127.0.0.1' ))
    
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    main()
