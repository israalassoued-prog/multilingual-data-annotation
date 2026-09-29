# Annotation Guidelines

## 1. Sentiment

### Positive
The text expresses satisfaction, approval, or a favorable opinion.

### Negative
The text expresses dissatisfaction, frustration, a problem, or a complaint.

### Neutral
The text is factual, informational, or does not clearly express a positive or negative opinion.

---

## 2. Intent

### Question
The person is asking for information.

### Request
The person is asking someone or a service to perform an action.

### Complaint
The person reports a problem or expresses dissatisfaction.

### Feedback
The person provides an opinion, evaluation, or comment about something.

### Information
The person is simply providing information without asking a question or requesting an action.

### Unclear
The intended purpose cannot be determined reliably from the available context.

---

## 3. Language Quality

### Good
The text is clear, understandable, and contains no significant grammar or spelling problems.

### Needs Review
The text contains significant grammar/spelling problems, unclear wording, missing context, or another issue that could affect interpretation.

---

## 4. Relevance

### Relevant
The text contains information that is useful for the intended task or context.

### Irrelevant
The text does not provide useful information for the intended task or context.

---

## 5. Context / Ambiguity

Mark a sample as ambiguous when its meaning cannot be determined confidently without additional context.

Examples include:

- Sarcasm or irony
- Very short or incomplete statements
- Multiple possible interpretations
- Missing contextual information
- Informal language that changes the intended meaning

When an example is ambiguous, explain the reason in the `notes` field.

When the intent cannot be determined confidently, use the `Unclear`
intent label rather than forcing the sample into another category.
---

## 6. Annotation Principles

- Read the entire text before assigning labels.
- Base the annotation on the meaning and context, not isolated words.
- Apply the same definitions consistently across all samples.
- Do not assume information that is not present in the text.
- When uncertain, mark the sample for review and explain the uncertainty.
- Review annotations for consistency before finalizing the dataset.