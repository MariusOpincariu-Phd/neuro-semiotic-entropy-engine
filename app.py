import os
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from sklearn.ensemble import RandomForestClassifier
from cognitive_cyberengine import AdaptiveCognitiveEngine

app = FastAPI(
    title="Neuro-Semiotic Entropy Modulation API",
    version="1.0.0",
    description="REST API providing real-time cognitive profile classification and topological entropy self-healing cascades."
)

# Production security fix: Ensure environment variables are mapped explicitly without raw hardcoded fallbacks
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS")

if not NEO4J_PASS:
    print("⚠️ WARNING: NEO4J_PASS environment variable is missing. Ensure your local environment configuration is set.")

# =========================================================================
# MODULE 4 (API MODULE 1): MACHINE LEARNING BEHAVIORAL CLASSIFIER
# =========================================================================
class CognitiveProfileClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.profile_mapping = {0: "FA", 1: "MA", 2: "FS", 3: "MS"}
        self._train_mock_classifier()

    def _train_mock_classifier(self):
        X_train = np.array([
            [1200.5, 0.12, 0.95],  # FA
            [1400.2, 0.15, 0.85],  # MA
            [350.8,  0.89, 0.10],  # FS
            [210.3,  1.45, 0.05]   # MS
        ])
        y_train = np.array([0, 1, 2, 3])
        self.model.fit(X_train, y_train)

    def predict_receptor_profile(self, scroll_velocity: float, fixation_delta: float, sycophancy_bias: float) -> str:
        input_vector = np.array([[scroll_velocity, fixation_delta, sycophancy_bias]])
        prediction_id = self.model.predict(input_vector)
        return self.profile_mapping[int(prediction_id[0])]

classifier_instance = CognitiveProfileClassifier()

class TelemetryPayload(BaseModel):
    scroll_velocity: float  
    fixation_delta: float   
    sycophancy_bias: float  

class EvaluationRequest(BaseModel):
    telemetry: TelemetryPayload
    trigger_node_id: str
    sycophancy_noise: float = 0.25

@app.get("/")
def read_root():
    return {
        "status": "ONLINE",
        "framework": "Neuro-Semiotic Fluid Dynamics",
        "protected_intellectual_property": "Doctoral Research Core Demo"
    }

@app.post("/api/v1/modulate", response_model=Dict[str, Any])
def execute_entropy_modulation_pipeline(payload: EvaluationRequest):
    """
    POST API Endpoint that runs telemetry classification and triggers the graph self-healing cascade.
    """
    try:
        predicted_profile = classifier_instance.predict_receptor_profile(
            scroll_velocity=payload.telemetry.scroll_velocity,
            fixation_delta=payload.telemetry.fixation_delta,
            sycophancy_bias=payload.telemetry.sycophancy_bias
        )
        
        engine = AdaptiveCognitiveEngine(
            uri=NEO4J_URI,
            user=NEO4J_USER,
            password=NEO4J_PASS,
            target_profile=predicted_profile
        )
        
        # Stability verification: Validate target node existence to protect execution flow
        with engine.driver.session() as session:
            check_node = session.run("MATCH (p:PrimitiveToken {id: $id}) RETURN p", id=payload.trigger_node_id)
            if not check_node.single():
                raise HTTPException(
                    status_code=400, 
                    detail=f"Node '{payload.trigger_node_id}' does not exist in Neo4j. Please verify your graph topology or seed nodes first."
                )

        print(f"[API] Intercepted request. ML Profile Prediction: {predicted_profile}. Launching graph execution.")
        engine.run_cognitive_attack_cascade(
            initial_trigger_id=payload.trigger_node_id,
            sycophancy_bias=payload.sycophancy_noise
        )
        
        engine.close()
        
        return {
            "success": True,
            "inferred_phenotype": predicted_profile,
            "applied_tau_threshold": engine.tau,
            "execution_status": "COMPLETED_WITH_DEFENSIVE_HEALING_CHECKS"
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph database connectivity or execution breakdown: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    print("[API SERVICE] Starting local Uvicorn development server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
