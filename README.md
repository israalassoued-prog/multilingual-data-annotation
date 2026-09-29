# Multilingual Text Data Annotation & Quality Review

## Overview

This project demonstrates a small-scale data annotation and quality assurance workflow for AI training data.

A bilingual dataset of English and French text samples was manually annotated using structured guidelines. The annotations cover sentiment, intent, language quality, relevance, and contextual ambiguity.

The project also includes a Python-based analysis of the annotated dataset and a visualization of the results.

## Objectives

- Practice manual data annotation using consistent labeling guidelines.
- Identify contextual and ambiguous examples.
- Evaluate text quality and relevance.
- Perform basic annotation quality checks.
- Analyze annotation distributions using Python and pandas.
- Visualize annotation results.

## Dataset

The dataset contains 35 English and French text samples related to common customer-service situations.

Each sample contains the following fields:

| Field | Description |
|---|---|
| `id` | Unique sample identifier |
| `text` | Original text |
| `language` | English or French |
| `sentiment` | Positive, Negative, Neutral, or Unclear |
| `intent` | Question, Request, Complaint, Feedback, Information, or Unclear |
| `language_quality` | Good or Needs Review |
| `relevance` | Relevant or Irrelevant |
| `ambiguous` | Whether contextual interpretation is required |
| `notes` | Explanation for difficult or ambiguous cases |

## Annotation Guidelines

The annotations were performed according to predefined guidelines.

### Sentiment

- **Positive** — satisfaction or favorable opinion
- **Negative** — dissatisfaction, frustration, or complaint
- **Neutral** — factual or non-evaluative statement
- **Unclear** — sentiment cannot be reliably determined

### Intent

- **Question** — asks for information
- **Request** — asks for an action
- **Complaint** — reports a problem or dissatisfaction
- **Feedback** — provides an opinion or evaluation
- **Information** — provides information without requesting an action
- **Unclear** — intent cannot be determined reliably

### Language Quality

- **Good** — clear and understandable
- **Needs Review** — significant language issues, unclear wording, or missing context

### Ambiguity

A sample is marked ambiguous when its interpretation depends on additional context.

Examples include:

- Sarcasm or irony
- Mixed evaluations
- Informal or vague wording
- Very short statements
- Missing contextual information

## Quality Review

The annotation process specifically examined difficult examples instead of forcing every sample into a simple category.

Examples include:

- `"Great, another update that broke everything."`
  - Negative sentiment despite the positive word "Great"
  - Marked as ambiguous because of sarcasm

- `"Merci pour rien."`
  - Negative sentiment
  - Marked as ambiguous because the literal wording can differ from the intended meaning

- `"Le produit est bon mais la livraison est horrible."`
  - Contains both positive and negative evaluations
  - Marked as ambiguous

- `"Whatever."`
  - Intent and meaning cannot be reliably determined without context
  - Marked as unclear and requiring review

## Analysis Results

The dataset contains:

- **35 total samples**
- **18 French samples**
- **17 English samples**
- **14 negative sentiment samples**
- **12 neutral sentiment samples**
- **8 positive sentiment samples**
- **5 ambiguous samples (14.3%)**
- **2 samples requiring language review (5.7%)**

All 35 samples were marked as relevant to the annotation task.

## Tools Used

- Python
- pandas
- Matplotlib
- CSV
- VS Code

## Project Structure

```text
data-annotation-project/
│
├── data/
│   ├── raw_data.csv
│   └── annotated_data.csv
│
├── annotation_guidelines.md
├── annotation_analysis.py
├── README.md
└── results/
    └── annotation_summary.png