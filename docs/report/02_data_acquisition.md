# Phase 2: Data Acquisition — [Completed]

## 📂 Dataset Overview — Student Lifestyle & Well-being

**Status**: Dataset Acquired (`data/raw.csv`)

We have acquired a new dataset focused on student lifestyle, academic performance, and stress levels. This dataset serves as the foundation for **Module A (Academic Risk)** and contributes to the target variables for **Module B (Well-being)**.

### Dataset Specifications
- **Source**: Local (`data/raw.csv`)
- **Format**: CSV (Tabular)
- **Size**: ~2,000 Records

### Feature Schema

| Column Name | Type | Description | Module Relevance |
| :--- | :--- | :--- | :--- |
| `Student_ID` | Categorical | Unique Identifier | Metadata |
| `Study_Hours_Per_Day` | Numerical | Daily study duration | Module A |
| `Extracurricular_Hours_Per_Day` | Numerical | Time spent on clubs/sports | Module A |
| `Sleep_Hours_Per_Day` | Numerical | Daily sleep duration | Module A / B |
| `Social_Hours_Per_Day` | Numerical | Time spent socializing | Module A / B |
| `Physical_Activity_Hours_Per_Day` | Numerical | Exercise duration | Module A / B |
| `GPA` | Numerical | Grade Point Average | **Module A Target** (Academic Performance) |
| `Stress_Level` | Categorical | Self-reported stress (Low/Moderate/High) | **Module B Target** (Mental Health) |

### Initial Observations
This dataset provides a direct link between **lifestyle habits** (Sleep, Study, Activity) and **outcomes** (GPA, Stress). 
- **Academic Risk** can be modeled by predicting `GPA` or identifying low-GPA clusters based on habits.
- **Mental Health Risk** is directly labeled via `Stress_Level`.

### Next Steps
1. Perform Exploratory Data Analysis (EDA) in `notebooks/01_student_eda.ipynb` to check for missing values, outliers, and correlations.
2. Preprocess data (normalization, encoding `Stress_Level`).
3. Split into Train/Test sets for Model A training.

### Limitations & Research Integrity
- **Absence of Text Data**: The acquired dataset (`data/raw.csv`) is exclusively tabular and does not contain student journals.
- **Module B Decision**: To preserve the empirical credibility of Module A, we will **not** hallucinate text for the 2,000 students. Instead, Module B will utilize **Synthetic Student Narratives** as an independent "test-bench" for architectural demonstration and XAI pipeline validation.

### One-Sentence Policy Rule
> "Module A shall be the sole source of empirical truth for risk prediction, while Module B serves as an uncoupled architectural framework for demonstrating NLP-driven interpretability."
