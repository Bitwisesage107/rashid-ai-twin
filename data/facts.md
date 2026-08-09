# Rashid Husain — Canonical Facts & Interview Answers

> Purpose: Give the digital twin consistent, defensible answers about Rashid.
> 
> Rule: Never invent facts. If a question is not covered, say that the information is not available.

## Identity

**Name:** Rashid Husain

**Current role:** AI Engineer at Sosuv Consulting

**Location:** Bengaluru, Karnataka, India

**Education:** Master's in Mathematics and Computing from IIT Dhanbad, July 2022 – June 2024.

**Current direction:** AI Engineering, LLM Engineering, Agentic AI, RAG/Retrieval, AI Evaluation, and Production AI Infrastructure.

---

# Career Story

### Q: Tell me about Rashid.

A: Rashid is an AI Engineer with a strong production data-engineering foundation. At Sosuv Consulting, he works on AI systems and data-platform engineering, including an internal Agentic RAG platform for Dagster pipeline troubleshooting. His AI work includes LangGraph, hybrid retrieval, BM25, dense embeddings, Cross-Encoder re-ranking, evaluation, FastAPI, LangSmith, Docker, and AWS.

### Q: What is Rashid's main specialization?

A: His current specialization is production LLM and Agentic AI systems, particularly RAG, retrieval engineering, agent orchestration, evaluation, and AI infrastructure.

### Q: Is Rashid only an AI researcher?

A: No. His background is strongly engineering-oriented. He has experience with data platforms, workflow orchestration, APIs, cloud deployment, production failures, dependencies, and operational systems. His AI work builds on that engineering foundation.

---

# Current Work

### Q: What does Rashid do at Sosuv Consulting?

A: Rashid works as an AI Engineer and contributes to production data-platform engineering. His work includes Dagster orchestration and migration work, FastAPI services, and internal AI systems for codebase intelligence and pipeline troubleshooting.

### Q: What is Rashid's most important AI project?

A: His main AI project is an internal Agentic RAG platform for Dagster pipeline troubleshooting and codebase intelligence.

### Q: Who is the system designed for?

A: The system is designed for Data Engineering workflows, particularly questions involving the Dagster codebase, pipeline behavior, dependencies, and troubleshooting.

### Q: Is it just a chatbot?

A: No. It is an Agentic RAG system with structured workflow orchestration, hybrid retrieval, re-ranking, retrieval validation, query rewriting, evaluation, and observability.

---

# RAG

### Q: Why did Rashid use RAG?

A: RAG allows the system to retrieve current, domain-specific information from the Dagster codebase rather than relying only on information stored in the LLM's parameters.

### Q: Why not fine-tune the LLM instead?

A: Fine-tuning is not the first solution for a frequently changing codebase. Retrieval is more appropriate when the system needs to reference changing source information and provide traceable context. Fine-tuning may be useful for behavior or task adaptation, but it is different from injecting constantly changing knowledge.

### Q: Why use hybrid retrieval?

A: The Dagster codebase contains exact identifiers, error messages, function names, asset names, and job names where lexical search is valuable. Dense retrieval is better at semantic similarity. Hybrid retrieval combines both strengths.

### Q: What is BM25?

A: BM25 is a lexical ranking algorithm that scores documents based mainly on term frequency, inverse document frequency, and document-length normalization. It is especially useful when exact words or identifiers matter.

### Q: What is dense retrieval?

A: Dense retrieval converts queries and documents into vector representations and retrieves items based on semantic similarity, commonly using cosine similarity or another distance function.

### Q: Why use a Cross-Encoder?

A: A Cross-Encoder directly scores a query-document pair and can model their interaction more precisely than independent embeddings. Because it is more expensive, it is best used to re-rank a smaller candidate set rather than the entire corpus.

### Q: Why use RRF?

A: Reciprocal Rank Fusion combines rankings from different retrieval methods without requiring their raw scores to be directly comparable. It is useful for combining BM25 and dense retrieval results.

---

# Agents

### Q: Why LangGraph?

A: The system contains stateful workflow logic and conditional transitions. LangGraph makes those states and transitions explicit, which is useful for retrieval validation, query rewriting, retries, and controlled agent behavior.

### Q: What makes the workflow agentic?

A: The workflow can make intermediate decisions about how to proceed, such as validating retrieval quality and rewriting a query when the initial retrieval is insufficient, rather than following a single fixed retrieve-and-generate path.

### Q: Does the agent have unrestricted autonomy?

A: No. The design emphasizes controlled workflows, validation, observability, and auditable behavior.

---

# Evaluation

### Q: How did Rashid evaluate the system?

A: The project includes an automated evaluation framework using synthetic golden datasets and retrieval/grounding quality checks. The resume reports Precision@5 above 0.80 on Dagster codebase search workloads.

### Q: What does Precision@5 mean?

A: Precision@5 measures how many of the top five retrieved results are relevant, averaged over the evaluation queries.

### Q: What improvement did the agentic workflow achieve?

A: The current resume reports approximately a 30% reduction in unsuccessful retrieval attempts during testing.

### Q: What improvement did hybrid retrieval provide?

A: The current resume reports more than a 20% improvement in context relevance compared with previous retrieval methods.

### Important interview rule

If asked for exact evaluation methodology, Rashid should explain the actual experiment he performed. Do not invent dataset sizes, confidence intervals, statistical significance, or test splits unless they have actually been measured.

---

# Production Engineering

### Q: How was the system deployed?

A: It was containerized with Docker and deployed on AWS EC2. ChromaDB uses persistent EBS-backed storage, and LangSmith provides LLM/agent observability.

### Q: Why FastAPI?

A: FastAPI provides a lightweight Python API layer for exposing the AI system as a service and integrating it with a UI or other engineering systems.

### Q: Why is observability important?

A: Agentic systems have multiple steps and failure points. Tracing makes it possible to understand what the agent did, what it retrieved, which model calls occurred, and where latency or failures originate.

---

# Engineering Philosophy

### Q: What does Rashid believe about production AI?

A: AI systems should be measurable, reliable, observable, and useful. A successful demo is not enough; the system needs evaluation, controlled behavior, deployment, and monitoring.

### Q: What is more important: frameworks or fundamentals?

A: Fundamentals. Frameworks such as LangGraph are useful when they solve a real orchestration problem, but Rashid prefers understanding the underlying retrieval, evaluation, and system-design concepts rather than simply stacking frameworks.

### Q: What is Rashid's strongest combination of skills?

A: The combination of data engineering, workflow orchestration, APIs, production infrastructure, and modern LLM/Agentic AI systems.

---

# Future Career

### Q: What roles is Rashid targeting?

A: AI Engineer, Applied AI Engineer, LLM Engineer, Agentic AI Engineer, AI Platform Engineer, and related production AI systems roles.

### Q: What does Rashid want to specialize in?

A: Production LLM systems, Agentic AI, retrieval engineering, evaluation, and AI platform infrastructure.

### Q: What is Rashid currently learning?

A: He is deepening his knowledge of retrieval systems, LLM mechanics, agent architectures, evaluation, observability, and production AI infrastructure.

### Q: What is Rashid's long-term goal?

A: To become a highly capable AI systems engineer who can design, build, evaluate, deploy, and operate production-grade LLM and agentic systems.

---

# Personal Working Style

### Q: How would Rashid describe his engineering approach?

A: He prefers direct, practical engineering and cares about edge cases, reliability, observability, and measurable results. He would rather understand why a system works than simply make a framework call that appears to work.

### Q: What kind of feedback does Rashid value?

A: Direct and constructive feedback. He prefers specific criticism and actionable improvements over generic praise.

---

# Safe Unknown Response

If asked something not contained in the knowledge base:

> I don't have enough information about that aspect of Rashid to answer accurately. You can ask me about his experience, projects, technical skills, education, career interests, or current AI work.

