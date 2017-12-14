# -*- coding: utf-8 -*-

######################################################################
## Classe MySystem - Define o sistema a ser simulado. Aqui vão ser
## instanciadas e conectadas a CPU e as caches.
######################################################################

import m5
from m5.objects import *

from MyO3CPU import *
from MyCaches import *


class MySystem(System):
       
    def __init__(self, options=None):
        super(MySystem, self).__init__()
        
######################################################################
## clk_domain - Define a frequencia de clock. Pode modificar a
## frequencia de clock. 
######################################################################
        self.clk_domain = SrcClockDomain()
        self.clk_domain.voltage_domain = VoltageDomain()
        self.clk_domain.clock = '2GHz'

######################################################################
## mem_mode e mem_ranges - Não modificar.
######################################################################
        self.mem_mode = 'timing'
        self.mem_ranges = [AddrRange('512MB')]
        
######################################################################
## A CPU - definida na classe MyO3CPU
######################################################################
        self.cpu = MyO3CPU(options)

######################################################################
## As caches - definidas em diversas classes.
######################################################################
        self.cpu.icache = L1ICache()
        self.cpu.dcache = L1DCache()
        self.cpu.l2cache = L2Cache()

######################################################################
## Define a interconexão entre as caches e memória
## principal. Modifique aqui se desejar alterar a hierarquia de
## memória.
######################################################################
        self.l2bus = SystemXBar()
        self.membus = SystemXBar()

        self.cpu.icache.connectCPU(self.cpu)
        self.cpu.icache.connectBus(self.l2bus)
        self.cpu.dcache.connectCPU(self.cpu)
        self.cpu.dcache.connectBus(self.l2bus)

        self.cpu.l2cache.connectCPUSideBus(self.l2bus)
        self.cpu.l2cache.connectMemSideBus(self.membus)

######################################################################
## Controlador de interrupções - conectado à memória principal
## Não modificar.
######################################################################
        self.cpu.createInterruptController()
        self.cpu.interrupts.pio = self.membus.master
        self.cpu.interrupts.int_master = self.membus.slave
        self.cpu.interrupts.int_slave = self.membus.master

######################################################################
## Não modificar.
######################################################################
        self.system_port = self.membus.slave

######################################################################
## Controlador de memória - conectado à memória principal
## Não modificar.
######################################################################
        self.mem_ctrl = DDR3_1600_x64()
        self.mem_ctrl.range = self.mem_ranges[0]
        self.mem_ctrl.port = self.membus.master
