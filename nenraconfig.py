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

import configparser
import os


def _GetConfig():
    _config = configparser.ConfigParser()
    _config.read(os.path.expanduser('./images/a.nenra'))
    return _config

def _GetOption( option):
    try:
        return _GetConfig().get('Nenra', option)
    except:
        return None

def _GetOption1( option):
    try:
        return _GetConfig().get('FBD', option)
    except:
        return None
def _GetOption2( option):
    try:
        return _GetConfig().get('tele', option)
    except:
        return None
def _GetOption3( option):
    try:
        return _GetConfig().get('Nenra1', option)
    except:
        return None
