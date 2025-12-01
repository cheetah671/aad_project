# Testing and Visualization Pipeline

## Quick Reference

### 1. Run Algorithms on Dataset

Run each algorithm separately on all 82 test files:

```bash
# Run p1 (Tarjan's Algorithm)
python3 run_p1_only.py

# Run p2 (Tarjan-Vishkin Parallel Algorithm)
python3 run_p2_only.py

# Run p4 (Naive Algorithm)
python3 run_p4_only.py

# Run p5 (Chain Decomposition Algorithm)
python3 run_p5_only.py
```

**Output:**
- Algorithm results: `outputs/p1/`, `outputs/p2/`, `outputs/p4/`, `outputs/p5/`
- CSV files: `outputs/p1_results.csv`, `outputs/p2_results.csv`, etc.

---

### 2. Generate Graph Visualizations

Generate network topology visualizations (showing articulation points and bridges):

```bash
# Generate visualizations for ALL graphs (run once)
python3 scripts/visualize_all.py
```

**Output:** `graphs/<category>/<graph_name>_visualization.png`
- Red nodes = Articulation points
- Red edges = Bridges
- Blue nodes = Regular vertices

**Note:** This only needs to be run once, as the visualizations are based on graph structure (not algorithm output).

---

### 3. Generate Performance Graphs

Generate performance analysis graphs (time vs size, time vs type):

```bash
# For a specific algorithm
python3 scripts/create_performance_graphs.py p1
python3 scripts/create_performance_graphs.py p2
python3 scripts/create_performance_graphs.py p4
python3 scripts/create_performance_graphs.py p5

# OR generate for all algorithms at once
python3 scripts/create_all_performance_graphs.py
```

**Output:** `graphs/<algo>_time_vs_size.png` and `graphs/<algo>_time_vs_type.png`

---

## Complete Workflow Example

### Step 1: Test p1
```bash
python3 run_p1_only.py
```

### Step 2: Generate p1 performance graphs
```bash
python3 scripts/create_performance_graphs.py p1
```

### Step 3: Generate graph visualizations (once)
```bash
python3 scripts/visualize_all.py
```

### Step 4: Test remaining algorithms
```bash
python3 run_p2_only.py
python3 run_p4_only.py
python3 run_p5_only.py
```

### Step 5: Generate all performance graphs
```bash
python3 scripts/create_all_performance_graphs.py
```

---

## Directory Structure After Running

```
AAD_CP/
├── outputs/
│   ├── p1/
│   │   ├── dense/dense_01.txt
│   │   ├── sparse/sparse_01.txt
│   │   └── ...
│   ├── p2/, p4/, p5/ (similar structure)
│   ├── p1_results.csv
│   ├── p2_results.csv
│   ├── p4_results.csv
│   └── p5_results.csv
│
└── graphs/
    ├── dense/dense_01_visualization.png
    ├── sparse/sparse_01_visualization.png
    ├── p1_time_vs_size.png
    ├── p1_time_vs_type.png
    ├── p2_time_vs_size.png
    ├── p2_time_vs_type.png
    ├── p4_time_vs_size.png
    ├── p4_time_vs_type.png
    ├── p5_time_vs_size.png
    └── p5_time_vs_type.png
```

---

## Individual Scripts Description

| Script | Purpose | Output |
|--------|---------|--------|
| `run_p1_only.py` | Run p1 on all datasets | `outputs/p1/` + `p1_results.csv` |
| `run_p2_only.py` | Run p2 on all datasets | `outputs/p2/` + `p2_results.csv` |
| `run_p4_only.py` | Run p4 on all datasets | `outputs/p4/` + `p4_results.csv` |
| `run_p5_only.py` | Run p5 on all datasets | `outputs/p5/` + `p5_results.csv` |
| `scripts/visualize_all.py` | Generate graph topology visualizations | `graphs/<category>/*.png` |
| `scripts/visualize_graph.py` | Visualize single graph | Custom output location |
| `scripts/create_performance_graphs.py` | Generate performance graphs for one algorithm | `graphs/<algo>_time_vs_*.png` |
| `scripts/create_all_performance_graphs.py` | Generate performance graphs for all algorithms | `graphs/*_time_vs_*.png` |

---

## Notes

- **Visualizations run once**: Graph structure visualizations (`visualize_all.py`) only need to run once since they're based on the graph structure, not algorithm output.

- **Performance graphs per algorithm**: Performance graphs must be generated after running each algorithm's test script.

- **Large graphs**: Graphs with >1000 vertices show degree distribution instead of full network diagram.

- **p3 excluded**: p3.cpp is not yet implemented, so it's excluded from all scripts.
