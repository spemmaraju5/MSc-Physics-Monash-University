from StandardParticles import StdAllNoPIDsPions as Pions
from StandardParticles import StdAllLooseKaons as Kaons
from StandardParticles import StdAllLoosePhotons as Photons
from Configurables import CombineParticles
from PhysConf.Selections import Selection
import GaudiConfUtils.ConfigurableGenerators as ConfigurableGenerators
from PhysConf.Selections import SimpleSelection
from PhysConfSelections import CombineSelection
#Combine Kaon and Pion to form K*
kstar_decay_products = {
    'K+': (ACHILDCUT (PIDk > 5) & (PT > 500*MeV | PT > 500*MeV) & MIPCHI2DV(PRIMARY) > 25),
    'pi-': (ACHILDCUT(PIDpi < 0) & (PT > 1200*MeV | PT > 500*MeV) & MIPCHI2DV(PRIMARY) > 25)
}

kstar_comb = "(ADAMASS('K*0) < 50*MeV)"

kstar_vertex = (
    'VFASPF(VCHI2/VDOF)< 9' 
    '& (BPVDIRA > 0.9997)'
    "& (ADAMASS('K*0') < 50*MeV)"
)

kstar_sel = CombineSelection(
    'Sel_kstar',
    ConfigurableGenerators.CombineParticles,
    [Kaons, Pions],
    DecayDescriptor = '[K*0 -> K+ pi-]cc',
    DaughterCuts=kstar_decay_products,
    CombinationCut=kstar_comb,
    MotherCut=kstar_vertex
)