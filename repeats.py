from itertools import product

# Read the sequence
with open("tp53.fasta") as f:
    lines = f.read().splitlines()
sequence = "".join(line for line in lines if not line.startswith(">"))
print("Sequence length:", len(sequence))

# Brute force:
results = []
for k in range(3, 7):
    for combo in product("ACGT", repeat=k):
        motif = "".join(combo)
        i = sequence.find(motif)
        while i != -1:
            
            copies = 1
            while sequence[i + copies * k:i + (copies + 1) * k] == motif:
                copies += 1

            if copies >= 2 and 6 <= copies * k <= 10:
                results.append((i, motif, copies))
            i = sequence.find(motif, i + copies * k)

results.sort()
for pos, motif, copies in results:
    print(f"pos {pos:>4}: {motif} x {copies} = {motif * copies} ({len(motif) * copies} letters)")
print("Total repetitions found:", len(results))
