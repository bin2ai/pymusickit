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
