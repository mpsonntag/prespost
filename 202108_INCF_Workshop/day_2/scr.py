import os
import time
import numpy as np
import nixio as nix
import matplotlib.pyplot as plt

from tempfile import TemporaryDirectory
from typing import List, Tuple


def create_file(nixfile: nix.File) -> List[int]:
    times = []
    blk = nixfile.create_block("benchmark", "block")
    grp = blk.create_group("benchmark", "group")
    for idx in range(200):
        da = blk.create_data_array(name=str(idx), array_type="array", data=[0])
        t0 = time.time()
        grp.data_arrays.append(da)
        times.append(time.time() - t0)
    return times


def benchmark_retrieve_actual(nixfile: nix.File) -> Tuple[List[int], List[int], List[int]]:
    create_file(nixfile)
    by_name = []
    by_id = []
    by_idx = []
    blk = nixfile.blocks[0]
    for idx, da in enumerate(blk.data_arrays):
        t0 = time.time()
        blk.data_arrays[da.name]
        by_name.append(time.time() - t0)

        t0 = time.time()
        blk.data_arrays[da.id]
        by_id.append(time.time() - t0)

        t0 = time.time()
        blk.data_arrays[idx]
        by_idx.append(time.time() - t0)
    return by_name, by_id, by_idx


def benchmark_retrieve_link(nixfile: nix.File) -> Tuple[List[int], List[int], List[int]]:
    create_file(nixfile)
    by_name = []
    by_id = []
    by_idx = []
    blk = nixfile.blocks[0]
    grp = blk.groups[0]
    for idx, da in enumerate(grp.data_arrays):
        t0 = time.time()
        grp.data_arrays[da.name]
        by_name.append(time.time() - t0)

        t0 = time.time()
        grp.data_arrays[da.id]
        by_id.append(time.time() - t0)

        t0 = time.time()
        grp.data_arrays[idx]
        by_idx.append(time.time() - t0)
    return by_name, by_id, by_idx


def main():
    with TemporaryDirectory() as tmpdir:
        with nix.File(os.path.join(tmpdir, "retrieve"), nix.FileMode.Overwrite) as nixfile:
            by_name, by_id, by_idx = benchmark_retrieve_actual(nixfile)
            plt.figure("Retrieval times from block.data_arrays")
            plt.plot(by_name, ".", label="by name")
            plt.plot(by_id, ".", label="by ID")
            plt.plot(by_idx, ".", label="by index")
            plt.legend()
            plt.xlabel("Item index")
            plt.ylabel("Time (s)")

    with TemporaryDirectory() as tmpdir:
        with nix.File(os.path.join(tmpdir, "link-retrieve"), nix.FileMode.Overwrite) as nixfile:
            by_name, by_id, by_idx = benchmark_retrieve_link(nixfile)
            plt.figure("Retrieval times from group.data_arrays")
            plt.plot(by_name, ".", label="by name")
            plt.plot(by_id, ".", label="by ID")
            plt.plot(by_idx, ".", label="by index")
            plt.legend()
            plt.xlabel("Item index")
            plt.ylabel("Time (s)")
    plt.show()

if __name__ == "__main__":
    main()
