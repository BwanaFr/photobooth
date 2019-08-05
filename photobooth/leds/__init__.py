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
from colorsys import hsv_to_rgb
from time import sleep

from .. import StateMachine
from ..Threading import Workers

modules = (
   ('ws2801', 'LedsWS2801', 'LedsWS2801'),
   ('dummy', 'LedsDummy', 'LedsDummy'))

class Leds:

    def __init__(self, config, comm, LedsModule):

        super().__init__()

        self._comm = comm
        self._is_enabled = config.getBool('Leds', 'enable')

        if self._is_enabled:

            self._leds = LedsModule()
            self._leds.loadConfig(config)

            logging.info(('LEDs enabled (led_count=%d, left_index=%d, right_index=%d)'),
                          self._leds.numberOfLeds, self._leds.leftButton,
                          self._leds.rightButton)

        else:
            logging.info('LEDs disabled')

    def run(self):

        for state in self._comm.iter(Workers.LEDS):
            self.handleState(state)

        return True

    def handleState(self, state):
        if self._is_enabled:                
            if isinstance(state, StateMachine.StartupState):
                self._leds.startup()
            elif isinstance(state, StateMachine.IdleState):
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
        colors = [None] * self._leds.numberOfLeds
        inc = 1/self._leds.numberOfLeds
        for i in range(self._leds.numberOfLeds):
            colors[i] = hsv_to_rgb(i*inc, 1.0, 1.0)

        while self._comm.empty(Workers.LEDS):
            self._leds.setLeds(colors)
            c = colors[0]
            for i in (range(self._leds.numberOfLeds-1)):
                colors[i] = colors[i+1]
            colors[self._leds.numberOfLeds-1] = c
            sleep(0.1)

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

