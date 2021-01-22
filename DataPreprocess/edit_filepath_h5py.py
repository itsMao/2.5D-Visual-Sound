#!/usr/bin/env python
import h5py
import numpy as np
import os
if __name__ == '__main__':
    with h5py.File('E://mono2binaural_data/splits/split1/train.h5', "r+") as f:
        for key in f.keys():
            print(f[key], key, f[key].name)
        for i in range(len(f["audio"][:])):
            suffix = os.path.split(f["audio"][i])[-1]
            f["audio"][i] = os.path.join(b'E://mono2binaural_data/audios/binaural_audios/', suffix)
        print(f["audio"][:])

    with h5py.File('E://mono2binaural_data/splits/split1/test.h5', "r+") as f:
        for key in f.keys():
            print(f[key], key, f[key].name)
        for i in range(len(f["audio"][:])):
            suffix = os.path.split(f["audio"][i])[-1]
            f["audio"][i] = os.path.join(b'E://mono2binaural_data/audios/binaural_audios/', suffix)
        print(f["audio"][:])

    with h5py.File('E://mono2binaural_data/splits/split1/val.h5', "r+") as f:
        for key in f.keys():
            print(f[key], key, f[key].name)
        for i in range(len(f["audio"][:])):
            suffix = os.path.split(f["audio"][i])[-1]
            f["audio"][i] = os.path.join(b'E://mono2binaural_data/audios/binaural_audios/', suffix)
        print(f["audio"][:])