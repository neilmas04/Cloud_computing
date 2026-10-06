"""Parse Sysbench memory outputs and print mean/stddev for VM vs container.

Run from the experiment folder:  python3 scripts/parse_sysbench.py
Expects results/raw/memory/{vm,container}/run_*.txt (created by benchmark.sh).
"""
import glob
import re
import statistics as st

PATTERNS = {
    "MiB/sec": r"\(([\d.]+) MiB/sec\)",
    "total_time_s": r"total time:\s+([\d.]+)s",
    "avg_latency_ms": r"avg:\s+([\d.]+)",
    "max_latency_ms": r"max:\s+([\d.]+)",
}


def parse(path):
    text = open(path).read()
    return {k: float(re.search(p, text).group(1)) for k, p in PATTERNS.items()}


def summarize(env):
    runs = [parse(f) for f in sorted(glob.glob(f"results/raw/memory/{env}/run*.txt"))]
    if not runs:
        print(f"{env}: no runs found")
        return None
    print(f"\n{env.upper()} ({len(runs)} runs)")
    out = {}
    for k in PATTERNS:
        vals = [r[k] for r in runs]
        sd = st.stdev(vals) if len(vals) > 1 else 0.0
        out[k] = st.mean(vals)
        print(f"  {k:16s} mean={out[k]:.4f}  stddev={sd:.4f}")
    return out


vm, ct = summarize("vm"), summarize("container")
if vm and ct:
    d = (ct["MiB/sec"] - vm["MiB/sec"]) / vm["MiB/sec"] * 100
    print(f"\nContainer vs VM throughput: {d:+.2f}%")
