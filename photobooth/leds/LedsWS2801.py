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
import Adafruit_WS2801

from .LedsInterface import LedsInterface

class LedsWS2801(LedsInterface):

    def __init__(self):

        super().__init__()
        self._spi_clk = -1
        self._spi_data = -1

        logging.info('Using WS2801 leds')

    def loadCustomConfig(self, config):

        self._spi_clk = config.getInt('Leds', 'spi_clk')
        self._spi_data = config.getInt('Leds', 'spi_data')
        logging.info('LedsWS2801 : Will use CLK:%s DATA:%d', self._spi_clk,
                    self._spi_data)

    def startup(self):

        logging.info('LedsWS2801 : Startup')
        self._pixels = Adafruit_WS2801.WS2801Pixels(self.numberOfLeds, 
                            self._spi_clk, self._spi_data)
        self._pixels.clear()
        self._pixels.show()

    def setLeds(self, leds):

        for i in range(self.numberOfLeds):
            self._pixels.set_pixel_rgb(i, leds[i][0], leds[i][1], leds[i][2])
        self._pixels.show()

    def setLeftButtonLed(self, rgb):

        if (self.leftButton > -1):
            self._pixels.set_pixel_rgb(self.leftButton, rgb[0], rgb[1], rgb[2])

    def setRightButtonLed(self, rgb):

        if (self.rightButton > -1):
            self._pixels.set_pixel(self.rightButton, rgb[0], rgb[1], rgb[2])

