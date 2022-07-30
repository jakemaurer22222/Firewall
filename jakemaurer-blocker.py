from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr

rules = [['00:00:00:00:00:01','00:00:00:00:00:03']]

class Firewall (EventMixin):
    
    def __init__ (self):
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp (self, event):
        for rule in rules:
            wall = of.ofp_match()
            wall.dl_src = EthAddr(rule[0])
            wall.dl_dst = EthAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = wall
            event.connection.send(flow_mod)
        
def launch ():
    core.registerNew(Firewall)