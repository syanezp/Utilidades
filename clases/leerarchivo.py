#!/usr/bin/python3
import os

def readfile(filename):
	with open(filename, 'r') as f:      # Ensure file is correctly closed under all circumstances
	    line = f.read()
	print(line)

filename = "texto.txt"
readfile(filename)