# NIDS Threshold Optimization: Simulated Annealing vs Genetic Algorithms

A research project comparing **Simulated Annealing (SA)** and **Genetic Algorithms (GA)** for optimizing decision thresholds in Network Intrusion Detection Systems (NIDS). The pipeline evaluates threshold tuning on a curated network traffic dataset using stratified cross-validation, macro-F1 fitness tracking, and convergence visualization.

---

## 📌 Project Overview
Modern NIDS pipelines convert classifier probabilities into binary labels using a fixed threshold (`θ = 0.5`). This work isolates **threshold optimization** as the sole search target to evaluate:
- How SA and GA navigate continuous decision boundaries
- The impact of cooling-rate schedules on SA convergence
- Operational trade-offs (recall vs precision) embedded in optimized cutoffs

Both algorithms converge near `θ ≈ 0.5` with nearly identical macro-F1 scores (~0.996), demonstrating diminishing returns for threshold tuning when baseline ensembles already achieve high feature separability. However, algorithm-specific trajectories reveal meaningful operational alignments: SA favors slightly lower thresholds (recall-oriented), while GA stabilizes at higher cutoffs (precision-oriented).

---

## ✨ Features
- 🔍 Modular `sa_optimizer.py` & `ga_optimizer.py` implementations
- 📊 Cooling-rate sensitivity analysis (`α = 0.90, 0.95, 0.99`)
- 📈 Convergence tracking with dual-axis temperature overlay plotting
- 🔄 Binary label conversion from multi-class NIDS attack types
- 🔁 Reproducible seeds & stratified 5-fold CV framework

---

## 📂 Project Structure
```
nids-threshold-optimization/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py                 # Data loading, feature selection, optimizer orchestration
│   ├── utils.py                # Stratified CV fitness function & metrics
│   ├── sa_optimizer.py         # Simulated Annealing implementation
│   └── ga_optimizer.py         # Genetic Algorithm implementation
├── notebooks/                  # Jupyter workflows for analysis & visualization
├── data/                       # Raw/preprocessed traffic dataset (~4K records)
└── results/                    # Plots, tables, and convergence logs
```

---

## 🚀 Usage

### Jupyter Workflow
1. Open your preferred notebook in `notebooks/` or launch a new cell session
2. Ensure `%autoreload 2` is enabled at the top if editing `.py` files during development:
   ```python
   %load_ext autoreload
   %autoreload 2
   ```
3. Run data preparation → optimizer cells sequentially
4. Execute visualization blocks for threshold trajectories & temperature overlays

---

## 📊 Results Summary
| Algorithm | Best Threshold (θ) | CV F1-Macro | Convergence Behavior |
|-----------|-------------------|-------------|----------------------|
| **SA** (`α=0.99`) | `~0.521` | `0.996` | High early variability → sharp drop ~iter 145–160 → stable plateau |
| **GA** | `~0.546` | `0.996` | Smooth population-driven convergence; early stopping at gen ~112 |

**Cooling-Rate Analysis (SA):**
| α     | Converges At (~Iter) | Final θ | CV F1-Macro |
|-------|----------------------|---------|-------------|
| 0.99  | 850                  | 0.521   | 0.996       |
| 0.95  | 175                  | 0.504   | 0.996       |
| 0.90  | 90                   | 0.531   | 0.996       |

*Final F1 is invariant to cooling rate; schedule only affects convergence speed and operational threshold positioning.*

---

## 🧪 Methodology Highlights
- **Data:** ~4,000 records with 7 engineered features (`src_bytes`, `dst_bytes`, `duration`, `serror_rate`, `rerror_rate`, `num_failed_logins`, `root_shell`)
- **Label Conversion:** Multi-class attack types → binary `0/1` (normal vs any attack)
- **Evaluation:** Stratified 5-fold CV; fitness = mean macro-F1 across folds
- **SA:** Metropolis acceptance, exponential cooling `T(t) = T₀·αᵗ`, Gaussian neighborhood clipping to `[0.4, 0.85]`
- **GA:** Arithmetic crossover, Gaussian mutation (`p=0.15`), top-10% elitism, early stopping (patience=10)

---

## 📚 References
1. Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by simulated annealing. *Science*, 220(4598), 671–680.  
2. Eiben, A. E., Hinterding, R., & Michalewicz, Z. (1999). Parameter control in evolutionary algorithms. *IEEE Transactions on Evolutionary Computation*, 3(2), 124–141.  
3. Chiba, Z., et al. (2019). A hybrid framework based on GA and SA for network IDS optimization. In *Innovations in Smart Cities Applications*. Springer.  
4. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson Education.  
5. UCI Machine Learning Repository. (1999). KDD Cup 99 dataset. https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.

**Author:** Cordero Magana  
**Course:** CS 654 – Artificial Intelligence   

---
