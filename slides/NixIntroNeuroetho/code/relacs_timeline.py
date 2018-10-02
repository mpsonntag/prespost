import numpy as np
import matplotlib.pyplot as plt


def plot_recording(times, ax):
    for i in times:
        ax.plot(list(i), [9, 9], color="red", lw=2)
    ax.text(-35, 8.75, "acquisition active", fontsize=8, color="red")


def plot_baseline(times, ax):
    for i in times:
        ax.plot(list(i), [8, 8], color="darkgreen", lw=2)
    ax.text(-35, 7.75, "baseline repro active", fontsize=8, color="darkgreen")


def plot_fi(repro_times, stimulus_times, contrasts, ax):
    for i in repro_times:
        ax.plot(list(i), [7, 7], color="blue", lw=2)
    ax.text(-35, 6.75, "fi-repro active", fontsize=8, color="blue")

    for i, c in zip(stimulus_times, contrasts):
        ax.plot(list(i), [6, 6], color="dodgerblue", lw=2)
        ax.plot([i[0] - 5., i[0]], [6, 6], color="dodgerblue", lw=1., ls='--')
        ax.text(i[0] + (5 if c < 10 else 2.5), 4.75, str(c), color="cornflowerblue", fontsize=8)
    ax.text(-35, 5.75, "fi-stimulus active", fontsize=8, color="dodgerblue")
    ax.text(-35, 4.75, "fi-contrast", fontsize=8, color="cornflowerblue")


def plot_data_times(recording_times, data_times, data__times_labels, ax):
    ax.plot(list(recording_on[0]), [2., 2.], color="k", ls="--", lw=1.)
    ax.text(-35, 1.75, "data time", fontsize=8, color="k")
    for d, dl in zip(data_times, data_times_labels): 
        ax.plot([d, d], [10, 1.75], lw=0.5, color="k", ls="--")
        ax.text(d, 1.25, str(dl), fontsize=6, color="k", horizontalalignment="center")


if __name__ == "__main__":
    fig = plt.figure()
    fig.set_size_inches(5.5, 2.5)
    ax = fig.add_subplot(111)

    recording_on = [(7.5, 125.0)]
    baseline_intervals = [(10., 28.), (105., 120.)]
    fi_intervals = [(36., 96.)]
    fi_stim_starts = np.arange(42.0, 90.0, 20.)
    fi_stim_ends = fi_stim_starts + 10.
    fi_stim_intervals = list(zip(fi_stim_starts, fi_stim_ends))
    fi_contrasts = np.arange(len(fi_stim_intervals)) * 5 + 5
    data_times = []
    data_times.extend([i[0] for i in fi_intervals])
    data_times.extend([i[1] for i in fi_intervals])
    data_times.extend([i[0] for i in baseline_intervals])
    data_times.extend([i[1] for i in baseline_intervals])
    data_times.sort()
    data_times_labels = [0, 28, 28, 88, 88, 103]

    ax.set_ylim([0, 10])
    ax.set_yticks([])
    ax.set_xlim([0, 130])
    ax.set_xticks(np.arange(0., 130., 20.))
    ax.set_xlabel("real time after relacs start [s]")

    plot_recording(recording_on, ax)
    plot_baseline(baseline_intervals, ax)
    plot_fi(fi_intervals, fi_stim_intervals, fi_contrasts, ax)
    plot_data_times(recording_on, data_times, data_times_labels, ax)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    fig.subplots_adjust(left=0.225, right=0.99, bottom=0.175, top=0.95)
    fig.savefig("../images/relacs_timeline.pdf")
