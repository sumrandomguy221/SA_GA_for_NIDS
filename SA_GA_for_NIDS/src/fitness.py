import numpy as np
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold

def compute_cv_fitness(candidate_threshold, X, y, clf_class, n_splits, random_state=42):
    """Run stratified K-fold CV and return mean F1-macro as fitness score."""
    print("Running fitness fucntion...")
    
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    f1_scores = []
    
    for train_idx, val_idx in skf.split(X, y):
        X_train, X_val = X[train_idx], X[val_idx]
        y_train, y_val = y[train_idx], y[val_idx]
        
        clf = clf_class().fit(X_train, y_train)
        proba = clf.predict_proba(X_val)[:, 1]
        preds = (proba >= candidate_threshold).astype(int)
        
        f1_scores.append(f1_score(y_val, preds, average='macro'))

    print("...Process complete!")
    return np.mean(f1_scores)