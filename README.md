# Music Repetition Matrices
These script create something I call "reptition matrices" for both lyrics and MIDI files. It was inspired by [this TEDx talk](https://youtu.be/_tjFwcmHy5M) by Colin Morris.

The basic idea is that we take the lyrics or notes of a song and map them along both the X and the Y axis. Then we go ahead and fill in every cell of the matrix whenever the words or notes along both axes are equal (similar to how DNA sequences are visualized). This exposes reptition on all scales in a visual form.  
My hope is that this kind of "repetition-fingerprinting" can be used for AI-based music and lyric generation in the future and I plan to conduct some expriments in this direction as well.

The generated output for lyrics looks something like this ("One" by Metallica):
![Sample Lyric Matrix](https://github.com/timwedde/lyric_repetition_matrix/blob/master/output_lyrics.png "Sample Lyric Matrix")

The generated output for MIDI files looks something like this (A small but polyphonic single-track melody file):
![Sample Note Matrix](https://github.com/timwedde/lyric_repetition_matrix/blob/master/output_midi.png "Sample Note Matrix")

## Installation
This script requires several depencdencies, so it's best to use it in a virtual Python environment:
```bash
$ git clone https://github.com/timwedde/music_repetition_matrix.git
$ cd music_repetition_matrix/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
```
usage: create_lyric_matrix.py [-h] -a string -t string [-m]

optional arguments:
  -h, --help            show this help message and exit
  -a string, --artist string
                        (required) The artist to search for
  -t string, --track string
                        (required) The song title to search for
  -m, --mask            If given, masks out the top half of the rendered
                        output
```
