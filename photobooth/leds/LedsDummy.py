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

from .LedsInterface import LedsInterface

class LedsDummy(LedsInterface):

    def __init__(self):

        super().__init__()
        logging.info('Using dummy leds')

    def setLeds(self, leds):

        raise NotImplementedError()

    def setLeftButtonLed(self, rgb):

        raise NotImplementedError()

    def setRightButtonLed(self, rgb):

        raise NotImplementedError()

    def loadCustomConfig(self, config):

        logging.info('Loading custom config')

    def setLeds(self, leds):

        logging.info(f"Setting leds {str(leds)}")

    def setLeftButtonLed(self, rgb):

        if (self.leftButton > -1):
            logging.info('Setting left button %x', rgb)

    def setRightButtonLed(self, rgb):

        if (self.rightButton > -1):
            logging.info('Setting right button %x', rgb)
