from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
from Configurables import DaVinci
from PhysConf.Filters import LoKi_Filters
from GaudiConf import IOHelper
# Stream and stripping line we want to use
stream = 'AllStreams'
line = 'D2hhPromptDst2D2KKLine'

# Create an ntuple to capture D*+ decays from the
# StrippingLine line

dtt = DecayTreeTuple('TupleDstToD0pi_D0ToKK')
dtt.Inputs = ['/Event/{0}/Phys/{1}Particles'.format(stream, line)]
dtt.Decay = '[D*(2010)+ -> (D0 -> K- K+) pi+]CC'

# Configure DaVinci
DaVinci().UserAlgorithms += [dtt]
DaVinci().InputType = 'DST'
DaVinci().TupleFile = 'DVntuple.root'
DaVinci().PrintFreq = 1000
DaVinci().DataType = '2016'
DaVinci().Simulation = True

#Only ask for Luminosity information when not using simulated data
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().EvtMax = -1 #Run over all events
DaVinci().CondDBtag = 'sim-2017021-2-vc-md100'
DaVinci().DDDBtag = 'dddb-2017021-3'

# Requirement for events to pass a specific stripping line requirement
fltrs = LoKi_Filters(
    STRIP_Code = "HLT_PASS_RE('StrippingD2hhhPromptDst2D2KKLineDecision')"
)
DaVinci().EventPreFilters = fltrs.filters('Filters')

#Use the local input data (specify the data that is to be run over)
#IOHelper().inputFiles(
 #   ['./00070793_00000001_7.AllStreams.dst'], clear=True)


#TupleTools and Branches
##track_tool = dtt.addTupleTool('TupleToolTrackInfo')
##track_tool.Verbose = True
##tt.addTupleTool('TupleToolPrimaries')

#Storing specific information for each particle
dstar_hybrid = dtt.Dstar.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Dstar')
d0_hybrid = dtt.D0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_D0')
pisoft_hybrid = dtt.pisoft.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Pisoft')


#Preambulo property (preprocessing of the LoKi functors to simplify the code used to fill the leaves)
preamble = [
    'DZ = VFASPF(VZ) - BPV(VZ)',
    'TRACK_MAX_PT = MAXTREE(ISBASIC & HASTRACK, PT, -1)'
]
dstar_hybrid.Preambulo = preamble
d0_hybrid.Preambulo = preamble

#Variables property

dstar_hybrid.Variables = {
    'mass': 'M', 
    'mass_D0' : 'CHILD(M,1)', 
    'pt' : 'PT',
    'dz' : 'DZ', 
    'dira' : 'BPVDIRA', 
    'max_pt' : 'MAXTREE(ISBASIC & HASTRACK, PT, -1)', 
    'max_pt_preambulo' : 'TRACK_MAX_PT', 
    'sum_pt_pions' : 'SUMTREE(211 == ABSID, PT)',
    'n_highpt_tracks': 'NINTREE(ISBASIC & HASTRACK & (PT > 1500*MeV))'
}

d0_hybrid.Variables = {
    'mass' : 'M', 
    'pt' : 'PT', 
    'dira' : 'BPVDIRA', 
    'vtx_chi2': 'VFASPF(VCHI2)', 
    'dz' : 'DZ'
}

pisoft_hybrid.Variables = {
    'p' : 'P', 
    'pt' : 'PT'
}
#Using a TupleToolDecayTreeFilter
dtt.addBranches({
    'DStar': '[D*(2010)+ -> (D0 -> K- K+) pi+]CC'
})
dtt.Dstar.addTupleTool('TupleToolDecayTreeFitter/ConsD') #Arbitrary chosen name consD

dtt.Dstar.ConsD.constrainToOriginVertex = True
dtt.Dstar.ConsD.Verbose = True #Want all output available
dtt.Dstar.ConsD.daughtersToConstrain = ['D0'] #Apply mass constraint to the D0
dtt.Dstar.ConsD.UpdateDaughters = True # Store information on the daughter particles of the decay products 


