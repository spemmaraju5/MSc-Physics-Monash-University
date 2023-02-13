from Configurables import DaVinci
from GaudiConf import IOHelper

#Load algorithms
from Configurables import CombineParticles
from Configurables import DaVinci
from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *

#Load input particles
from StandardParticles imp

import GaudiConfUtils.ConfigurableGenerators as ConfigurableGenerators
from PhysConf.Selections import SimpleSelection


line = 'Beauty2XGammaExclusiveBd2KstGammaLine'
strip_sel = StrippingSelection("Strip_sel", "HLT_PASS(StrippingBeauty2XGammaExclusiveBd2KstGammaLineDecision)")
strip_input = AutomaticData('Phys/{0}/Particles'.format(line))
tuple_sel = TupleSelection('Tuple_sel', 
                           [strip_sel, strip_input],
                           Decay='B0 -> (K*(892)0~ -> K+ pi-) gamma]CC')
