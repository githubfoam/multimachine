#!/bin/python3


'''

'''

from mininet.topo import Topo

class MyTopo( Topo ):
    """Simple Topology """
    def __init__(self):
        """Create custom simple topology."""
        # Initialize topology
        Topo.__init__(self)

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )


        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add host to switch links
        self.addLink(h1,s1)
        self.addLink(h2,s3)

        # Add switch to switch links
        self.addLink(s1,s2)
        self.addLink(s2,s3)

topos = {"simple":( lambda : MyTopo() )}
# sudo mn --custom /vagrant/topologies/simple.py --topo simple --controller remote,ip=172.17.0.2
