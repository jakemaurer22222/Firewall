from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def Topology():
    net = Mininet( controller=RemoteController )
    net.addController('control')
    
    h1 = net.addHost( 'h1', ip='127.0.0.1', mac='00:00:00:00:00:01' )
    h2 = net.addHost( 'h2', ip='127.0.0.2', mac='00:00:00:00:00:02' )
    h3 = net.addHost( 'h3', ip='127.0.0.3', mac='00:00:00:00:00:03' )
    h4 = net.addHost( 'h4', ip='127.0.0.4', mac='00:00:00:00:00:04' )

    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    
    info( '*** Creating links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s2 )
    net.addLink( h3, s3 )
    net.addLink( h4, s4 )
	
	net.addLink( s1, s2 )
    net.addLink( s1, s4 )
    net.addLink( s2, s3 )
    net.addLink( s3, s4 )
	
    net.start()
    CLI( net )
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    Topology()