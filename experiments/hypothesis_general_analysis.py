import pandas as pd
import os
from scipy.stats import ttest_rel, wilcoxon, shapiro, probplot
import matplotlib.pyplot as plt

DATA_DIR = r"c:\Users\julis\VSCODE\SUDcom\experiments\ud_sud_metrics.csv"

df = pd.read_csv(DATA_DIR)

metrics = {
    "Baumtiefe": ("depth_ud", "depth_sud"),
    "Durchschnittliche Abhängigkeitsdistanz": ("add_ud", "add_sud"),
    "Closeness-Zentralisierung": ("clos_cent_ud", "clos_cent_sud"),
    "Outdegree-Zentralisierung": ("outdeg_cent_ud", "outdeg_cent_sud"),
}

for name, (col_ud, col_sud) in metrics.items():
    print(f"\n=== {name} ===")
    diff = df[col_sud] - df[col_ud]
    
    # Paired t-test
    t_stat, t_p = ttest_rel(df[col_sud], df[col_ud])
    print(f"Paired t-test: t={t_stat:.3f}, p={t_p:.4g}")

    outdir = "Illustrations/results"
    os.makedirs(outdir, exist_ok=True)

    # QQ-plot
    probplot(diff, dist="norm", plot=plt)
    plt.title(f"QQ-plot of {name} differences (SUD–UD)")

    # Save instead of just showing
    plt.savefig(f"{outdir}/qq_{name}.png", dpi=300, bbox_inches="tight")
    plt.close()
    