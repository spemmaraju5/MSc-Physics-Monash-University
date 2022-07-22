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
IOHelper().inputFiles(
    ['00070793_00000001_7.AllStreams.dst'], clear=True)
