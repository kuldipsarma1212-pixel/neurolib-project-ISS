import mne
import matplotlib.pyplot as plt

file_path = r"C:\Users\kuldip\Downloads\sub-001\sub-001_ses-01_task-Rest_eeg.set"

raw = mne.io.read_raw_eeglab(file_path, preload=True)

montage = mne.channels.make_standard_montage("standard_1020")
raw.set_montage(montage, on_missing="ignore")

print("Applying Band-pass Filter...")

raw.filter(1,40)

print("Applying Notch Filter...")

raw.notch_filter(freqs=50)

raw.plot(duration=10,n_channels=20,block=True)

raw.compute_psd().plot()

plt.show()

raw.save("filtered_raw.fif",overwrite=True)

print("Filtered EEG saved.")