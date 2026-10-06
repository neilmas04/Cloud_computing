#!/usr/bin/env bash
# Experiment 2 - Memory benchmark: VM vs Docker container (10 repetitions each)
# Run from the project root (~/vm-vs-container-performance).
set -e
RUNS=10
mkdir -p results/raw/memory/vm results/raw/memory/container

for i in $(seq 1 $RUNS); do
  sysbench memory --memory-block-size=1M --memory-total-size=10G --threads=4 run \
    > results/raw/memory/vm/run_$i.txt
done

for i in $(seq 1 $RUNS); do
  docker run --rm vm-container-benchmark \
    sysbench memory --memory-block-size=1M --memory-total-size=10G --threads=4 run \
    > results/raw/memory/container/run_$i.txt
done
echo "Done. Raw outputs in results/raw/memory/{vm,container}"
