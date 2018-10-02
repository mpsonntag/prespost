import numpy as np
import matplotlib.pyplot as plt


def plot_traces(time, stim_times, stim_contrasts, ax, y_pos=12):
    stim_on = np.zeros(time.shape)
    for i,c in zip(stim_times, stim_contrasts):
        stim_on[(time >= i[0]) & (time < i[1])] = c/np.max(stim_contrasts)

    voltage = np.random.randn(len(time))
    voltage *= (stim_on + 1)
    spikes = time[voltage > 1.8]
    eod = np.sin(2*np.pi*0.5*time) * 0.25
    local_eod = np.sin(2 * np.pi*0.5*time+1.55) * 0.1
    stim = np.sin(2 * np.pi*0.5*time+1.55) * stim_on * 0.1

    ax.plot(time, voltage * 0.2 + y_pos, color="crimson", lw=0.3)
    ax.scatter(spikes, np.ones(spikes.shape) * y_pos-1, s=2, color='red')
    ax.plot(time, eod + y_pos-2, color="darkred", lw=0.3)
    ax.plot(time, local_eod * (stim_on + 1) + y_pos - 3,
            color="darkred", lw=0.3)
    ax.plot(time, stim + y_pos- 4, color="orange", lw=0.5)

    ax.text(-35, y_pos-0.25, "V-1", fontsize=8, color="crimson")
    ax.text(132, y_pos-0.25, "DataArray", fontsize=8, color="crimson")

    ax.text(-35, y_pos-1.25, "Spikes-1", fontsize=8, color="red")
    ax.text(132, y_pos-1.25, "DataArray", fontsize=8, color="red")

    ax.text(-35, y_pos-2.25, "EOD", fontsize=8, color="darkred")
    ax.text(132, y_pos-2.25, "DataArray", fontsize=8, color="darkred")

    ax.text(-35, y_pos-3.25, "LocalEOD-1", fontsize=8, color="darkred")
    ax.text(132, y_pos-3.25, "DataArray", fontsize=8, color="darkred")

    ax.text(-35, y_pos-4.25, "EFieldStim", fontsize=8, color="orange")
    ax.text(132, y_pos-4.25, "DataArray", fontsize=8, color="orange")


def plot_baseline(times, ax, y_pos=8):
    for i in times:
        ax.plot(list(i), [y_pos, y_pos], color="darkgreen", lw=2)
    ax.text(-35, y_pos-0.25, "baseline repro active", fontsize=8,
            color="darkgreen")
    ax.text(132, y_pos-0.25, "Tag", fontsize=8, color="darkgreen")


def plot_fi(repro_times, stimulus_times, contrasts, ax, y_pos=7):
    for i in repro_times:
        ax.plot(list(i), [y_pos, y_pos], color="blue", lw=2)
    ax.text(-35, y_pos -0.25, "fi-repro active", fontsize=8, color="blue")
    ax.text(132, y_pos -0.25, "Tag", fontsize=8, color="blue")

    for i, c in zip(stimulus_times, contrasts):
        ax.plot(list(i), [y_pos-1, y_pos-1], color="dodgerblue", lw=2)
        ax.plot([i[0] - 5., i[0]], [y_pos-1, y_pos-1], color="dodgerblue",
                lw=1., ls='--')
        ax.text(i[0] + (5 if c < 10 else 2.5), y_pos-2.25, str(c),
                color="cornflowerblue", fontsize=8)
    ax.text(-35, y_pos - 1.25, "fi-stimulus active", fontsize=8,
            color="dodgerblue")
    ax.text(132, y_pos - 1.25, "MultiTag", fontsize=8,
            color="dodgerblue")

    ax.text(-35, y_pos - 2.25, "fi-contrast", fontsize=8,
            color="cornflowerblue")
    ax.text(132, y_pos - 3., "Feature/\nDataArray", fontsize=8,
            color="cornflowerblue")


if __name__ == "__main__":
    fig = plt.figure()
    fig.set_size_inches(5.5, 2.5)
    ax = fig.add_subplot(111)

    time = np.arange(0.0, 130., 0.25)
    baseline_intervals = [(10., 28.), (105., 120.)]
    fi_intervals = [(36., 96.)]
    fi_stim_starts = np.arange(42.0, 90.0, 20.)
    fi_stim_ends = fi_stim_starts + 10.
    fi_stim_intervals = list(zip(fi_stim_starts, fi_stim_ends))
    fi_contrasts = np.arange(len(fi_stim_intervals)) * 5 + 5
    
    ax.set_ylim([0, 13])
    ax.set_yticks([])
    ax.set_xlim([0, 130])
    ax.set_xticks(np.arange(0., 130., 20.))
    ax.set_xlabel("real time after relacs start [s]")

    #plot_recording(recording_on, ax)
    plot_traces(time, fi_stim_intervals, fi_contrasts, ax, y_pos=12)
    plot_baseline(baseline_intervals, ax, 5)
    plot_fi(fi_intervals, fi_stim_intervals, fi_contrasts, ax, y_pos=4)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    fig.subplots_adjust(left=0.2, right=0.875, bottom=0.175, top=0.95)
    fig.savefig("../images/relacs_tagging.pdf")
