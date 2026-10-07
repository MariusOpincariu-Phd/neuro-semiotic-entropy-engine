# Neuro-Semiotic Entropy Modulation Engine

An advanced doctoral research prototype bridging Information Theory, Machine Learning, and Graph Topologies to simulate and adaptively mitigate semantic complexity collapses in real-time.

## 📐 Architectural Overview

This system tracks and manages cognitive load and semantic degradation across complex networks using a dual-layer approach:
1. **Behavioral Inference Layer:** A Scikit-Learn `RandomForestClassifier` that extracts dynamic phenotype classifications (`FA`, `MA`, `FS`, `MS`) from real-time telemetry inputs (scroll velocity, fixation pauses, and compliance bias).
2. **Topological Graph Layer:** An official Neo4j Bolt execution engine that tracks sequence paths and models information degradation cascades based on unique mathematical thresholds (τ).

When nodes breach their critical entropy constraints (τ), the engine dynamically triggers self-healing circuit breakers—mutating visual layout variables (slashing local Shannon entropy by 65%, locking visibility weight to `0.15`, and shifting chromatic rendering to slate gray `#708090`) to stabilize structural network integrity.

## 📂 Project Structure

* `cognitive_cyberengine.py` - Core network configuration, Cypher sequence operations, and self-healing algorithms.
* `app.py` - Production-ready FastAPI implementation housing the ML behavioral classifier.
* `seed_db.py` - Autonomous setup utility to map sample semiotic nodes into Neo4j instances.
* `requirements.txt` - Python project dependencies.

## 🚀 Quick Start & Deployment

### 1. Prerequisites
Ensure you have a running instance of **Neo4j** (local instance or Neo4j AuraDB).

### 2. Environment Configuration
Configure your local environment variables before starting the cluster:
```bash
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASS="your_secure_password"
```

### 3. Installation
Install the project core dependencies:
```bash
pip install -r requirements.txt
```

### 4. Graph Initialization
Seed the target multi-node topology structure into your active database instance:
```bash
python seed_db.py
```

### 5. Launch the REST API
Start the FastAPI local orchestration server using Uvicorn:
```bash
python app.py
```
The endpoint will be available at `http://127.0.0.1:8000`. You can execute the cascade pipeline via POST requests to `/api/v1/modulate`.

## 📜 Academic Research & Compliance
This software module serves as an execution prototype for multi-level semiosis evaluation and automated human-AI behavioral alignment frameworks. 
