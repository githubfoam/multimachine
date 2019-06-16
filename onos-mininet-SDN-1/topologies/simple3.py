#!/bin/python3


'''
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.util import irange
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

class LinearTopo( Topo ):
    " k switches, n hosts per switch."

    def build( self, k=2, n=1, **_opts):
        """k: number of switches
           n: number of hosts per switch"""
        self.k = k
        self.n = n

        if n == 1:
            genHostName = lambda i, j: 'h%s' % i
        else:
            genHostName = lambda i, j: 'h%ss%d' % ( j, i )

        lastSwitch = None
        for i in irange( 1, k ):
            # Add switch
            switch = self.addSwitch( 's%s' % i )
            # Add hosts to switch
            for j in irange( 1, n ):
                host = self.addHost( genHostName( i, j ) )
                self.addLink( host, switch )
            # Connect switch to previous
            if lastSwitch:
                self.addLink( switch, lastSwitch )
            lastSwitch = switch

def runMinimalTopo():

        topo = LinearTopo(4,2)

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
        setLogLevel('info')
        runMinimalTopo()
        topos = {
            'minimal': LinearTopo()
        }

# sudo python /vagrant/topologies/topolinear.py
# sudo mn -c
