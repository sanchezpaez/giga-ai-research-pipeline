# AI-assisted Political Research Explorer  
**PREPPS Latin America – Concept Prototype for GIGA**

## Overview
This repository contains a **conceptual prototype** of an AI-assisted digital research service designed for social science research institutions such as the German Institute for Global and Area Studies (GIGA).

The project demonstrates how expert survey data can be processed, explored, and **interpreted responsibly** using a combination of:
- reproducible data analysis workflows,
- cloud-based infrastructure (AWS),
- and controlled use of Large Language Models via **Amazon Bedrock**.

The goal is not to automate political analysis, but to **support researchers in exploratory interpretation while preserving methodological rigor**.

---

## Research Context
The project is based on the **PREPPS Latin America** expert survey, which captures:
- political party positions on key ideological dimensions (`score_pos`),
- the salience or importance of these dimensions (`score_imp`),
- and the level of expert agreement or disagreement (`sd_pos`).

Each observation represents a *party × political dimension* combination.  
As the data is based on expert judgments rather than direct measurement, **quality control, aggregation, and cautious interpretation are essential**.

---

## Motivation
Researchers working with complex comparative datasets often face two recurring challenges:

1. High technical barriers to exploring and aggregating data.
2. Time-consuming interpretation of statistical results, especially for non-technical users.

This project addresses these challenges by:
- separating statistical computation from interpretation,
- and introducing AI **only at the interpretative layer**, not as a replacement for analysis.

---

## Conceptual Architecture

### Data and processing flow
The service is designed as a modular pipeline with clearly separated responsibilities:

1. **Cleaned and aggregated data**  
   Quality-controlled, aggregated survey results stored in **Amazon S3**.

2. **Processing and orchestration**  
   **AWS Lambda** functions load aggregated data and prepare structured inputs.

3. **Prompt construction**  
   A controlled prompt is generated, explicitly constraining the AI to descriptive and methodological interpretation.

4. **AI interpretation**  
   **Amazon Bedrock (Claude)** produces a concise analytical summary based strictly on the provided data.

5. **Research output**  
   The resulting interpretative summary is stored or delivered as a research support artifact.

---

## Role of AI
Amazon Bedrock is used exclusively to:
- summarise aggregated results,
- highlight salient political dimensions,
- identify areas of high expert disagreement,
- and generate methodological cautions for researchers.

The AI component:
- does **not** calculate statistics,
- does **not** infer causal relationships,
- does **not** access raw expert responses.

This ensures transparency, reproducibility, and institutional compliance.

---

## Why Amazon Bedrock
Amazon Bedrock was selected because it:
- keeps data within AWS infrastructure,
- supports governance and compliance requirements typical of public research institutions,
- avoids reliance on external third-party APIs,
- allows controlled, auditable use of Large Language Models.

---

## Current Project Status
- PREPPS dataset explored and structurally analysed.
- Quality filtering applied to expert responses.
- Aggregations implemented locally using pandas.
- Exploratory visualisations created (importance, position vs. salience, expert disagreement).
- Prompt design for AI-assisted interpretation completed.
- Cloud architecture (S3, Lambda, Bedrock) defined at a conceptual level.

---

## Methodological Principles
The project follows several key methodological principles:

- **Separation of concerns**: data ingestion, analysis, and interpretation are clearly separated.
- **Aggregation before interpretation**: AI is applied only to aggregated, quality-controlled results.
- **Transparency**: all assumptions and thresholds (e.g. minimum number of expert responses) are explicit.
- **Human-in-the-loop**: AI outputs are intended as research support, not authoritative conclusions.

---

## Potential Extensions
Possible future extensions of this prototype include:
- API-based access for researchers.
- Integration with additional GIGA datasets.
- Automated methodological quality alerts.
- Cross-dataset semantic comparison using embeddings.
- Lightweight research dashboards for non-technical users.

---

## Disclaimer
This repository represents a **research and infrastructure prototype**.  
It is not intended to produce publishable scientific results, but to demonstrate how AI and cloud infrastructure can responsibly support social science research workflows.

---

## Author
**Sandra Sánchez Páez**  
Computational Linguist & AI Research Specialist  
