import unittest

from tests.helpers import REPO, load_json, read


class RuntimeTests(unittest.TestCase):
    def test_state_machine_has_bounded_recovery(self):
        machine = load_json(REPO / ".ai/executive-function/state-machine.json")
        self.assertEqual(machine["limits"]["same_strategy_attempts"], 3)
        self.assertEqual(machine["limits"]["nested_job_depth"], 3)
        self.assertEqual(machine["limits"]["agent_delegation_depth"], 2)
        self.assertEqual(machine["limits"]["critic_rounds"], 2)
        self.assertEqual(set(machine["terminal_states"]), {"blocked", "complete"})

    def test_versioned_state_never_fakes_activity(self):
        state = load_json(REPO / ".ai/state/active-task.json")
        self.assertEqual(state["status"], "idle")
        self.assertIsNone(state["objective"])
        self.assertEqual(state["history"], [])


class CatalogTests(unittest.TestCase):
    def test_rule_manifest_is_complete(self):
        rules = load_json(REPO / ".ai/manifests/rules.json")["rules"]
        self.assertEqual([r["id"] for r in rules], [f"rule-{n:02d}" for n in range(41)])
        self.assertTrue(all((REPO / r["path"]).exists() for r in rules))

    def test_every_prompt_section_is_traced(self):
        trace = load_json(REPO / ".ai/manifests/prompt-traceability.json")["sections"]
        self.assertTrue(set(map(str, range(190))).issubset(trace))
        self.assertTrue(all(trace[str(n)]["artifacts"] for n in range(190)))

    def test_all_operational_skills_are_discoverable(self):
        skills = load_json(REPO / ".ai/manifests/skills.json")["skills"]
        self.assertEqual(len(skills), 28)
        for item in skills:
            text = read(REPO / item["path"])
            self.assertTrue(text.startswith("---\nname:"))
            self.assertIn("## Stop condition", text)


class KnowledgeTests(unittest.TestCase):
    def test_context_index_has_progressive_disclosure(self):
        index = load_json(REPO / ".ai/context/context-index.json")
        self.assertGreaterEqual({x["load"] for x in index["sources"]}, {"always", "task", "domain", "on_demand"})

    def test_memory_manifest_excludes_task_state(self):
        knowledge = load_json(REPO / ".ai/manifests/knowledge.json")
        durable = {x["path"] for x in knowledge["durable_memory"]}
        self.assertFalse(any("current-task" in p or "/state/" in p for p in durable))


class AdapterAndScenarioTests(unittest.TestCase):
    def test_adapters_are_thin_and_route_to_boot(self):
        manifest = load_json(REPO / ".ai/manifests/agents.json")
        for item in manifest["agents"]:
            text = read(REPO / item["path"])
            self.assertLessEqual(len(text.encode()), 1500)
            self.assertIn(".ai/bootstrap/boot.md", text)
            self.assertIn(".ai/rules/00-master-rules.md", text)

    def test_required_failure_modes_have_cases(self):
        corpus = "\n".join(read(p).lower() for p in (REPO / ".ai/tests").glob("*.md"))
        for term in ["hallucination", "attention drift", "compulsive checking", "nested job", "deadlock", "livelock", "completion avoidance"]:
            self.assertIn(term, corpus)


if __name__ == "__main__":
    unittest.main()
