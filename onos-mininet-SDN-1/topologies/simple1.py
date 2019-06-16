#!/bin/python


'''

'''

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class MinimalTopo( Topo ):
    " a single switch and three hosts"

    def build( self ):
        # Create hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )

        # Create switches
        s1 = self.addSwitch( 's1' )

        # Add links between switches and each host
        self.addLink( s1, h1 )
        self.addLink( s1, h2 )
        self.addLink( s1, h3 )

def runMinimalTopo():

        topo = MinimalTopo()

        net = Mininet(
            topo=topo,
            controller=lambda name: RemoteController( name, ip='172.17.0.2' ),
            switch=OVSSwitch,
            autoSetMacs=True )

        net.start()
        CLI( net )
        # After the user exits the CLI, shutdown the network.
        net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    runMinimalTopo()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'minimal': MinimalTopo
}

# sudo mn --custom /vagrant/topologies/simple1.py --topo minimal --controller remote,ip=172.17.0.2
# sudo python /vagrant/topologies/simple1.py
# sudo mn -c
