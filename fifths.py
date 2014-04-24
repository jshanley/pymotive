import math

steps = ['F','C','G','D','A','E','B']

symbols = { 'b': -7, '#': 7, 'x': 14 }

def fifths(noteName):
	#enforce uppercase
	step = noteName[0].upper()
	output = steps.index(step) - 1
	accidentals = noteName[1:]
	for symbol in accidentals:
		output += symbols[symbol]
	return output


def noteName(fifths):
	offset, idx = divmod(fifths + 1, len(steps))
	step = steps[idx]
	output = step
	# add on accidentals as needed
	while offset < 0:
		output += 'b'
		offset += 1
	while offset > 1:
		output += 'x'
		offset -= 2
	while offset > 0:
		output += '#'
		offset -= 1
	return output





