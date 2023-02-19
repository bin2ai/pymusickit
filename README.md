# PyMusicKit
A python project that uses Librosa and other libraries to analyze the key that a song (an .mp3) is in, i.e. F major or C# minor, using the Krumhansl-Schmuckler key-finding algorithm.

** Forked from Jack Mcarthur's work 'https://github.com/jackmcarthur/musical-key-finder' **
This forked version allows the user to install the package using pip and use it as a library in their own projects.

## Installation

To install the package, run the following command in your terminal:

```bash
pip install pymusickit
```

## Usage

### Key Finder

```python
from pymusickit.key_finder import KeyFinder

audio_path = 'sweet-home-alabama.mp3'
song = KeyFinder(audio_path)

#optional parameters: t_start, t_end (in seconds)
# song = KeyFinder(audio_path, t_start=10, t_end=20)

#variety of print functions
song.print_key()
song.print_chroma()
song.print_correlation()
song.print_correlation_table()

#plotting functions
song.chromagram(title="Sweet Home Alabama")
```

the KeyFinder class has many attributes to programatically access the data

### Music Theory

```python
from pymusickit.music_theory import MusicTheory
mt = MusicTheory(key_str = 'C')

'''
class MusicTheory:
    ...
    major_scale: List[Note]
    natural_minor_scale: List[Note]
    chromatic_scale: List[Note]
    pentatonic_scale: List[Note]
    mode: Mode
    modal_scale: List[Note]
    relative_minor: Note
    relative_major: Note
    key: Note
    ...

class Mode:
    ...
    mode_int:  0 = Ionian, 1 = Dorian, 2 = Phrygian, 3 = Lydian, 4 = Mixolydian, 5 = Aeolian, 6 = Locrian
    mode_str: 'Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'
    ...

class Note:
    ...
    note_str: 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    note_int: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
    ...
'''
```

the MusicTheory class has many attributes to programatically access the data
