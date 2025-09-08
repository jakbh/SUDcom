import pandas as pd
from scipy.stats import ttest_rel, wilcoxon, shapiro, probplot
import matplotlib.pyplot as plt

DATA_DIR = r"c:\Users\julis\VSCODE\SUDcom\experiments\ud_sud_metrics.csv"

df = pd.read_csv(DATA_DIR)

metrics = {
    "depth": ("depth_ud", "depth_sud"),
    "ADD": ("add_ud", "add_sud"),
    "Closeness centralization": ("clos_cent_ud", "clos_cent_sud"),
    "Outdegree centralization": ("outdeg_cent_ud", "outdeg_cent_sud"),
}

for name, (col_ud, col_sud) in metrics.items():
    print(f"\n=== {name} ===")
    diff = df[col_sud] - df[col_ud]
    
    # Paired t-test
    t_stat, t_p = ttest_rel(df[col_sud], df[col_ud])
    print(f"Paired t-test: t={t_stat:.3f}, p={t_p:.4g}")
    
    # Wilcoxon
    try:
        w_stat, w_p = wilcoxon(df[col_sud], df[col_ud])
        print(f"Wilcoxon: W={w_stat:.3f}, p={w_p:.4g}")
    except ValueError as e:
        print(f"Wilcoxon could not be computed: {e}")
    
    # Shapiro–Wilk normality test
    shap_stat, shap_p = shapiro(diff)
    print(f"Shapiro–Wilk (diffs): W={shap_stat:.3f}, p={shap_p:.4g}")
    if shap_p > 0.05:
        print("  → Differences look approximately normal (t-test OK).")
    else:
        print("  → Differences deviate from normal (Wilcoxon safer).")
    
    # QQ-plot
    probplot(diff, dist="norm", plot=plt)
    plt.title(f"QQ-plot of {name} differences (SUD–UD)")
    plt.show()
    
    # Histogram
    plt.hist(diff, bins=15, edgecolor="black")
    plt.title(f"Histogram of {name} differences (SUD–UD)")
    plt.xlabel("Difference")
    plt.ylabel("Frequency")
    plt.show()