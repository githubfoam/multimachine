#!/bin/python


'''
https://gist.github.com/John-Lin/961156c1c6dcac545b41
'''
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class MyTopo(Topo):
    " two switches two hosts"
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('s3')
        rightSwitch = self.addSwitch('s4')

        # Add links
        self.addLink(leftHost, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightSwitch, rightHost)


def runMyTopo():

        topo = MyTopo()

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
    runMyTopo()

# Allows the file to be imported using `mn --custom <filename> --topo mytopo`
topos = {'mytopo': (lambda: MyTopo())}


# sudo mn --custom /vagrant/topologies/simple2.py --topo mytopo --controller remote,ip=172.17.0.2
# sudo python /vagrant/topologies/simple2.py
# sudo mn -c
