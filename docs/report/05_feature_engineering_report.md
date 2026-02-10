# Phase 5: Preprocessing & Feature Engineering Report

**Project**: Student Stress Risk Prediction with Explainable AI  
**Role**: ML Engineer / Data Architect  
**Date**: 2026-02-10  

---

## 1. Executive Summary
Following the Phase 4 Audit, the data was found to be structurally sound but required advanced transformations to reach "model-ready" status. Phase 5 focused on mitigating linear dependency (the "24-Hour Law"), handling high cardinality, and engineering domain-specific interaction ratios to improve predictive signal.

## 2. Transformations Performed

### A. Cardinality Management
- **Action**: Dropped `Student_ID`.
- **Rationale**: 100% uniqueness in `Student_ID` (2,000 unique values) would lead to categorical overfitting, where a model memorizes the ID rather than learning student behavior patterns.

### B. Compositional Data Correction (Linear Dependency)
- **Problem**: Total activity hours summed to exactly 24.0, creating infinite multicollinearity.
- **Action**:
    1. Fixed minor floating-point artifacts to ensure exactly 24.0.
    2. Dropped `Extracurricular_Hours_Per_Day`.
- **Result**: Remaining features are no longer linearly dependent, allowing for stable convergence in linear and distance-based models.

### C. Advanced Feature Engineering (Ratios)
We created three primary interaction features to capture the "balance" of a student's life:
1. **Academic Pressure Index**: `Study_Hours / (Social_Hours + Sleep_Hours)`. Captures the relative strain of academic work against recovery time.
2. **Wellness Ratio**: `(Physical_Activity + Sleep) / Study_Hours`. Measures how well a student offsets academic load with health-positive activities.
3. **GPA Efficiency**: `GPA / Study_Hours`. Measures the "return on investment" for study time.

### D. Data Normalization & Encoding
- **Target Encoding**: `Stress_Level` mapped to Ordinal integers: `Low: 0`, `Moderate: 1`, `High: 2`.
- **Feature Scaling**: All numerical features normalized to a `[0, 1]` range using `MinMaxScaler`. This ensures that GPA (0-4 scale) and lifestyle features (various hour scales) are treated with equal weight by distance-based algorithms.

## 3. Data Readiness Verdict

**File Created**: `data/processed_student_data.csv`  
**Verdict**: **READY FOR ML BASELINE.**

The dataset is now mathematically robust. The engineered ratios show better statistical separation between stress classes in initial diagnostic plots than the raw hour features.

---

**Approval**:  
*Antigravity - ML Lead*
