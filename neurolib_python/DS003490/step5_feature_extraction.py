import mne
import pandas as pd
import numpy as np

# -----------------------------
# Load EEG
# -----------------------------
raw = mne.io.read_raw_fif("ica_ready_raw.fif", preload=True)

print(raw)

# -----------------------------
# Compute PSD
# -----------------------------
psd = raw.compute_psd()

# Plot PSD
psd.plot()

# -----------------------------
# Get Data
# -----------------------------
power = psd.get_data()

freqs = psd.freqs

print("PSD Shape:", power.shape)

# -----------------------------
# Mean Power
# -----------------------------
mean_power = np.mean(power, axis=1)

# -----------------------------
# Save CSV
# -----------------------------
df = pd.DataFrame({
    "Channel": raw.ch_names,
    "Mean Power": mean_power
})

df.to_csv("band_power_features.csv", index=False)

print(df.head())

print("\nFeatures saved to band_power_features.csv")