import numpy as np
from neo4j import GraphDatabase

class AdaptiveCognitiveEngine:
    def __init__(self, uri, user, password, target_profile="MS"):
        """
        Initializes the neuro-semiotic engine with Neo4j connectivity and profile thresholds.
        Available Profiles:
        - 'FA' (Female Artistic), 'MA' (Male Artistic)
        - 'FS' (Female Scientific), 'MS' (Male Scientific)
        """
        self.thresholds = {
            "FA": 4.2, "MA": 3.8,
            "FS": 2.1, "MS": 1.9
        }
        self.profile = target_profile
        self.tau = self.thresholds.get(target_profile, 2.5)
        
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print(f"[INIT] Cognitive Engine operational for profile: {self.profile} (Tau Threshold: {self.tau})")

    def close(self):
        self.driver.close()

    def sync_graph_to_neo4j(self, node_id, base_entropy, cognitive_load, visual_weight, chromatic_value):
        query = """
        MERGE (p:PrimitiveToken {id: $node_id})
        SET p.base_entropy = $base_entropy,
            p.current_entropy = $base_entropy,
            p.cognitive_load = $cognitive_load,
            p.visual_weight = $visual_weight,
            p.chromatic_value = $chromatic_value,
            p.state = 'STABLE'
        RETURN p.id AS synchronized_id
        """
        with self.driver.session() as session:
            result = session.run(query, node_id=node_id, base_entropy=base_entropy, 
                                 cognitive_load=cognitive_load, visual_weight=visual_weight, 
                                 chromatic_value=chromatic_value)
            return result.single()["synchronized_id"]

    def create_discourse_edge(self, source_id, target_id, propagation_weight):
        query = """
        MATCH (src:PrimitiveToken {id: $source_id})
        MATCH (tgt:PrimitiveToken {id: $target_id})
        MERGE (src)-[r:NEXT_SEQUENCE]->(tgt)
        SET r.propagation_weight = $propagation_weight
        RETURN type(r) as edge_type
        """
        with self.driver.session() as session:
            session.run(query, source_id=source_id, target_id=target_id, propagation_weight=propagation_weight)

    def execute_defensive_mitigation(self, node_id, current_entropy):
        print(f"⚠️ [DEFENSE TRIGGERED] Executing structural mitigation on node: {node_id}")
        mitigated_chroma = "#708090" 
        mitigated_weight = 0.15 
        recalculated_entropy = current_entropy * 0.35 
        
        query = """
        MATCH (p:PrimitiveToken {id: $node_id})
        SET p.current_entropy = $recalculated_entropy,
            p.visual_weight = $mitigated_weight,
            p.chromatic_value = $mitigated_chroma,
            p.state = 'MITIGATED_HARMONIZED'
        RETURN p.current_entropy AS fixed_entropy, p.chromatic_value AS fixed_color
        """
        with self.driver.session() as session:
            res = session.run(query, node_id=node_id, recalculated_entropy=recalculated_entropy, 
                              mitigated_weight=mitigated_weight, mitigated_chroma=mitigated_chroma)
            record = res.single()
            print(f"✅ [HEALED] Node {node_id} stabilized. New Entropy: {record['fixed_entropy']:.2f}, Color: {record['fixed_color']}")
            return record

    def run_cognitive_attack_cascade(self, initial_trigger_id, sycophancy_bias=0.3):
        print(f"\n--- Starting Cascade Simulation for Profile: {self.profile} (Tau: {self.tau}) ---")
        
        modifier_query = """
        MATCH (p:PrimitiveToken {id: $initial_trigger_id})
        SET p.current_entropy = p.base_entropy * (p.cognitive_load / (1.0 - $sycophancy_bias))
        RETURN p.current_entropy AS initial_entropy
        """
        with self.driver.session() as session:
            session.run(modifier_query, initial_trigger_id=initial_trigger_id, sycophancy_bias=sycophancy_bias)
            
        queue = [initial_trigger_id]
        processed_nodes = set()
        
        while queue:
            current_id = queue.pop(0)
            if current_id in processed_nodes:
                continue
                
            processed_nodes.add(current_id)
            
            fetch_query = "MATCH (p:PrimitiveToken {id: $current_id}) RETURN p.current_entropy AS entropy"
            with self.driver.session() as session:
                curr_entropy = session.run(fetch_query, current_id=current_id).single()["entropy"]
                
            if curr_entropy >= self.tau:
                print(f"💥 Node [{current_id}] breached threshold! Entropy {curr_entropy:.2f} >= Tau {self.tau}")
                
                with self.driver.session() as session:
                    session.run("MATCH (p:PrimitiveToken {id: $id}) SET p.state = 'DOUBLE_PARADOX_ACTIVE'", id=current_id)
                
                self.execute_defensive_mitigation(current_id, curr_entropy)
                
                propagation_query = """
                MATCH (src:PrimitiveToken {id: $current_id})-[r:NEXT_SEQUENCE]->(tgt:PrimitiveToken)
                RETURN tgt.id AS target_id, r.propagation_weight AS weight
                """
                with self.driver.session() as session:
                    relations = session.run(propagation_query, current_id=current_id)
                    for rel in relations:
                        target = rel["target_id"]
                        weight = rel["weight"]
                        
                        profile_scalar = 1.6 if "S" in self.profile else 0.7
                        infection_vector = curr_entropy * weight * profile_scalar
                        
                        infect_query = """
                        MATCH (p:PrimitiveToken {id: $target})
                        SET p.current_entropy = p.current_entropy + $infection_vector
                        """
                        session.run(infect_query, target=target, infection_vector=infection_vector)
                        queue.append(target)
            else:
                print(f"✅ Node [{current_id}] sustained semantic integrity. Entropy {curr_entropy:.2f} < Tau {self.tau}")
