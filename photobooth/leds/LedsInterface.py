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


class LedsInterface:

    def __init__(self):

        self._led_count = 0
        self._left_btn = -1
        self._right_btn = -1

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.cleanup()

    def cleanup(self):

        pass

    def startup(self):

        pass

    @property
    def numberOfLeds(self):

        return self._led_count

    @numberOfLeds.setter
    def numberOfLeds(self, value):

        if not isinstance(value, int):
            raise ValueError('Expected int')

        self._led_count = value

    @property
    def leftButton(self):

        return self._left_btn

    @leftButton.setter
    def leftButton(self, value):

        if not isinstance(value, int):
            raise ValueError('Expected int')

        self._left_btn = value

    @property
    def rightButton(self):

        return self._right_btn

    @leftButton.setter
    def rightButton(self, value):

        if not isinstance(value, int):
            raise ValueError('Expected int')

        self._right_btn = value

    def loadCustomConfig(self, config):

        pass

    def loadConfig(self, config):
        
        self._led_count =  config.getInt('Leds', 'led_count')
        self._left_btn = config.getInt('Leds', 'left_index')
        self._right_btn = config.getInt('Leds', 'right_index')
        self.loadCustomConfig(config)

    def setLeds(self, leds):

        raise NotImplementedError()

    def setLeftButtonLed(self, rgb):

        raise NotImplementedError()

    def setRightButtonLed(self, rgb):

        raise NotImplementedError()

    def teardown(self):

        pass

