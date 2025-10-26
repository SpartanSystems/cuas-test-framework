#!/usr/bin/env python3
"""
SpartanCore Phase Workflow Integration
Links phases with SME agent assessments
"""

import json
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from sme_assessment.load_agents import AgentProfileLoader

class PhaseWorkflow:
    def __init__(self, phase_number):
        self.phase = f"phase_{phase_number}"
        self.loader = AgentProfileLoader()
        self.agents = self.loader.get_phase_agents(self.phase)
        
    def run_sme_assessment(self, test_data):
        """Run SME assessment for current phase"""
        results = {}
        
        print(f"\n=== Running {self.phase.upper()} SME Assessment ===")
        print(f"Assigned Agents: {', '.join(self.agents)}")
        
        for agent in self.agents:
            profile = self.loader.load_agent_profile(agent)
            if profile:
                print(f"\n[{agent}] Assessment:")
                # Here you would integrate with actual agent processing
                results[agent] = {
                    "status": "ready",
                    "profile_loaded": True,
                    "phase": self.phase
                }
            else:
                results[agent] = {
                    "status": "error",
                    "profile_loaded": False,
                    "error": "Profile not found"
                }
        
        return results

# Test phases 19, 20, 21
if __name__ == "__main__":
    for phase_num in [19, 20, 21]:
        workflow = PhaseWorkflow(phase_num)
        results = workflow.run_sme_assessment({"test": "data"})
        print(json.dumps(results, indent=2))
