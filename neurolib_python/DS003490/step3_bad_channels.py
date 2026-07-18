import mne

# -----------------------------
# Load Filtered EEG
# -----------------------------
raw = mne.io.read_raw_fif("filtered_raw.fif", preload=True)

print("Original Channels:", len(raw.ch_names))

# -----------------------------
# Remove Non-EEG Channels
# -----------------------------
drop_list = ["VEOG", "X", "Y", "Z"]

existing = [ch for ch in drop_list if ch in raw.ch_names]

raw.drop_channels(existing)

print("Remaining Channels:", len(raw.ch_names))

# -----------------------------
# Check Channel Types
# -----------------------------
print(raw.get_channel_types())

# -----------------------------
# Plot EEG
# -----------------------------
raw.plot(duration=10,
         n_channels=20,
         title="Filtered EEG",
         block=True)

# -----------------------------
# Save
# -----------------------------
raw.save("prepared_raw.fif", overwrite=True)

print("\nPrepared EEG saved as prepared_raw.fif")