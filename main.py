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

consonants = set()
consonants.add((0, 0))
progressions = set()
progressions.add((0, 0))


def add_consonants(tone_set):
    for _, tone in list(tone_set):
        consonants.add((tone, (tone - 4) % 12))
        consonants.add((tone, (tone - 5) % 12))
        consonants.add((tone, (tone - 7) % 12))


def add_progressions(tone_set):
    for _, tone in list(tone_set):
        progressions.add((tone, (tone - 1) % 12))
        progressions.add((tone, (tone - 5) % 12))


def reachable_by_progression():
    result = set()
    for t1, t2 in progressions:
        result.add(t1)
        result.add(t2)
    return result


def reachable_by_consonance():
    result = set()
    for t1, t2 in consonants:
        result.add(t1)
        result.add(t2)
    return result


def print_consonants():
    reachable = reachable_by_progression()
    for t1, t2 in consonants:
        if t1 != t2 and t1 in reachable and t2 in reachable:
            say('  "{}" -> "{}" [dir=none,color=red];'.format(tones[t1], tones[t2]))


def print_progressions():
    reachable = reachable_by_consonance()
    for t1, t2 in progressions:
        if t1 != t2 and t1 in reachable and t2 in reachable:
            say('  "{}" -> "{}";'.format(tones[t1], tones[t2]))


def run():
    add_progressions(progressions)
    add_consonants(consonants)
    add_progressions(consonants)
    add_consonants(progressions)

    say('digraph harmony {')
    print_consonants()
    print_progressions()
    say('}')


run()
