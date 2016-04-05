#!/usr/local/bin/python

"""
Spectrum analyser by Robert de Lisle

Uses libraries wave to read in sound, and matplotlib for displaying results
"""
import sys, wave

def main( wav_file ):
    w = wave.open(wav_file, 'r')


if __name__ == '__main__':
    ## Parse command-line args
    try:
        wav_file = sys.argv[1]
    except:
        raise ValueError("Audio filename expected but not found")
    main( wav_file )
