
# Phase 4: Data Validation & Integrity Audit

**Project**: Student Stress Risk Prediction with Explainable AI  
**Role**: Data Integrity Officer & Validation Authority  
**Date**: 2026-02-09  

---

## 1. Validation Summary Table

| Feature | Check Performed | Status | Findings / Notes |
| :--- | :--- | :--- | :--- |
| **Schema** | Type & Name Audit | **PASS** | `int64` for ID, `float64` for metrics, `object` for Target. |
| **Study_Hours** | Range (5-10) | **PASS** | Plausible for a full-time student. |
| **Social_Hours** | Range (0-6) | **PASS** | No violations observed. |
| **Physical_Hours** | Range (0-13) | **FLAG** | Max value of 13.0h is extreme but physically possible. |
| **GPA** | Range (2.24-4.0) | **PASS** | Normal academic distribution. |
| **Total Daily Sum** | Cross-feature sum | **FLAG** | Every row sums to exactly 24.0 hours (Compositional Data). |
| **Missingness** | Null Count | **PASS** | 0.0% Missing values across all 2000 rows. |
| **Target Label** | Set Integrity | **PASS** | Labels limited to {Low, Moderate, High}. |

---

## 2. Critical Risk List

### A. Perfect Linear Dependency (Compositional Data)
The audit reveals that **Total_Hours (Sum of all 5 activity features) = 24.0** for every student in the dataset.  
*   **Risk**: Including all activity features in a model will result in a singular matrix (Infinite Multicollinearity). 
*   **Impact**: Linear models (Logistic Regression) will fail without regularization or dropping one feature.

### B. High Concentration in High-Stress Category
The Target distribution (`High`: 51.4%) vs (`Low`: 14.8%) is valid but represents a "Risk-Saturated" environment. 
*   **Risk**: Potential "Label Bias" in the data collection source (e.g., data collected during finals week).

---

## 3. Safe-to-Model Verdict

**Verdict: YES, WITH DOCUMENTED CAVEATS.**

The dataset is internally consistent and lacks "impossible" values (no negative hours, no >24h sums). It is structurally ready for Module A. However, the modeler must be warned that the data is **compositional**, meaning the value of one feature is constrained by the others.

*Resolution (2026-02-10)*: Compositional constraints were mitigated in Phase 5 by dropping `Extracurricular_Hours_Per_Day`.

---

## 4. Constraints for Cleaning & Preprocessing

1.  **Redundancy Handling**: One feature from the "Hours" set *must* be dropped if using non-regularized linear models, or the model must utilize Tree-based methods (RF, XGBoost) which handle collinearity better.
2.  **No Imputation Needed**: The 0% missing rate means no synthetic data generation is permitted.
3.  **Floating Point Cleanup**: The sum-to-24 check showed minor floating-point artifacts (24.000...04). Preprocessing should normalize these to exactly 24.0 if numerical precision becomes an issue.
4.  **Label Preservation**: No undersampling of the 'High' class or oversampling of 'Low' class is allowed in the *Validation* state; balancing is only permitted in the model training experiments.

---

**Approval**:  
*Antigravity - Validation Authority*
