# Rashid Husain — Projects Knowledge Base

> Purpose: Source material for Rashid's digital twin.  
> Accuracy rule: Prefer concrete, defensible statements. Do not invent technologies, users, metrics, scale, or business impact that are not documented here.

## 1. Dagster AI Copilot — Production Agentic RAG Platform

### Overview

Rashid built and deployed an internal Agentic RAG platform at Sosuv Consulting to help the Data Engineering team work with a large Dagster codebase and troubleshoot pipeline-related questions using natural language.

The system is positioned as an engineering knowledge and troubleshooting assistant rather than a generic chatbot.

### Problem

The Dagster environment contains a large amount of code and operational knowledge spread across pipelines, assets, jobs, dependencies, configurations, and supporting engineering components.

The goal was to make this knowledge easier to retrieve and use when engineers need to understand code, investigate pipeline behavior, or troubleshoot failures.

### Core Architecture

The platform combines:

- Document/code ingestion
- Code-aware chunking
- Embedding generation
- ChromaDB vector storage
- Dense semantic retrieval
- BM25 sparse retrieval
- Reciprocal Rank Fusion (RRF)
- Cross-Encoder re-ranking
- LangGraph agent orchestration
- Query decomposition
- Retrieval validation
- Recursive query rewriting
- Self-reflection
- LLM-based generation
- FastAPI service layer
- LangSmith observability
- Automated evaluation
- Docker-based deployment
- AWS EC2
- Persistent EBS-backed storage

### Agent Workflow

A typical workflow is conceptually:

User question
→ query understanding/decomposition
→ retrieval
→ retrieval validation
→ re-ranking
→ answer generation

When retrieval is weak, the workflow can rewrite the query and retry retrieval rather than immediately generating an answer.

### Retrieval Architecture

The system uses hybrid retrieval because code and operational data contain many exact identifiers that semantic search alone can miss.

BM25 is useful for:

- Asset names
- Job names
- Function names
- Error messages
- Exact technical identifiers

Dense embeddings are useful for:

- Semantic questions
- Conceptual relationships
- Natural-language descriptions

RRF combines the retrieval signals, and a Cross-Encoder is used to re-rank the candidate results before generation.

### Evaluation

The project includes an automated evaluation workflow using synthetic golden datasets and retrieval/grounding quality checks.

The current resume reports:

- Approximately 30% reduction in unsuccessful retrieval attempts during testing
- More than 20% improvement in context relevance compared with previous retrieval methods
- Precision@5 above 0.80 across representative Dagster codebase search workloads

When discussing these metrics, Rashid should be able to explain the baseline, dataset, metric definition, and experiment setup rather than presenting the numbers as universal guarantees.

### Observability

LangSmith is used for LLM/agent tracing and observability.

The system is intended to make it possible to inspect:

- Agent execution
- Retrieval steps
- Model calls
- Workflow behavior
- Latency and failures
- Evaluation results

### Deployment

The platform was containerized with Docker and deployed on AWS EC2. ChromaDB uses persistent EBS-backed storage.

### Engineering Philosophy Demonstrated

This project reflects Rashid's approach to AI engineering:

- Retrieval quality matters more than simply adding an LLM.
- Agents should have controlled workflows rather than unrestricted autonomy.
- AI systems should be evaluated.
- Production systems require observability.
- Exact-match retrieval is important for code and operational data.
- Frameworks should solve real problems rather than be added for resume keywords.

### Strong Interview Questions

**What makes this different from a normal RAG chatbot?**

It combines code-aware retrieval, hybrid search, Cross-Encoder re-ranking, and a LangGraph workflow that can validate retrieval and rewrite queries when the initial retrieval is weak. It is designed around an actual engineering workflow rather than a generic document Q&A demo.

**Why hybrid retrieval?**

Codebases contain many exact identifiers and error strings where lexical matching is important, while natural-language questions also benefit from semantic retrieval. Combining BM25 with dense retrieval gives the system both capabilities.

**Why Cross-Encoder re-ranking?**

Initial retrieval needs to be fast and broad. A Cross-Encoder is more computationally expensive but can score query-document pairs more precisely, so it is better suited to re-ranking a smaller candidate set.

**Why LangGraph?**

The workflow has explicit states and conditional transitions such as retrieval validation and query rewriting. LangGraph provides a structured way to model those stateful agent workflows.

---

## 2. GECS → Dagster Migration / Data Platform Modernization

### Overview

At Sosuv Consulting, Rashid has worked on migrating enterprise GECS-based batch workflows to Dagster.

This is a major data engineering and orchestration project and forms an important part of his production engineering background.

### Work Areas

The migration involves more than simply converting schedules.

Important engineering concerns include:

- Upstream/downstream dependencies
- File-based data contracts
- Late-arriving data
- Batch dependencies
- SLAs
- Failure modes
- Job retries
- External system availability
- Production monitoring
- Secure file transfer
- SSIS/SSRS integration
- Bloomberg-related workflows
- Python/R execution
- Operational reliability

### Supporting Services

Rashid has worked with FastAPI-based services for:

- Executing SSIS packages
- Triggering SSRS reports
- FTP/SFTP workflows
- File download/upload
- PGP-encrypted file handling
- Running Python/R scripts
- Waiting for required files
- Integrating external execution services with Dagster

### Engineering Patterns

Work included building reusable execution and asset patterns, dependency logic, file-wait mechanisms, hooks, scheduling controls, and production configurations.

### Why This Matters for AI Engineering

This experience gives Rashid a production systems foundation that complements his LLM work.

He is not approaching AI only as a model/API problem. He has experience with:

- Orchestration
- APIs
- Distributed workflows
- Data dependencies
- Production failures
- Observability
- Deployment
- Operational constraints

That is relevant to AI Platform and LLM Systems engineering.

---

## 3. Agentic Pipeline Supervision / AI-Assisted Operations

### Concept

Rashid has explored an agentic supervision layer around data pipeline operations.

The design combines deterministic signals with LLM reasoning.

Possible signals include:

- Pipeline state
- File availability
- SLA timing
- Retry history
- Upstream health

The system is intended to produce explainable recommendations rather than blindly control production execution.

### Important Design Principle

The AI layer should remain controlled and auditable.

A safe architecture is:

Deterministic operational state
→ AI reasoning
→ recommendation
→ human/operator decision

rather than:

AI reasoning
→ unrestricted production execution

This project is useful when discussing AI safety, human-in-the-loop design, and agent reliability.

---

## 4. LLM Training — Outlier

Rashid worked as an LLM Trainer at Outlier.

The work involved:

- Prompt engineering
- Training large language models
- Applying artificial intelligence, statistics, and mathematics to multimodal data

This experience provides exposure to model behavior and LLM training/evaluation workflows.

---

## 5. Data Science / Computer Vision — NullClass

Rashid worked as a Data Science Intern at NullClass.

Work included:

- Age and gender detection using image-processing techniques
- NLP and machine-learning algorithms
- Model troubleshooting and optimization
- Collaboration with a remote team

This is earlier experience and should not be presented as Rashid's primary current specialization.

---

## 6. Profit Prediction — Exposys Data Labs

Rashid developed a machine-learning model intended to optimize company spending and maximize profits.

The resume reports 92% prediction accuracy using R&D, administration, and other expenditure features.

This demonstrates early experience with applied machine learning and business-oriented modeling.

---

## 7. Computer Science Expert — Chegg

Rashid worked as a Computer Science Expert, providing explanations and solutions involving:

- Python
- SQL
- C
- Data Structures and Algorithms
- Computer Science concepts

This experience strengthened technical communication and problem-solving skills.

---

# Project Positioning

For AI/LLM interviews, prioritize:

1. Dagster AI Copilot / Agentic RAG
2. Agentic pipeline supervision
3. GECS → Dagster production engineering
4. LLM training experience
5. Earlier ML/CV projects

The key story is:

**Data Engineering + Production Systems → LLM/RAG → Agentic AI → AI Platform Engineering**

