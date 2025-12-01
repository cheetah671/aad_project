#!/usr/bin/env python3
"""Generate performance analysis graphs from results CSV"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPHS_DIR = ROOT / 'graphs'

def create_performance_graphs(algorithm='p1'):
    """Create time vs size and time vs type graphs."""
    
    RESULTS_CSV = ROOT / 'outputs' / f'{algorithm}_results.csv'
    
    if not RESULTS_CSV.exists():
        print(f"Error: {RESULTS_CSV} not found!")
        print(f"Please run run_{algorithm}_only.py first to generate results.")
        return False
    
    # Read results
    df = pd.read_csv(RESULTS_CSV)
    
    # Filter successful runs only
    df = df[df['exitcode'] == 0].copy()
    
    print(f"Loaded {len(df)} successful test results for {algorithm}")
    
    # Create graphs directory if not exists
    GRAPHS_DIR.mkdir(exist_ok=True)
    
    # ========== Graph 1: Time vs Graph Size ==========
    plt.figure(figsize=(10, 6))
    
    # Plot each category with different color/marker
    categories = df['category'].unique()
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    markers = ['o', 's', '^', 'D', 'v', 'p']
    
    for i, category in enumerate(sorted(categories)):
        cat_data = df[df['category'] == category]
        plt.scatter(cat_data['n'], cat_data['time'], 
                   label=category, 
                   color=colors[i % len(colors)],
                   marker=markers[i % len(markers)],
                   s=50, alpha=0.7)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of Vertices (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    plt.title(f'{algorithm.upper()} Algorithm: Time vs Graph Size', fontsize=14, fontweight='bold')
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    output_file = GRAPHS_DIR / f'{algorithm}_time_vs_size.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    plt.close()
    
    # ========== Graph 2: Time vs Graph Type ==========
    plt.figure(figsize=(10, 6))
    
    # Calculate statistics per category
    category_stats = df.groupby('category')['time'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index()
    category_stats = category_stats.sort_values('mean')
    
    # Create bar plot with error bars
    x_pos = range(len(category_stats))
    plt.bar(x_pos, category_stats['mean'], 
            yerr=category_stats['std'],
            color=colors[:len(category_stats)],
            alpha=0.7, capsize=5, edgecolor='black', linewidth=1.5)
    
    plt.xlabel('Graph Category', fontsize=12, fontweight='bold')
    plt.ylabel('Average Execution Time (seconds)', fontsize=12, fontweight='bold')
    plt.title(f'{algorithm.upper()} Algorithm: Average Time by Graph Type', fontsize=14, fontweight='bold')
    plt.xticks(x_pos, category_stats['category'], rotation=45, ha='right')
    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    output_file = GRAPHS_DIR / f'{algorithm}_time_vs_type.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    plt.close()
    
    # ========== Bonus: Summary Statistics Table ==========
    print("\n" + "="*70)
    print(f"SUMMARY STATISTICS BY CATEGORY - {algorithm.upper()}")
    print("="*70)
    print(f"{'Category':<20} {'Mean (s)':<12} {'Median (s)':<12} {'Std Dev':<12}")
    print("-"*70)
    for _, row in category_stats.iterrows():
        print(f"{row['category']:<20} {row['mean']:<12.6f} {row['median']:<12.6f} {row['std']:<12.6f}")
    print("="*70)
    
    print(f"\n✓ Performance graphs saved to: {GRAPHS_DIR}")
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        algorithm = sys.argv[1]
    else:
        algorithm = 'p1'
    
    create_performance_graphs(algorithm)
