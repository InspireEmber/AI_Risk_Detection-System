
# Phase 3: Exploratory Data Analysis (EDA) Report

**Project**: Student Stress Risk Prediction with Explainable AI  
**Role**: Exploratory Data Analysis Lead & Methodological Gatekeeper  
**Date**: 2026-02-09

---

## 1. Dataset Overview
The primary dataset (`data/raw.csv`) contains structured tabular data representing student lifestyle factors and academic performance. It is designed to support **Module A** (Stress Risk Prediction) by mapping behavioral and academic indicators to subjective stress levels.

- **Rows**: 2,000
- **Columns**: 8
- **Feature Types**: 
    - 6 Numerical (Continuous/Discrete)
    - 1 Categorical (Target: `Stress_Level`)
    - 1 Identifier (`Student_ID`)
- **Purpose**: Diagnostic assessment of features determining student stress risk.

---

## 2. Target Analysis: `Stress_Level`
The target variable is categorical and ordinal in nature (Low < Moderate < High).

### Distribution & Imbalance
| Class | Count | Percentage |
| :--- | :--- | :--- |
| **High** | 1,029 | 51.45% |
| **Moderate** | 674 | 33.70% |
| **Low** | 297 | 14.85% |

### Red Flags
- **Significant Class Imbalance**: The dataset is heavily skewed toward "High" stress levels (over 50%). Models trained on this data may over-predict high-risk cases.
- **Ordinal Behavior**: Distribution suggests `Stress_Level` behaves more as an intensity score than a nominal class.

---

## 3. Univariate Feature Analysis
Individual features show specific ranges and behavioral patterns.

| Feature | Range | Mean | Skewness | Observations |
| :--- | :--- | :--- | :--- | :--- |
| `Study_Hours_Per_Day` | 5.0 - 10.0 | 7.48 | 0.03 | Uniformly distributed around 7.5h. |
| `Extracurricular_Hours_Per_Day` | 0.0 - 4.0 | 1.99 | 0.00 | Perfectly centered normal-like distribution. |
| `Sleep_Hours_Per_Day` | 5.0 - 10.0 | 7.50 | -0.01 | Balanced sleep patterns reported. |
| `Social_Hours_Per_Day` | 0.0 - 6.0 | 2.70 | 0.18 | Slightly right-skewed; most students spend <4h. |
| `Physical_Activity_Hours_Per_Day` | 0.0 - 13.0 | 4.33 | 0.40 | **High Risk Outlier**: 13h/day is likely noisy or erroneous. |
| `GPA` | 2.24 - 4.0 | 3.12 | 0.03 | Academic performance is healthy (Mean ~3.1). |

---

## 4. Bivariate Analysis: Relationships

### Feature vs. `Stress_Level`
Correlations calculated using ordinal encoding (Low=0, Moderate=1, High=2):
- **Positive Correlations**:
    - `Study_Hours_Per_Day` (**0.74**): Strongest predictor; higher study load directly tracks with higher stress.
    - `GPA` (**0.55**): Paradoxically, higher-performing students report higher stress levels.
- **Negative Correlations**:
    - `Sleep_Hours_Per_Day` (**-0.30**): Lack of sleep is a moderate indicator of stress.
    - `Physical_Activity_Hours_Per_Day` (**-0.21**): Activity has a mild buffering effect on perceived stress.

### Feature-Feature Redundancy (Collinearity)
- **`GPA` vs. `Study_Hours_Per_Day` (0.73)**: High collinearity. Performance is structurally tied to time investment in this dataset. Modeling should consider if both are necessary or if one acts as a proxy for the other.

---

## 5. Multivariate Signals
Preliminary exploratory signals suggest that the interaction between `Study_Hours_Per_Day` and `Sleep_Hours_Per_Day` creates the most distinct stress clusters. Students with >8h study and <6h sleep are almost exclusively in the **High Stress** category.

---

## 6. EDA Summary Table

| Key Insight | Key Risk | Open Questions |
| :--- | :--- | :--- |
| Stress is primarily driven by study hours and academic pressure (`GPA`). | Physical Activity (13h/day) contains extreme values that may skew regression-based models. | Is the high stress level a result of academic ambition or poor time management? |
| Clear ordinal relationship between features and target. | `GPA` and `Study_Hours` are redundant; may lead to inflated feature importance. | Would text-based entries (Module B) explain the high variance in "Moderate" stress? |

---

## 7. Explicit EDA Boundaries
- **No Predictive Conclusions**: We describe correlations, not predictive reliability.
- **No Feature Engineering**: Ratios like `Study/Sleep` are noted but not yet created.
- **Module Boundary**: This analysis serves **Module A**. While **Module B** (NLP) exists, this EDA does not assume text data will solve the "Moderate" stress classification noise.
- **Imputation**: No missing values were found, so no imputation strategy is proposed yet.

---

> **Gatekeeper Policy**: "EDA describes what the data is, not what we wish it were."
