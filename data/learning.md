# Rashid Husain — Learning & Growth Profile

> Purpose: Describe what Rashid is learning, why he is learning it, and how it connects to his target AI engineering roles.

## Current Career Direction

Rashid is moving deliberately toward:

- AI Engineer
- Applied AI Engineer
- LLM Engineer
- Agentic AI Engineer
- AI Platform Engineer
- LLM/AI Systems Engineer

The goal is not simply to learn more frameworks. The goal is to become capable of designing and operating production AI systems.

---

# Current Learning Priorities

## 1. LLM Fundamentals

### Topics

- Tokenization
- Context windows
- Transformer architecture
- Attention
- Embeddings
- Model limitations
- Hallucination mechanisms
- Inference basics
- Sampling
- Temperature
- Context engineering

### Why

A strong AI engineer should understand what the model is doing rather than treating an LLM API as a black box.

---

# 2. Retrieval Engineering

### Topics

- Dense embeddings
- Cosine similarity
- Approximate nearest-neighbor search
- HNSW
- BM25
- Hybrid retrieval
- Reciprocal Rank Fusion
- Cross-Encoder re-ranking
- Metadata filtering
- Query rewriting
- Query decomposition
- Retrieval evaluation

### Why

Retrieval quality is one of the most important determinants of RAG quality.

For codebase RAG, exact identifiers and semantic meaning both matter, making hybrid retrieval especially relevant.

---

# 3. RAG Evaluation

### Topics

- Golden datasets
- Precision@K
- Recall@K
- MRR
- NDCG
- Context relevance
- Groundedness
- Faithfulness
- Answer correctness
- Hallucination detection
- Regression testing
- Evaluation data generation
- Human evaluation

### Goal

Move from:

"the answer looks good"

to:

"we can measure whether the system improved."

---

# 4. Agentic Systems

### Topics

- State machines
- LangGraph
- Tool calling
- Structured outputs
- Conditional routing
- Retry strategies
- Query rewriting
- Planning
- Memory
- Human-in-the-loop
- Agent safety
- Failure recovery
- Agent evaluation

### Principle

An agent should not be autonomous merely for the sake of being autonomous. Every additional decision loop should solve a real problem.

---

# 5. LLM Observability

### Tools/Concepts

- LangSmith
- Tracing
- Latency
- Token usage
- Cost tracking
- Retrieval traces
- Failure analysis
- Prompt/version tracking
- Evaluation monitoring

### Goal

Understand why an AI system behaved a certain way.

---

# 6. Production AI Infrastructure

### Topics

- FastAPI
- Docker
- AWS
- CI/CD
- Persistent storage
- API security
- Secrets management
- Logging
- Metrics
- Monitoring
- Health checks
- Rate limiting
- Caching
- Failure recovery

### Goal

Turn an AI prototype into a service that can be operated reliably.

---

# 7. Model Adaptation

Future learning area:

- Fine-tuning
- LoRA
- QLoRA
- PEFT
- Quantization
- Dataset preparation
- Evaluation before/after tuning

This should come after strong fundamentals in RAG, retrieval, evaluation, and production systems.

---

# 8. Hugging Face

Rashid should understand the parts that are directly useful for LLM engineering:

- Transformers
- Tokenizers
- Model loading
- Pipelines
- Text-generation workflows
- Embedding models
- Fine-tuning interfaces
- PEFT ecosystem
- Model configuration

He does not need to learn every Hugging Face feature simply to list Hugging Face on a resume.

---

# 9. Framework Strategy

### LangGraph

Use when the system needs explicit stateful/conditional agent workflows.

### LangChain

Understand the ecosystem and useful components, but do not depend on it blindly. Core concepts should remain understandable without the framework.

### FastAPI

Important because AI systems need reliable service interfaces.

### LangSmith

Useful for tracing, debugging, evaluation, and LLM observability.

### ChromaDB

Useful for learning and for the current project, while understanding the trade-offs against production vector/database options.

---

# Interview Learning Priorities

For AI/LLM/Agentic interviews, Rashid should be able to explain:

1. Transformer fundamentals
2. Embeddings
3. BM25
4. Dense retrieval
5. Hybrid retrieval
6. RRF
7. Cross-Encoder vs bi-encoder
8. Chunking trade-offs
9. RAG failure modes
10. Evaluation methodology
11. Hallucination mitigation
12. Agent state management
13. Tool calling
14. Agent reliability
15. LLM observability
16. API/system design
17. Docker/cloud deployment
18. Cost and latency optimization

---

# Learning Philosophy

Rashid prefers depth over tool collecting.

A technology should be learned because it solves a real engineering problem.

The learning loop is:

Concept
→ implement from fundamentals
→ integrate into production-style project
→ evaluate
→ observe failures
→ optimize
→ explain trade-offs in an interview

---

# Long-Term Direction

The intended progression is:

Data Engineering & Orchestration
→ Production Systems
→ RAG & Retrieval
→ Agentic Systems
→ Evaluation & Reliability
→ AI Platform Engineering
→ Advanced LLM Systems

