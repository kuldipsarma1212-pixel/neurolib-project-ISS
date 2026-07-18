import mne
from mne.preprocessing import ICA

# -----------------------------
# Load Prepared EEG
# -----------------------------
raw = mne.io.read_raw_fif("prepared_raw.fif", preload=True)

print(raw)

# -----------------------------
# Create ICA Model
# -----------------------------
ica = ICA(
    n_components=20,
    random_state=42,
    max_iter="auto"
)

print("Fitting ICA...")

ica.fit(raw)

print("ICA Finished.")

# -----------------------------
# Plot Components
# -----------------------------
ica.plot_components()

# -----------------------------
# Plot Sources
# -----------------------------
ica.plot_sources(raw)

# ===================================================
# DO NOT REMOVE COMPONENTS YET
# We will learn how to identify eye blink artifacts
# before excluding them.
# ===================================================

raw.save("ica_ready_raw.fif", overwrite=True)

print("ICA model completed.")