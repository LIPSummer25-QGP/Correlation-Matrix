import uproot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#"/user/u/u25pedrochan/TMVA/TMVA_Sample/Bu_Rsideband/data_Rsideband_Bu_nochi2.root"
#"/user/u/u25pedrochan/TMVA/TMVA_Sample/Bu_2sideband/data_sidebands_Bu.root" //nochi2
# data_sidebands_Kstar.root
# data_unbinned_Bu_first.root First 2 Cuts
# MC_Bu.root
# data_Rsideband_Bu_afterChi.root
# data_Rsideband_Bu_afterChi_FirstCutted.root
# data_Rsideband_Bu_afterChi_SecondCutted.root
# === Step 1: Open ROOT file and get the TTree ===
file = uproot.open("/user/u/u25pedrochan/data_Rsideband_Bu_afterChi.root")         # Replace with your actual file
tree = file["tree"]              # Replace with actual TTree name

# === Step 2: Select branches (variables) for correlation ===
variables = [
    "B_pt", "B_y", "B_mass", "B_alpha", "B_Qvalueuj",
    "B_Qvalue","B_cos_dtheta","B_trkPtimb", "B_chi2cl", 
    "B_trk1dR","B_trk1Pt", "B_norm_svpvDistance_2D", "B_norm_svpvDistance",
    "B_norm_trk1Dxy"  
    # Replace or extend with actual variable names from your tree
]

# === Step 3: Load data into a pandas DataFrame ===
df = tree.arrays(variables, library="pd")

# === Step 4: Compute and plot correlation matrix ===
corr = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".3f", cmap="coolwarm", vmin=-1, vmax=1, annot_kws={"size": 6})
plt.xticks(rotation=45, ha="right")  # 45° inclined
plt.title("Correlation Matrix of Selected Variables Rightsideband Nocut B+")
plt.tight_layout()
plt.savefig("CM_ppRef_Rsideband_nocut_Bu.png", dpi=300)
plt.close()
