from Gauss.Configuration import GenInit
from Gaudi.Configuration import *

GaussGen = GenInit("GaussGen")
GaussGen.FirstEventNumber = 1
GaussGen.RunNumber = 1082

from Configurables import LHCbApp
LHCbApp().DDDBtag = 'dddb-20170721-3'
LHCbApp().CondDBtag = 'sim-20190430-vc-md100'
LHCbApp().EvtMax = 50000