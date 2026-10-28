import math
import random

import matplotlib.pyplot as plt

# read the sequence
with open("sequence.fasta") as f:
    lines = f.read().splitlines()
sequence = "".join(line for line in lines if not line.startswith(">"))
print("Sequence length:", len(sequence))

# 10 random samples in an array

samples = []
for i in range(10):
    length = random.randint(100, 3000)
    start = random.randint(0, len(sequence) - length)
    samples.append(sequence[start:start + length])

for i, s in enumerate(samples, 1):
    print(f"Sample {i}: {len(s)} bp")


positions = []
for s in samples:
    positions.append(math.log10(len(s)))

# draw the gel
plt.figure(figsize=(12, 9))
plt.gca().set_facecolor("black")

for i in range(len(samples)):
    lane = i + 1
    plt.hlines(positions[i], lane - 0.3, lane + 0.3, colors="lime", linewidth=6)
    plt.text(lane + 0.32, positions[i], f"{len(samples[i])}", color="white", va="center", fontsize=9)

plt.xticks(range(1, 11), [f"S{i}" for i in range(1, 11)])
plt.ylabel("log10(length)  -  top: long, bottom: short")
plt.title("Simulated gel electrophoresis")
plt.savefig("gel.png")
plt.show()
