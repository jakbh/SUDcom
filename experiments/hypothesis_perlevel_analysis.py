import pandas as pd
import statsmodels.formula.api as smf


DATA_DIR = r"c:\Users\julis\VSCODE\SUDcom\experiments\ud_sud_metrics.csv"
df = pd.read_csv(DATA_DIR)

# Reshape to long format
long_df = pd.wide_to_long(
    df,
    stubnames=["depth","add","clos_cent","outdeg_cent"],
    i="id", j="schema", sep="_", suffix="\\w+"
).reset_index()

# Schema column will be "ud"/"sud" → uppercase
long_df["schema"] = long_df["schema"].str.upper()

print(long_df.head())

md = smf.mixedlm("depth ~ schema * level", long_df, groups=long_df["id"])
m_depth = md.fit()
print(m_depth.summary())