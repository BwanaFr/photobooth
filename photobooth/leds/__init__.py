#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Photobooth - a flexible photo booth software
# Copyright (C) 2018  Balthasar Reuter <photobooth at re - web dot eu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
from time import sleep

from .. import StateMachine
from ..Threading import Workers


class Leds:

    def __init__(self, config, comm):

        super().__init__()

        self._comm = comm
        self._leds = None

        self._is_trigger = False
        self._is_enabled = config.getBool('Leds', 'enable')

        self.initLeds(config)

    def initLeds(self, config):

        if self._is_enabled:
            self._leds = Entities()
         
            led_count =  config.getInt('Leds', 'led_count')
            spi_clk = config.getInt('Leds', 'spi_clk')
            spi_data = config.getInt('Leds', 'spi_data')
            button1_index = config.getInt('Leds', 'button1_index')
            button2_index = config.getInt('Leds', 'button2_index')

            logging.info(('LEDs enabled (led_count=%d, spi_clk=%d, '
                         'spi_data=%d, button1_index=%d, button2_index=%d)'),
                         led_count, spi_clk, spi_data, button1_index, button2_index)

        else:
            logging.info('LEDs disabled')

    def run(self):

        for state in self._comm.iter(Workers.LEDS):
            self.handleState(state)

        return True

    def handleState(self, state):

        if isinstance(state, StateMachine.IdleState):
            self.showIdle()
        elif isinstance(state, StateMachine.GreeterState):
            self.showGreeter()
        elif isinstance(state, StateMachine.CountdownState):
            self.showCountdown()
        elif isinstance(state, StateMachine.CaptureState):
            self.showCapture()
        elif isinstance(state, StateMachine.AssembleState):
            self.showAssemble()
        elif isinstance(state, StateMachine.ReviewState):
            self.showReview()
        elif isinstance(state, StateMachine.PostprocessState):
            self.showPostprocess()
        elif isinstance(state, StateMachine.TeardownState):
            self.teardown(state)

    def teardown(self, state):

        if self._is_enabled:
            self._leds.teardown()

    def showIdle(self):

         logging.info('LEDs showIdle')

    def showGreeter(self):

         logging.info('LEDs showGreeter')

    def showCountdown(self):

         logging.info('LEDs showCountdown')

    def showCapture(self):

         logging.info('LEDs showCountdown')

    def showAssemble(self):

         logging.info('LEDs showAssemble')

    def showReview(self):

         logging.info('LEDs showReview')

    def showPostprocess(self):

        pass


class Entities:

    def __init__(self):

        super().__init__()

#        import gpiozero
#        self.LED = gpiozero.LED

    def teardown(self):

         pass
