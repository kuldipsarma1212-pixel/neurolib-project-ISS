import matplotlib.pyplot as plt
import numpy as np
from neurolib.models.fhn import FHNModel

print("Libraries imported successfully!")

# ── PART 1: Single node ─────────────────────────────
print("\nRunning Part 1: Single isolated brain region...")

model = FHNModel()

# Simulate for 2 seconds = 2000 milliseconds
model.params['duration'] = 2 * 1000

# Add a small amount of noise (like real brain background activity)
model.params['sigma_ou'] = 0.1

# Run it
model.run()

print("Output variables available:", list(model.outputs.keys()))

# Plot the excitatory activity over time
plt.figure(figsize=(12, 4))
plt.plot(model.t, model.output.T)
plt.xlabel("Time [ms]")
plt.ylabel("Activity")
plt.title("PART 1: Single FHN Node - Brain Region Activity Over Time")
plt.show()

print("Part 1 done!")

# ── PART 2: Network of 4 nodes, weak coupling ───────
print("\nRunning Part 2: 4 connected brain regions, weak coupling...")

N = 4
cmat = np.ones((N, N))    # all regions connected to all others
dmat = np.zeros((N, N))   # no signal delay

network = FHNModel(Cmat=cmat, Dmat=dmat)
network.params['duration'] = 2 * 1000
network.params['sigma_ou'] = 0.1
network.params['K'] = 0.1   # WEAK coupling

network.run()

plt.figure(figsize=(12, 4))
plt.plot(network.t, network.output.T)
plt.xlabel("Time [ms]")
plt.ylabel("Activity")
plt.title("PART 2: 4 Brain Regions - Weak Coupling (K=0.1)")
plt.show()

print("Part 2 done!")

# ── PART 3: Same network, strong coupling ───────────
print("\nRunning Part 3: Same 4 regions, strong coupling...")

network.params['K'] = 2.0   # STRONG coupling
network.run()

plt.figure(figsize=(12, 4))
plt.plot(network.t, network.output.T)
plt.xlabel("Time [ms]")
plt.ylabel("Activity")
plt.title("PART 3: 4 Brain Regions - Strong Coupling (K=2.0)")
plt.show()

print("Part 3 done!")
print("\nAll experiments complete!")