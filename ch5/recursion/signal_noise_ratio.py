# calculate the signal to noise ratio:

# SNRdb = 10 * log10(Psignal / Pnoise)

import math

signal_power = 9
noise_power = 10
ratio = signal_power / noise_power
decibals = 10 * math.log10(ratio)
print(decibals)