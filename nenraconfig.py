# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.01.2014
# Copyright:   (c) NAMIK ERDOĞAN  2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import ConfigParser
import os


def _GetConfig():
    _config = ConfigParser.ConfigParser()
    _config.read(os.path.expanduser('./images/a.nenra'))
    return _config

def _GetOption( option):
    try:
        return _GetConfig().get('Nenra', option)
    except:
        return None
