import sys
import asyncio
from pathlib import Path

# Add backend_api to Python path so we can import app modules
backend_dir = Path(__file__).parent.parent.parent / "apps" / "backend_api"
sys.path.insert(0, str(backend_dir))

from app.agents.ranking_agent import RankingAgent
from app.agents.base import AgentTask, AgentType

async def test_ranking_agent():
    agent = RankingAgent()
    
    # Using the first mock customer ID we seeded
    task = AgentTask(
        task_id="test-task-001",
        agent_type=AgentType.MATCHER,
        input_data={
            "customer_id": "11111111-1111-1111-1111-111111111111",
            "city": "Karachi",
            "problem_description": "My AC is leaking water heavily and stopped cooling. Need someone urgently, guests are arriving soon!"
        }
    )
    
    print("Sending test task to RankingAgent...")
    response = await agent.process(task)
    
    if response.success:
        print("\nSUCCESS! Here is the response:\n")
        import json
        print(json.dumps(response.output_data, indent=2))
    else:
        print("\nFAILED:")
        print(response.error)

if __name__ == "__main__":
    asyncio.run(test_ranking_agent())
