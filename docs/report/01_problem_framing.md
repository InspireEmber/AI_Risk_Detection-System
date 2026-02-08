# Phase 1: Problem Framing — Dual Module (A + B)

## 1. Problem Statement

Students often experience academic decline and well-being challenges that go undetected until performance or behavior deteriorates significantly. Institutions lack early, interpretable signals to identify at-risk students and prioritize timely support. This project focuses on risk identification (not diagnosis) to assist teachers and counselors in making informed, early interventions.

## 2. Dual-Module Structure

The system is explicitly divided into two independent but related modules:

- **Module A — Academic Risk**: Identifies students at risk of academic decline (GPA drop, course failure, disengagement).
- **Module B — Well-Being Risk**: Identifies students at risk of well-being deterioration using non-clinical, observable indicators.

Each module produces its own **independent risk score and explanation**.

## 3. Proposed Solution

The system outputs two continuous risk scores [0, 1]:

- **A-Score (Academic Risk)**: Likelihood of near-term academic decline.
- **B-Score (Well-Being Risk)**: Likelihood of entering a high-risk well-being state.
  Higher scores indicate greater urgency for human attention.

## 4. Role of Human Intervention

The system is a **decision-support tool only**:

- **Teachers** act on Academic Risk Scores.
- **Counselors** act on Well-Being Risk Scores.
- **No automated decisions**, penalties, or clinical diagnoses.

## 5. Definition of “Risk”

### Academic Risk (Module A)

- Declining GPA or grades.
- Missing or late assignments.
- Attendance irregularities.
- Reduced learning platform engagement.

### Well-Being Risk (Module B)

- Persistent disengagement or withdrawal.
- Sudden behavioral changes.
- Self-reported stress or burnout indicators.
- Environmental and contextual stressors.

## 6. Feature Conceptualization

### Module A — Academic Risk Indicators

| Feature Category     | Observable Indicator      | Data Source     |
| :------------------- | :------------------------ | :-------------- |
| Academic Performance | Low or declining GPA      | Gradebooks      |
| Assignment Behavior  | Missed / late submissions | LMS             |
| Attendance           | Frequent absences         | Attendance logs |
| Digital Engagement   | Reduced activity          | LMS analytics   |

### Module B — Well-Being Risk Indicators

| Feature Category       | Observable Indicator         | Non-Clinical Source   |
| :--------------------- | :--------------------------- | :-------------------- |
| Emotional & Behavioral | Withdrawal, visible distress | Teacher observations  |
| Self-Reported          | High stress, burnout scores  | Surveys               |
| Behavioral Incidents   | Repeated non-academic issues | Incident logs         |
| Contextual             | Housing, workload stress     | Institutional records |

_Note: Sensitive attributes (age, gender) are used for fairness checks/context only, not direct prediction._

## 7. Explainability Requirement

Each score must answer:

- **Why** is the student at risk?
- **Which** factors contributed most?
- **What** has changed recently?

## 8. Ethical Boundary Lock

- **No mental health diagnosis.**
- **No automated penalties.**
- **Mandatory human-in-the-loop.**
- **Privacy-aware data handling.**

## 9. One-Sentence Project Definition

An explainable dual-module system assigning academic and well-being risk scores to support early, human-led intervention.
