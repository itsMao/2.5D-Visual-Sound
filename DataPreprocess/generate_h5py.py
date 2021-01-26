#!/usr/bin/env python
import numpy as np
import random
import h5py
import os
if __name__ == '__main__':
    index_list = np.arange(1, 1001)
    random.shuffle(index_list)
    #print(index_list)
    i1 = index_list[0:600]
    i2 = index_list[600:800]
    i3 = index_list[800:1001]
    print(len(i1))
    print(len(i2))
    print(len(i3))
    basic_path = "E://mono2binaural_data/audios/binaural_audios/"
    with h5py.File('E://mono2binaural_data/splits/split0126/train.h5','w') as f:
        path_list = np.empty(len(i1), dtype = bytearray)
        #print(path_list)
        for i in range(len(i1)):
            p = os.path.join(basic_path, str(i1[i]).zfill(6) + '.wav')
            if(os.path.isabs(p)):
                bytes(p, encoding="utf8")
                path_list[i] = p
            else:
                print("不是绝对路径")
        f.create_dataset("audio", data = path_list)
        #print(f["audio"][1])
        for key in f.keys():
            print(f[key], key, f[key].name)
        f.close()

    with h5py.File('E://mono2binaural_data/splits/split0126/test.h5','w') as f:
        path_list = np.empty(len(i2), dtype = bytearray)
        #print(path_list)
        for i in range(len(i2)):
            p = os.path.join(basic_path, str(i2[i]).zfill(6) + '.wav')
            bytes(p, encoding="utf8")
            path_list[i] = p
        f.create_dataset("audio", data = path_list)
        print(f["audio"][1])
        for key in f.keys():
            print(f[key], key, f[key].name)
        f.close()

    with h5py.File('E://mono2binaural_data/splits/split0126/val.h5','w') as f:
        path_list = np.empty(len(i3), dtype = bytearray)
        #print(path_list)
        for i in range(len(i3)):
            p = os.path.join(basic_path, str(i3[i]).zfill(6) + '.wav')
            bytes(p, encoding="utf8")
            path_list[i] = p
        f.create_dataset("audio", data = path_list)
        print(f["audio"][1])
        for key in f.keys():
            print(f[key], key, f[key].name)
        f.close()


