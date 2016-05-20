#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import platform

info_ico = """
		  GH0ST-S0FTWARE
# ------------------------------------------------#
# - Işletim Sistemi 	|         Çıktı          -#
# ------------------------------------------------#
# -  32 bit Linux 	| ('32bit', 'ELF')       -#
# -  64 bit Linux 	| ('64bit', 'ELF')       -#
# - 32 bit Windows 	| ('32bit', 'WindowsPE') -#
# - 64 bit Windows 	| ('64bit', 'WindowsPE') -#
# ------------------------------------------------#
"""
islemler_ico = """
(1) BUL
(2) ÇIKIŞ
"""

print info_ico

print islemler_ico

islem = input("Yapılcak işlem numarasını giriniz : ")

def system_name_and_bit_info():
	print "İşletim sisiteminiz : ", platform.architecture()

if islem == 1:
	system_name_and_bit_info()
	
elif islem == 2:
	sys.exit()
