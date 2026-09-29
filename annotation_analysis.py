import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the annotated dataset
file_path = Path("data/annotated_data.csv")
df = pd.read_csv(file_path)

# Create results folder if it doesn't exist
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

print("=" * 50)
print("ANNOTATION DATASET ANALYSIS")
print("=" * 50)

print(f"\nTotal samples: {len(df)}")

print("\n--- Language Distribution ---")
print(df["language"].value_counts())

print("\n--- Sentiment Distribution ---")
print(df["sentiment"].value_counts())

print("\n--- Intent Distribution ---")
print(df["intent"].value_counts())

print("\n--- Language Quality ---")
print(df["language_quality"].value_counts())

print("\n--- Relevance ---")
print(df["relevance"].value_counts())

print("\n--- Ambiguous Samples ---")
print(df["ambiguous"].value_counts())

# Quality indicators
ambiguous_count = (df["ambiguous"] == "Yes").sum()
review_count = (df["language_quality"] == "Needs Review").sum()

ambiguous_percentage = ambiguous_count / len(df) * 100
review_percentage = review_count / len(df) * 100

print("\n--- Quality Indicators ---")
print(f"Ambiguous samples: {ambiguous_count} ({ambiguous_percentage:.1f}%)")
print(f"Samples needing language review: {review_count} ({review_percentage:.1f}%)")

# Samples requiring review
print("\n--- Samples Requiring Review ---")

review_df = df[
    (df["ambiguous"] == "Yes") |
    (df["language_quality"] == "Needs Review")
]

if len(review_df) > 0:
    print(
        review_df[
            ["id", "text", "language", "intent",
             "language_quality", "ambiguous", "notes"]
        ].to_string(index=False)
    )
else:
    print("No samples require additional review.")

# --------------------------------------------------
# Visualization
# --------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Language distribution
df["language"].value_counts().plot(
    kind="bar",
    ax=axes[0, 0],
    title="Language Distribution"
)
axes[0, 0].set_xlabel("Language")
axes[0, 0].set_ylabel("Number of Samples")

# Sentiment distribution
df["sentiment"].value_counts().plot(
    kind="bar",
    ax=axes[0, 1],
    title="Sentiment Distribution"
)
axes[0, 1].set_xlabel("Sentiment")
axes[0, 1].set_ylabel("Number of Samples")

# Intent distribution
df["intent"].value_counts().plot(
    kind="bar",
    ax=axes[1, 0],
    title="Intent Distribution"
)
axes[1, 0].set_xlabel("Intent")
axes[1, 0].set_ylabel("Number of Samples")

# Quality / ambiguity
quality_data = pd.Series({
    "Ambiguous": ambiguous_count,
    "Needs Review": review_count
})

quality_data.plot(
    kind="bar",
    ax=axes[1, 1],
    title="Quality Review Indicators"
)
axes[1, 1].set_xlabel("Category")
axes[1, 1].set_ylabel("Number of Samples")

plt.tight_layout()

output_path = results_dir / "annotation_summary.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"\nVisualization saved to: {output_path}")

print("\n" + "=" * 50)
print("Analysis complete.")
print("=" * 50)