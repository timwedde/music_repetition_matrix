"""
Idea: Create repetition matrix for notes, then play the analyzed file and highlight the X/Y of the current note.
"""

import os
import sys
import argparse
from signal import signal, SIGINT, SIG_IGN


def extract_notes(score):
    notes = []
    for a in score.recurse().notes:
        if a.isNote:
            x = a
            notes.append(str(x.pitch))
        if a.isChord:
            for x in a._notes:
                notes.append(str(x.pitch))

    return notes


def main(args):
    with tqdm(total=4) as bar:
        tqdm.write("Downloading Lyrics")
        song = m.converter.parse("melody.mid")

        words = extract_notes(song)
        tqdm.write("  Got {} notes".format(len(words)))
        words.insert(0, "")  # insert dummy value at 0, 0 so all actual words are part of the matrix
        bar.update(1)

        tqdm.write("Generating repetition matrix")
        matrix = [[0 for _ in range(len(words))] for _ in range(len(words))]

        matrix[0] = words
        for i in range(len(words)):
            matrix[i][0] = words[i]

        matrix = np.array(matrix)

        for y in range(1, matrix.shape[0]):
            for x in range(matrix.shape[1]):
                if matrix[y][0] == matrix[0][x]:
                    matrix[y][x] = 1

        matrix = np.delete(matrix, 0, 0)
        matrix = np.delete(matrix, 0, 1)

        df = pd.DataFrame(data=matrix, columns=words[1:])
        df.index = words[1:]
        df = df.astype("float64")
        bar.update(1)

        tqdm.write("Plotting")
        sns.set(style="white")

        mask = None
        if args.mask:
            mask = np.zeros_like(df, dtype=np.bool)
            mask[np.triu_indices_from(mask)] = True

        fig_size = len(words) // 5
        f, ax = plt.subplots(figsize=(fig_size, fig_size))
        tqdm.write("  Plot Size: {0}x{0}in".format(fig_size))

        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        hm = sns.heatmap(df, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=0,
                         xticklabels=True, yticklabels=True, cbar=False)
        bar.update(1)

        tqdm.write("Rendering plot")
        hm.get_figure().savefig("output.png", format="png", dpi=65, bbox_inches="tight")
        bar.update(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, dest="input_file", required=True,
                        metavar="file", help="(required) The MIDI file to analyze")
    parser.add_argument("-m", "--mask", action="store_true", dest="mask",
                        help="If given, masks out the top half of the rendered output")
    args = parser.parse_args()

    print("Importing libraries")
    ### Data Science ###
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    ### Music21 ###
    import music21 as m

    ### tqdm ###
    from tqdm import tqdm

    original_sigint_handler = signal(SIGINT, SIG_IGN)
    signal(SIGINT, original_sigint_handler)

    try:
        main(args)
    except KeyboardInterrupt:
        print("\nReceived SIGINT, terminating...")
