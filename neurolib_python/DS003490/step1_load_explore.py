import mne
import matplotlib.pyplot as plt

# Read EEG
file_path = r"C:\Users\kuldip\Downloads\sub-001\sub-001_ses-01_task-Rest_eeg.set"

raw = mne.io.read_raw_eeglab(file_path, preload=True)

print(raw)

print("\n========== BASIC INFORMATION ==========")
print("Channels :", raw.info["nchan"])
print("Sampling Frequency :", raw.info["sfreq"])
print("Duration :", raw.times[-1])

print("\n========== CHANNEL NAMES ==========")
print(raw.ch_names)

print("\n========== SHAPE ==========")
print(raw.get_data().shape)

# Apply montage
montage = mne.channels.make_standard_montage("standard_1020")
raw.set_montage(montage, on_missing="ignore")

# Plot sensors
raw.plot_sensors(show_names=True)

# Raw EEG
raw.plot(duration=10, n_channels=20, block=True)

# PSD
raw.compute_psd().plot()

plt.show()