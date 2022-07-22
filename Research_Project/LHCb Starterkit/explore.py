import sys
import GaudiPython as GP
from GaudiConf import IOHelper
from Configurables import DaVinci
from LoKiPhys.decorators import PX, PY, PZ, PT, M, E, P, GeV, VCHI2

dv = DaVinci()
dv.DataType = '2016'
dv.Simulation = True

# Retrieve file path to open as the last command line argument
Files = [sys.argv[-1]]
IOHelper('ROOT').inputFiles(Files)

appMgr = GP.AppMgr()
evt = appMgr.evtsvc()

appMgr.run(1)

def nodes(evt, root='/Event'):
    """List all nodes in `evt` starting from `node`."""
    node_list  = [root]
    for leaf in evt.leaves(evt[root]):
        node_list += nodes(evt, leaf.identifier())
        return node_list

def advance(decision):
    """Advance until stripping decision is true, returns
    number of events by which we advanced"""
    n = 0
    while evt['/Event']:
        reports = evt['/Event/Strip/Phys/DecReports']
        if reports.hasDecisionName('Stripping{}Decision'.format(decision)):
            break
        appMgr.run(1)
        n += 1
    return n
advance('D2hhPromptDst2D2KKLine')
candidates = evt['/Event/AllStreams/Phys/D2hhPromptDst2D2KKLine/Particles']
candidate = candidates[0]
#LoKi Functors
print(PX(candidate))
print(PY(candidate))
print(PZ(candidate))

#Print transverse momentum and mass functors
print(PT(candidate))
print(M(candidate))

#Print momentum magnitude using functors
mom_mag = (PX**2+PY**2+PZ**2)**0.5
print('Momentum magnitude is: {}'.format(mom_mag(candidate)))

invariant_mass = (E**2-P**2)**0.5
print('Invariant mass is: {}'.format(invariant_mass(candidate)))

#Get properties of D*+ vertex as well as its goodness of fit (chi**2)
print(VCHI2(candidate.endVertex()))

#Obtaining largest transverse momentum of decay products
def find_tracks(particle):
    tracks = []
    if particle.isBasicParticle():
        proto = particle.proto()
        if proto:
            track = proto.track()
            if track:
                try:
                    tracks.append(particle.data())
                except AttributeError:
                    tracks.append(particle)
    else:
        for child in particle.daughters():
            tracks += find_tracks(child)
    return tracks

max_pt = max([PT(child) for child in find_tracks(candidate)])