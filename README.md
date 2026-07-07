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
├── src/
│   ├── main.ipynb              # Jupyter workflow for analysis & visualization
│   ├── utils.py                # Stratified CV fitness function & metrics
│   ├── sa_optimizer.py         # Simulated Annealing implementation
│   └── ga_optimizer.py         # Genetic Algorithm implementation
└── data/                       # Raw/preprocessed traffic dataset (~4K records)
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
| **SA** (`α=0.99`) | `~0.521` | `0.996` | High early variability → converse around iteration 850 |
| **GA** | `~0.546` | `0.996` | Smooth population-driven convergence |

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
1. Artificial Intelligence: Foundations of Computational Agents, 3rd edition. David L. Poole and Alan K. Mackworth. Cambridge University Press. ISBN: 978-1009258197.2023
2. Chawathe, S., Bishop, P., McHugh, J., & Wang, H. (1999). The KDD'99 intrusion detection evaluation dataset. University of California, Irvine Machine Learning Repository. https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
3. Chiba, Z., Abghour, N., Moussaid, K., El omri, A., Rida, M. (2019). A New Hybrid Framework Based on Improved Genetic Algorithm and Simulated Annealing Algorithm for Optimization of Network IDS Based on BP Neural Network. In: Ben Ahmed, M., Boudhir, A., Younes, A. (eds) Innovations in Smart Cities Applications Edition 2. SCA 2018. Lecture Notes in Intelligent Transportation and Infrastructure. Springer, Cham. https://doi.org/10.1007/978-3-030-11196-0_43  
4. Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Pearson Education. 

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.

**Author:** Cordero Magana  
**Course:** CS 654 – Artificial Intelligence   

---
