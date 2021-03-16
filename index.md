## Digital Collections of Beethoven Piano Sonatas

This site is a dedicated resource presenting a note-by-note comparison between two digital transcriptions of the Beethoven Piano Sonatas:

- Craig Sapp's [Humdrum Transcriptions](http://kern.humdrum.org/search?s=t&keyword=Beethoven)
- ClassicMan's [MuseScore Transcriptions](https://musescore.com/user/19710/sets/54311)

Both of these resources can be accessed through the corresponding websites or by contacting the corresponding authors.

In this website, we show a comparison of the musical content between these two transcriptions, with the objective of improving the overall quality of both transcriptions.

The comparisons were made only at the pitch and duration levels; making sure that the position in the score of one note is the same in both versions. Other attributes (e.g., articulations, dynamics, page layout, etc.) were not compared and are left for future work.

The reason why we care about accurate pitch and duration values is because they have implications for musicians who learn from these scores (i.e., preferrably, they don't learn the wrong notes), and because most computational music theory models make use of pitch and duration information only. Thus, we consider it valuable to verify whether the notes between these two transcriptions coincide. Doing so, it should be easier to correct any wrong notes in either version.


---

# Methodology

The transcriptions have been encoded in different formats: Humdrum and MusicXML (encoded with MuseScore).

The first step to compare them is to convert them into a similar representation. One of the easiest accomplish this is by using the `music21` python library. This is what we used for the comparisons.

The parser for Humdrum data in `music21` is currently unable to handle some elements of the Humdrum syntax. We overcome this by doing slight changes to the Humdrum files. Particularly:

- `sonata06-1.krn`: Removing multiple spines of dynamics in `m25`.