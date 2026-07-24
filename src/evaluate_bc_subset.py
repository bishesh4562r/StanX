import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, precision_recall_curve, f1_score, auc as sk_auc

# --- EDIT THESE to match your actual output filenames ---
STRING = 'final_1'          # param_name + '_' + str(k)
BEST_KK = 3                 # from your results/ filename
BEST_ITERATION = 9         # from your results/ filename
BATCH_SIZE = 512            # must match what you trained with
# ----------------------------------------------------------

results_dir = '../results/'
data_dir = '../data/'

# test pairs (gene_a_id, gene_b_id, label) — fixed across folds
test_data = pd.read_csv(results_dir + f'test_data_{STRING}.csv', header=None,
                         names=['gene_a', 'gene_b', 'label'])

scores = pd.read_csv(results_dir + f'{STRING}_{BEST_KK}_{BEST_ITERATION}_scores.csv',
                      header=None, names=['score'])

# ctr_eval drops the last incomplete batch, so truncate test_data to match
n_scored = len(scores)
n_full_batches = (n_scored // BATCH_SIZE) if n_scored % BATCH_SIZE == 0 else n_scored
test_data = test_data.iloc[:n_scored].reset_index(drop=True)

df = pd.concat([test_data, scores], axis=1)
df['pred'] = (df['score'] >= 0.5).astype(int)

# BC entity ids
bc_ids = set(pd.read_csv(data_dir + 'breast_related_ids.csv', header=0).iloc[:, 0]
             .dropna().astype(int).values)

df['a_is_bc'] = df['gene_a'].isin(bc_ids)
df['b_is_bc'] = df['gene_b'].isin(bc_ids)
df['either_bc'] = df['a_is_bc'] | df['b_is_bc']
df['both_bc'] = df['a_is_bc'] & df['b_is_bc']

def report(name, subset):
    if subset['label'].nunique() < 2:
        print(f'{name}: n={len(subset)}  (skipped — only one class present)')
        return
    auc_ = roc_auc_score(subset['label'], subset['score'])
    p, r, _ = precision_recall_curve(subset['label'], subset['score'])
    aupr_ = sk_auc(r, p)
    f1_ = f1_score(subset['label'], subset['pred'])
    print(f'{name}: n={len(subset):5d}  AUC={auc_:.4f}  AUPR={aupr_:.4f}  F1={f1_:.4f}')

print(f'--- {STRING} (fold {BEST_KK}, epoch {BEST_ITERATION}) ---')
report('Overall           ', df)
report('At least one BC   ', df[df['either_bc']])
report('Both BC           ', df[df['both_bc']])
report('Neither BC        ', df[~df['either_bc']])