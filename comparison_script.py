from music21.converter import parse
from pathlib import Path
from difflib import HtmlDiff
from score_dict import BPSVERSIONS

outputFolder = 'bpsdiff'

if __name__ == '__main__':
    Path(outputFolder).mkdir(parents=True, exist_ok=True)
    n = 1
    d = HtmlDiff()
    for annotation, scoreVersions in BPSVERSIONS.items():
        print(annotation)
        lines = {}
        for version, score in scoreVersions.items():
            if not score:
                continue
            s = parse(score)
            with open(f"{outputFolder}/{n}_{version}.txt", "w") as fd:
                for c in s.chordify().flat.notes:
                    attributes = (
                        c.offset,
                        c.measureNumber,
                        c.beat,
                        c.duration.quarterLength,
                        tuple([n.nameWithOctave for n in c])
                    )
                    line = "\t".join([str(a) for a in attributes])
                    fd.write(f"{line}\n")
        # Create the diff file
        classicman = open(f"{outputFolder}/{n}_classicman.txt").readlines()
        sapp = open(f"{outputFolder}/{n}_sapp.txt").readlines()
        diffHtml = d.make_file(classicman, sapp)
        with open(f"{outputFolder}/{n}_diff.html", "w") as fd:
            fd.write(diffHtml)
        n += 1
