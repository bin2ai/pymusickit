from typing import List


VALID_KEYS = set(['C', 'C#', 'D', 'D#', 'E', 'F',
                 'F#', 'G', 'G#', 'A', 'A#', 'B'])


def int_to_str(key: int) -> str:
    '''
    key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
    '''

    if key < 0 or key > 11:
        raise ValueError('Invalid key')

    return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'][key]


def str_to_int(key: str) -> int:
    '''
    key: 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    '''
    key = key.upper()
    key = flats_to_sharps(key)

    return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'].index(key)


def flats_to_sharps(key: str) -> str:
    '''
    input key: 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B, C#', 'D#', 'F#', 'G#', 'A#, E#, B#'
    resulting key: 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    this function will convert all possible key names to the standard form
    '''

    if not isinstance(key, str):
        raise TypeError('Invalid key type')

    key = key[0].upper() + key[1:].lower()

    VALID_INPUTS = set(['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'E#',
                       'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'B#', 'Cb'])

    if key not in VALID_INPUTS:
        raise ValueError('Invalid key')

    flat_to_sharp_dict = {'Db': 'C#', 'Eb': 'D#',
                          'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#', 'Cb': 'B', 'Fb': 'E'}

    if key in flat_to_sharp_dict:
        return flat_to_sharp_dict[key]
    else:
        return key


class Note:
    note_str: str = None
    note_int: int = None
    octave: int = None  # TODO: implement octave

    def __init__(self, note_str: str = None, note_int: int = None):
        '''
        note_str: 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
        #, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        note_int: 0 = C, 1 = C
        '''

        if note_str is not None:
            self.note_str = note_str
            self.note_int = str_to_int(note_str)
        elif note_int is not None:
            self.note_int = note_int
            self.note_str = int_to_str(note_int)
        else:
            raise ValueError('Must provide either note_str or note_int')

    def print_all(self, prefix: str = ''):
        print(prefix + "Note: " + self.note_str + ", " + str(self.note_int))


class Mode:

    mode_int: int = None
    mode_str: str = None

    def __init__(self, mode: int = None, mode_str: str = None):
        '''
        mode_int:  0 = Ionian, 1 = Dorian, 2 = Phrygian, 3 = Lydian, 4 = Mixolydian, 5 = Aeolian, 6 = Locrian
        mode_str: 'Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'
        '''
        if mode is not None:
            if mode < 0 or mode > 6:
                raise ValueError('Invalid mode')
            self.mode_int = mode
            self.mode_str = ['Ionian', 'Dorian', 'Phrygian',
                             'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'][mode]
        elif mode_str is not None:
            if mode_str not in ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']:
                raise ValueError('Invalid mode_str')
            self.mode_int = ['Ionian', 'Dorian', 'Phrygian', 'Lydian',
                             'Mixolydian', 'Aeolian', 'Locrian'].index(mode_str)
            self.mode_str = mode_str
        else:
            raise ValueError('Must provide either mode or mode_str')

    def print_all(self, prefix: str = ''):
        print(prefix + "Mode: " + self.mode_str + ", " + str(self.mode_int))


class MusicTheory:

    major_scale: List[Note] = None
    natural_minor_scale: List[Note] = None
    chromatic_scale: List[Note] = None
    pentatonic_scale: List[Note] = None
    mode: Mode = None
    modal_scale: List[Note] = None
    relative_minor: Note = None
    relative_major: Note = None
    key: Note = None

    def __init__(self, key_str: str = None, key_int: int = None, mode_int: int = None, mode_str: str = None):
        '''
        key_str: 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
        #, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        key_int: 0 = C, 1 = C
        mode:  0 = Ionian, 1 = Dorian, 2 = Phrygian, 3 = Lydian, 4 = Mixolydian, 5 = Aeolian, 6 = Locrian
        '''
        if key_str is not None and key_int is not None:
            raise ValueError('Cannot specify both key_str and key_int')
        elif key_str is None and key_int is None:
            raise ValueError('Must specify either key_str or key_int')
        elif key_str is not None:
            self.key = Note(note_str=key_str)
        elif key_int is not None:
            self.key = Note(note_int=key_int)
        else:
            raise ValueError('Invalid key')
        if mode_int is not None and mode_str is not None:
            raise ValueError('Cannot specify both mode_int and mode_str')
        elif mode_int is None and mode_str is None:
            raise ValueError('Must specify either mode_int or mode_str')
        elif mode_str is not None:
            self.mode = Mode(mode_str=mode_str)
        elif mode_int is not None:
            self.mode = Mode(mode=mode_int)
        else:
            raise ValueError('Invalid mode')

        self.major_scale = self.__major_scale()
        self.natural_minor_scale = self.__natural_minor_scale()
        self.chromatic_scale = self.__chromatic_scale()
        self.pentatonic_scale = self.__pentatonic_scale()
        self.modal_scale = self.__modal_scale()
        self.relative_minor = self.__relative_minor()
        self.relative_major = self.__relative_major()

    def __major_scale(self) -> List[Note]:
        '''
        key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        '''
        steps = [2, 2, 1, 2, 2, 2, 1]
        notes: List[Note] = [self.key]
        for i in range(len(steps)):
            note_int = (notes[i].note_int + steps[i]) % 12
            notes.append(Note(note_int=note_int))
        return notes

    def __natural_minor_scale(self) -> List[Note]:
        '''
        key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        '''
        steps = [2, 1, 2, 2, 1, 2, 2]
        notes: List[Note] = [self.key]
        for i in range(len(steps)):
            note_int = (notes[i].note_int + steps[i]) % 12
            notes.append(Note(note_int=note_int))
        return notes

    def __chromatic_scale(self) -> list:
        '''
        key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        '''
        notes: List[Note] = [self.key]
        for i in range(1, 12):
            note_int = (self.key.note_int + i) % 12
            notes.append(Note(note_int=note_int))
        return notes

    def __pentatonic_scale(self) -> list:
        '''
        key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        '''
        notes_int = [(self.key.note_int + i*7) % 12 for i in range(5)]
        notes: List[Note] = [Note(note_int=note_int) for note_int in notes_int]
        return notes

    def __modal_scale(self) -> list:
        '''
        key: 0 = C, 1 = C#, 2 = D, 3 = D#, 4 = E, 5 = F, 6 = F#, 7 = G, 8 = G#, 9 = A, 10 = A#, 11 = B
        mode: 0 = Ionian, 1 = Dorian, 2 = Phrygian, 3 = Lydian, 4 = Mixolydian, 5 = Aeolian, 6 = Locrian
        '''
        steps = [2, 2, 1, 2, 2, 1, 2]
        notes: List[Note] = [self.key]
        for i in range(len(steps)):
            note_int = (notes[i].note_int + steps[i]) % 12
            notes.append(Note(note_int=note_int))
        notes = notes[self.mode.mode_int:] + notes[:self.mode.mode_int]
        return notes

    def __relative_minor(self) -> Note:
        """
        Returns the relative minor key for a given major key.

        Parameters:
        key (str): The major key to find the relative minor for.

        Returns:
        str: The relative minor key.
        """

        # Create a dictionary mapping major keys to their relative minor keys
        # use sharps only
        relative_minor_dict = {'C': 'A', 'G': 'E', 'D': 'B', 'A': 'F#', 'E': 'C#', 'B': 'G#', 'F#': 'D#',
                               'F#': 'D#', 'C#': 'A#', 'G#': 'F', 'D#': 'C', 'A#': 'G', 'F': 'D'}

        # Look up the relative minor key and return it
        return Note(note_str=relative_minor_dict[self.key.note_str])

    def __relative_major(self) -> str:
        """
        Returns the relative major key for a given minor key.

        Parameters:
        key (str): The minor key to find the relative major for.

        Returns:
        str: The relative major key.
        """

        # Create a dictionary mapping minor keys to their relative major keys
        relative_major_dict = {'A': 'C', 'E': 'G', 'B': 'D', 'F#': 'A', 'C#': 'E', 'G#': 'B', 'D#': 'F#',
                               'F': 'G#', 'C': 'D#', 'G': 'A#', 'D': 'F', 'A#': 'C#', 'D#': 'F#'}

        # Look up the relative major key and return it
        return Note(note_str=relative_major_dict[self.key.note_str])

    def print_all(self):
        print('key:', self.key.note_str)
        attrs = vars(self)

        for attr, value in attrs.items():
            # if type Note, call Note.print()
            if isinstance(value, Note):
                print('-', attr, ':')
                value.print_all('--')
            # if type Mode, call Note.print()
            elif isinstance(value, Mode):
                print('-', attr, ':')
                value.print_all('--')
            # if type List[Note], call Note.print() for each Note in List
            elif isinstance(value, list):
                print('-', attr, ':')
                if isinstance(value[0], Note):
                    for note in value:
                        note: Note
                        note.print_all('--')
            # if type List[Mode], call Mode.print() for each Mode in List
                elif isinstance(value[0], Mode):
                    for mode in value:
                        mode: Mode
                        mode.print_all('--')
            else:
                print('-', attr, ':', value)


# example

if __name__ == '__main__':

    # create a music_theory object
    for key in ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']:
        for mode in ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']:
            print('key:', key, 'mode:', mode)
            mt = MusicTheory(key_str=key, mode_str=mode)

            # print all attributes
            mt.print_all()
