# -*- coding: utf-8 -*-
######################################################################
######################################################################
##
## Arquivo de configuração da CPU
##
## Inicialmente, define uma série de classes que vão representar as
## unidades funcionais. Nessas classes, descreve-se o tipo de operação
## que aquela unidade funcional executa (opClass), a latência ou tempo
## que a operação leva para concluir (opLat), e a quantidade de
## unidades daquele tipo (count). Também é possível modelar se a
## unidade funcional opera em pipeline ou não (variável pipelined -
## que é True por padrão).
##
## A seguir, a classe MyO3CPU instancia o pool de unidades funcionais
## (MyFUPool), definidos antes, e define os demais parâmetros do
## processador. É possível mudar a largura dos estágios do pipeline
## (variáveis *Width), a latência de cada estágio (e.g.: variável
## fetchToDecodeDelay = 3 modela um pipeline com o Fetch dividido em 3
## estágios), a quantidade de posições nos buffers (*BufferSize,
## *QueueSize, *Entries).
##
## O fluxo de instruções entre os estágios do pipeline é:
##
## Fetch -> Decode -> Rename -> Dispatch,Issue,Execute,Writeback -> Commit.
##
## OBS: Os estágios Dispatch,Issue,Execute,Writeback são agrupados em um único
## estágio, chamado aqui de IEW.
##
######################################################################
######################################################################


from m5.objects import DerivO3CPU
from m5.objects import TournamentBP
from m5.objects import OpDesc
from m5.objects import FUDesc
from m5.objects import FUPool

from m5.defines import buildEnv

######################################################################
## Unidades funcionais
######################################################################

class MyIntALU(FUDesc):
    opList = [ OpDesc(opClass='IntAlu', opLat=1) ]
    count = 2

class MyIntMultDiv(FUDesc):

    opList = [ OpDesc(opClass='IntMult', opLat=3, pipelined=True),
               OpDesc(opClass='IntDiv', opLat=12, pipelined=False)]

    count = 1

class My_FP_ALU(FUDesc):
    opList = [ OpDesc(opClass='FloatAdd', opLat=5),
               OpDesc(opClass='FloatCmp', opLat=5),
               OpDesc(opClass='FloatCvt', opLat=5) ]
    count = 2

class My_FP_MultDiv(FUDesc):
    opList = [	OpDesc(opClass='FloatDiv', opLat=9, pipelined=False),
                OpDesc(opClass='FloatSqrt', opLat=33, pipelined=False),
                OpDesc(opClass='FloatMult', opLat=4) ]
    count = 2

class My_SIMD_Unit(FUDesc):
    opList = [ OpDesc(opClass='SimdAdd', opLat=4),
               OpDesc(opClass='SimdAddAcc', opLat=4),
               OpDesc(opClass='SimdAlu', opLat=4),
               OpDesc(opClass='SimdCmp', opLat=4),
               OpDesc(opClass='SimdCvt', opLat=3),
               OpDesc(opClass='SimdMisc', opLat=3),
               OpDesc(opClass='SimdMult',opLat=5),
               OpDesc(opClass='SimdMultAcc',opLat=5),
               OpDesc(opClass='SimdShift',opLat=3),
               OpDesc(opClass='SimdShiftAcc', opLat=3),
               OpDesc(opClass='SimdSqrt', opLat=9),
               OpDesc(opClass='SimdFloatAdd',opLat=5),
               OpDesc(opClass='SimdFloatAlu',opLat=5),
               OpDesc(opClass='SimdFloatCmp', opLat=3),
               OpDesc(opClass='SimdFloatCvt', opLat=3),
               OpDesc(opClass='SimdFloatDiv', opLat=3),
               OpDesc(opClass='SimdFloatMisc', opLat=3),
               OpDesc(opClass='SimdFloatMult', opLat=3),
               OpDesc(opClass='SimdFloatMultAcc',opLat=1),
			   OpDesc(opClass='SimdFloatSqrt', opLat=9) ]
    count = 2

class MyReadPort(FUDesc):
    opList = [ OpDesc(opClass='MemRead', opLat=2) ]
    count = 1

class MyWritePort(FUDesc):
    opList = [ OpDesc(opClass='MemWrite', opLat=2) ]
    count = 1

class MyIprPort(FUDesc):
    opList = [ OpDesc(opClass='IprAccess', opLat = 3, pipelined = True) ]
    count = 1

class MyFUPool(FUPool):
    FUList = [ MyIntALU(), MyIntMultDiv(), My_FP_ALU(), My_FP_MultDiv(), MyReadPort(),
               MyWritePort(), My_SIMD_Unit(), MyIprPort() ]


############################################################
## Processador
############################################################

class MyO3CPU(DerivO3CPU):
############################################################
## Latências (em ciclos) entre os diferentes estágios do pipeline.
## Pode ser usado para simular pipelines mais profundos.
############################################################
    fetchToDecodeDelay = 3 # Latência Fetch -> Decode
    decodeToRenameDelay = 2 # Latência Decode -> Rename
    renameToIEWDelay = 1 # Latência Rename -> IEW
    renameToROBDelay = 1 # Latência Rename -> ReorderBuffer
    issueToExecuteDelay = 1 # Latência do Issue -> Execute
    iewToCommitDelay = 1 # Latência IEW -> Commit

############################################################
## Tamanho das estruturas do pipeline. Afetam a quantidade
## de instruções que podem ser armazenadas nos buffers.
############################################################

    fetchBufferSize =	16 # Tamanho do buffer entre a cache e o estágio
                         # de Fetch (em Bytes)
    fetchQueueSize = 32 # Tamanho da fila de Fetch, em qtd. de
                        # micro-ops
    numIQEntries =	32 # Tamanho da fila de instruções, em qtd. de
                      # micro-ops
    numROBEntries = 40 #168 # Tamanho do reorder buffer, em qtd. de
                        # micro-ops
    LQEntries = 16 # Tamanho da fila de loads, em qtd. de micro-ops
    SQEntries = 16 # Tamanho da fila de stores, em qtd. de micro-ops

    numPhysIntRegs = 128 # Quantidade de registradores fisicos de
                         # inteiros
    numPhysFloatRegs = 192 # Quantidade de registradores físicos de
                           # FloatingPoint

############################################################
## Largura das estruturas do pipeline. Afetam a quantidade
## de instruções processadas por ciclo em cada estágio.
############################################################

    fetchWidth = 3 # Largura do Fetch
    decodeWidth = 3 # Largura do Decode
    renameWidth = 3 # Largura do Rename
    dispatchWidth = 6 # Largura do Dispatch
    issueWidth = 4 # Largura do Issue
    wbWidth = 4 # Largura do Writeback
    commitWidth = 4 # Largura do Commit
    squashWidth = 4 # Largura de squash (quantas instruções podem ser
                    # removidas do ROB no caso de misspeculation)
    
    fuPool = MyFUPool() # Pool de unidades funcionais





    
############################################################
## Outros parâmetros. Não modificar.
############################################################

    branchPred = TournamentBP() # Preditor de desvios

    numRobs = 1 # Number of Reorder Buffers;
    
    #### Latências de retorno dos sinais (sinais voltando para
    #### estágios anteriores do pipeline
    decodeToFetchDelay = 1 
    renameToFetchDelay = 1 
    renameToDecodeDelay = 1 
    iewToFetchDelay = 1
    iewToDecodeDelay = 1
    iewToRenameDelay = 1
    commitToFetchDelay = 1
    commitToDecodeDelay = 1
    commitToRenameDelay = 1
    commitToIEWDelay = 1
    
    LSQDepCheckShift = 4 # Number of places to shift addr before check
    LSQCheckLoads = True # Should dependency violations be checked for loads & stores or just stores
    store_set_clear_period = 250000 # Number of load/store insts before the dep predictor should be invalidated
    LFSTSize = 1024 # Last fetched store table size
    SSITSize = 1024 # Store set ID table size
                                  
    # most ISAs don't use condition-code regs # so default is 0
    _defaultNumPhysCCRegs = 0

    # For x86, each CC reg is used to hold only a subset of the flags, so we
    # need 4-5 times the number of CC regs as physical integer regs to be
    # sure we don't run out.  In typical real machines, CC regs are not
    # explicitly renamed (it's a side effect of int reg renaming),
    # so they should never be the bottleneck here.
    _defaultNumPhysCCRegs = numPhysIntRegs * 5
    numPhysCCRegs = _defaultNumPhysCCRegs # Number of physical cc registers
      
    activity = 0 # Initial count

    cachePorts = 3 # Cache Ports

    trapLatency = 13 # Trap latency
    fetchTrapLatency = 1 # Fetch trap latency

    backComSize = 10 # Time buffer size for backwards communication
    forwardComSize = 10 # Time buffer size for forward communication

    smtNumFetchingThreads = 1 # SMT Number of Fetching Threads
    smtFetchPolicy = 'SingleThread' # SMT Fetch policy
    smtLSQPolicy = 'Partitioned' # SMT LSQ Sharing Policy
    smtLSQThreshold = 100 # SMT LSQ Threshold Sharing Parameter
    smtIQPolicy = 'Partitioned' # SMT IQ Sharing Policy
    smtIQThreshold = 100 # SMT IQ Threshold Sharing Parameter
    smtROBPolicy = 'Partitioned' # SMT ROB Sharing Policy
    smtROBThreshold = 100 # SMT ROB Threshold Sharing Parameter
    smtCommitPolicy = 'RoundRobin' # SMT Commit Policy
    
    needsTSO = True # Enable TSO Memory model
    def __init__(self, options=None):
        super(MyO3CPU, self).__init__()
