# Phase 1: Problem Framing

## 📝 Problem Definition

Educational institutions often struggle to identify at-risk students before they fail or experience severe mental health crises. This project addresses two critical facets:

1. **Academic Persistence**: Identifying students likely to drop out or fail based on behavior and history.
2. **Mental Well-being**: Detecting early signs of high stress or emotional distress through text analysis.

## 👥 Stakeholders & Impact

- **Students**: Receive proactive support and early intervention.
- **Educators**: Targeted focus on students who need the most help.
- **Counselors**: Quantifiable data to prioritize mental health check-ins.

## 🎯 Success Metrics

- **Module A (Academic)**: High Recall (minimizing missed at-risk students) while maintaining acceptable Precision.
- **Module B (Mental Health)**: Maximum sensitivity to high-stress indicators (Recall > 0.90 for "High Risk" class).
- **Explainability**: 100% of predictions must be accompanied by a human-readable "Why?" factor.

## 🛠 Assumptions

- Student historical data is available and updated regularly.
- Text inputs (logs/journals) are provided voluntarily by students.
- Risk levels are categorized into Low, Medium, and High.

## ⚠️ Known Risks

- **Data Privacy**: Handling sensitive mental health text requires strict de-identification.
- **Self-Reporting Bias**: Students might mask their true feelings in digital logs.
- **Automation Bias**: Educators might rely too heavily on the AI without human judgment.

## 🔄 Alternatives Considered

- **Heuristic-based flagging**: Rule-based systems (e.g., "if GPA < 2.0") are too rigid and lack predictive power.
- **Single-module system**: Would miss the correlation between mental health and academic performance.
