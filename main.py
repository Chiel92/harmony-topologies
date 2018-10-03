'''
Model assumptions:
1. We work in 12-tone equal temperament.
2. Tones are equivalent modulo octaves.
'''

f = open('out.dot', 'w')
def say(msg):
    print(msg, file=f)

tones = [
    'C',
    'C#',
    'D',
    'D#',
    'E',
    'F',
    'F#',
    'G',
    'G#',
    'A',
    'A#',
    'B'
]

def print_leittones():
    for i,tone in enumerate(tones):
        say('  "{}" -> "{}";'.format(tone, tones[i-1]))

def print_quints():
    for i,tone in enumerate(tones):
        say('  "{}" -> "{}";'.format(tone, tones[i-5]))


def run():
    say('digraph harmony {')
    print_leittones()
    print_quints()
    say('}')

run()
