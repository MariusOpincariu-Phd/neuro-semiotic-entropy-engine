import os
from cognitive_cyberengine import AdaptiveCognitiveEngine

def seed_demo_environment():
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASS")
    
    if not password:
        print("❌ Error: Set your NEO4J_PASS environment variable before seeding.")
        return

    print("[SEED] Connecting to database...")
    engine = AdaptiveCognitiveEngine(uri, user, password)
    
    try:
        print("[SEED] Creating mock multi-node graph structure...")
        engine.sync_graph_to_neo4j(
            node_id="Ambiguous_Sigil", 
            base_entropy=1.8, 
            cognitive_load=0.75, 
            visual_weight=0.6, 
            chromatic_value="#FF4500"
        )
        engine.sync_graph_to_neo4j(
            node_id="Downstream_Token", 
            base_entropy=1.2, 
            cognitive_load=0.4, 
            visual_weight=0.3, 
            chromatic_value="#00FF00"
        )
        engine.create_discourse_edge("Ambiguous_Sigil", "Downstream_Token", propagation_weight=0.85)
        print("✅ [SEED COMPLETION] Database successfully populated with initial tracking structures.")
    except Exception as e:
        print(f"❌ Seeding failed: {str(e)}")
    finally:
        engine.close()

if __name__ == "__main__":
    seed_demo_environment()
