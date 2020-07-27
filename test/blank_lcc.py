#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/7/27 16:33
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import logging as lg

lg.basicConfig(
	format="%(levelname)s:%(message)s>>%(asctime)s>>%(funcName)s",
	datefmt="%d-%m-%Y %H:%M:%S", level=lg.DEBUG)

def main2():
	lg.debug("hellp")


main2()