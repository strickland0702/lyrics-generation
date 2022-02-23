import pandas as pd
import numpy as np

train_data = pd.read_json("song-lyrics.train.jsonl", lines=True)
train_data.lyrics = train_data.lyrics.str.replace("\n", " michigan ")
train_data.lyrics = train_data.lyrics.apply(lambda x: x[:1024])
with open("train_lyrics_single_line.txt", "w+") as file_object:
    for lyrics in train_data.lyrics[:100000]:
        file_object.write(lyrics + "\n")