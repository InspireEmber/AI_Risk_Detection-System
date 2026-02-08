# Phase 2: Data Acquisition & Understanding

## 1. Dataset Overview

- **Dataset Name**: Student Mental Health & Productivity Dataset
- **Source**: Publicly available dataset (Kaggle).
- **Link**: https://www.kaggle.com/datasets/fahadhasan93/student-mental-health-and-productivity-dataset
- **Collection Method**: Survey-based, self-reported metrics from a student population.
- **Micro-Domain**: Student lifestlye, academic habits, and subjective well-being.
- **Population**: General student body (features imply a mix of high school/undergraduate context).
- **Timeframe**: Cross-sectional snapshot (single point in time per student).

## 2. Data Acquisition Process

- **Method**: The dataset was acquired via direct download from the source repository.
- **Availability**: Open access for educational and research purposes.
- **Preprocessing**: The dataset appears to be pre-structured into a tabular format, likely aggregated from raw survey responses. No additional cleaning (imputation, encoding) has been applied in this phase.

## 3. Dataset Structure

- **Format**: Structured Tabular Data (CSV).
- **Dimensions**: 
  - Rows: 1,100 (estimated based on file preview).
  - Columns: 10 features.
- **Data Types**:
  - **Numerical (Float)**: `sleep_hours`, `study_hours`, `social_media_hours`.
  - **Numerical (Integer)**: `exercise_minutes`, `class_attendance_percent`, `assignment_deadlines_missed`, `mental_health_score`.
  - **Ordinal/Scale (Integer)**: `stress_level` (1-10), `focus_level` (1-10).
  - **Identifier**: `student_id`.

## 4. Target Variable Identification

To align with the **Dual-Module** architecture defined in Phase 1:

### Module A: Academic Risk
- **Primary Target Feature**: `assignment_deadlines_missed`
  - *Rationale*: A direct, authorized indicator of academic dysfunction and executive failure.
- **Secondary Target Feature**: `class_attendance_percent`
  - *Rationale*: A strong proxy for disengagement and dropout risk.

### Module B: Well-Being Risk
- **Primary Target Feature**: `mental_health_score` (0-100)
  - *Rationale*: A composite metric representing the overall psychological state.
- **Secondary Target Feature**: `stress_level` (1-10)
  - *Rationale*: A subjective self-assessment that captures acute distress.

## 5. Feature Categories

### Academic-Related
- `study_hours`: Active effort input.
- `class_attendance_percent`: Engagement metric.
- `assignment_deadlines_missed`: Performance/Dysfunction output.

### Lifestyle-Related
- `sleep_hours`: Physiological recovery metric.
- `social_media_hours`: Digital consumption/Distraction metric.
- `exercise_minutes`: Physical coping mechanism.

### Psychological & Cognitive Indicators
- `stress_level`: Subjective emotional state.
- `focus_level`: Cognitive capacity/Executive function.
- `mental_health_score`: Aggregate well-being index.

## 6. Data Quality Assessment (Qualitative)

- **Self-Reporting Bias**: High. Features like `stress_level` and `focus_level` are subjective and depend on the student's self-perception, not clinical diagnosis.
- **Missing Values**: The dataset is fully populated (0 missing values), suggesting it may be synthetic or heavily curated.
- **Subjectivity**: "Mental Health Score" is likely a calculated index or self-reported value, not a clinician's assessment.
- **Causality**: The data is cross-sectional; we cannot definitively say `social_media_hours` *caused* `stress`, only that they are correlated.

## 7. Assumptions & Limitations

### Assumptions
1. **Honesty**: We assume students reported their habits (e.g., social media usage) truthfully, despite social desirability bias.
2. **Consistency**: We assume the scale (1-10) is interpreted similarly across the population.

### Limitations
- **No Longitudinal Data**: We cannot track deterioration over time (e.g., "stress increasing week-over-week").
- **Lack of Clinical History**: No data on prior diagnoses, medication, or therapy, which limits distinct medical validation.
- **Simplified Academic Metric**: `assignment_deadlines_missed` is a proxy for academic failure, but does not capture test scores or grades directly.

### Risks
- **Over-Interpretation**: Models might learn to "detect" stress based on simple correlates (e.g., low sleep) without understanding the root cause.
- **Circular Logic**: If `mental_health_score` is just a sum of `stress_level` and `sleep_hours`, predictions will be deterministic, not predictive.

## 8. Phase-2 Output Summary

- **Understanding**: We have mapped the dataset columns to the Dual-Module problems (Academic vs. Well-Being).
- **Unresolved**: The exact derivation of `mental_health_score` is unknown (is it a formula?). This will be tested in Phase 3 (EDA).
- **Readiness**: The dataset involves relevant features for both modules and is structured correctly for exploratory analysis.

**Status**: Ready for Phase 3 (Exploratory Data Analysis).
