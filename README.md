# Lyric Repetition Matrix
This script creates something I call "reptition matrices". It was inspired by [this TEDx talk](https://youtu.be/_tjFwcmHy5M) by Colin Morris.

The basic idea is that we take the lyrics of a song and map them along both the X and the Y axis. Then we go ahead and fill in every cell of the matrix whenever the words along both axes are equal (similar to how DNA sequences are visualized). This exposes reptition on all scales in a visual form.  
My hope is that this kind of "repetition-fingerprinting" can be used for AI-based music and lyric generation in the future and I plan to conduct some expriments in this direction as well.

The generated output looks something like this ("One" by Metallica):
![Sample Output](https://github.com/timwedde/lyric_repetition_matrix/blob/master/output.png "Sample Output")

## Installation
This script requires several depencdencies, so it's best to use it in a virtual Python environment:
```bash
$ git clone https://github.com/timwedde/lyric_repetition_matrix.git
$ cd lyric_repetition_matrix/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
```
usage: create_matrix.py [-h] -a string -t string [-m]

optional arguments:
  -h, --help            show this help message and exit
  -a string, --artist string
                        (required) The artist to search for
  -t string, --track string
                        (required) The song title to search for
  -m, --mask            If given, masks out the top half of the rendered
                        output
```
