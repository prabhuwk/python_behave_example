#!/usr/bin/env python
import os
import sys
import re

class Findapp:
	def __init__(self, directory, pattern):
		self.directory = directory
		self.pattern = pattern
	def find_impl(self):
		self.result = []
		expression = re.compile(self.pattern)
		for root, dirs, filename in os.walk(self.directory):
			for fname in filename:
				if expression.search(fname):
					filepath = os.path.join(root, fname)
					print filepath
					self.result.append(filepath)

if __name__ == '__main__':
	directory = sys.argv[1]
	pattern = sys.argv[3]
	j = Findapp(directory, pattern)
	j.find_impl()
