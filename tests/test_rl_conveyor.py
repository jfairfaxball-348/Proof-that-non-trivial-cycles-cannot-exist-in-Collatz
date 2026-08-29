import json
import re
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import rl_catalog  # noqa: E402
import rl_conveyor  # noqa: E402


class ConveyorKnowledgeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sessions = rl_catalog.load_jsonl(
            ROOT / "knowledge" / "session_catalog.jsonl", rl_catalog.SESSION_FORMAT
        )
        cls.results = rl_catalog.load_jsonl(
            ROOT / "knowledge" / "result_catalog.jsonl", rl_catalog.RESULT_FORMAT
        )

    def test_current_rl_comes_from_unique_target(self):
        state = rl_conveyor.state()
        target_number = int(re.search(r"RL(\d+)", Path(state["target"]).name).group(1))
        self.assertEqual(state["current_rl"], target_number)
        self.assertEqual(state["handover_generation"], 175)

    def test_every_physical_session_container_is_catalogued(self):
        physical = {path.as_posix() for path in (ROOT / "sessions").glob("RL*") if path.is_dir()}
        physical = {str(Path("sessions") / Path(path).name) for path in physical}
        indexed = {record["container_path"] for record in self.sessions}
        self.assertEqual(physical, indexed)

    def test_catalogue_ids_and_source_pointers_are_valid(self):
        self.assertEqual(len(self.sessions), len({record["generation_id"] for record in self.sessions}))
        self.assertEqual(len(self.results), len({record["record_id"] for record in self.results}))
        for record in self.sessions:
            for key, values in record.items():
                if key.endswith("_paths") or key in {"generation_paths", "certificate_roots"}:
                    for value in values:
                        self.assertTrue((ROOT / value).exists(), (record["generation_id"], key, value))
        for record in self.results:
            path = ROOT / record["source_path"]
            self.assertTrue(path.is_file(), record["source_path"])
            self.assertGreaterEqual(record["source_line_start"], 1)
            self.assertGreaterEqual(record["source_line_end"], record["source_line_start"])

    def test_modern_container_label_is_not_completed_rl(self):
        result = rl_catalog.query_sessions(ROOT, 174)
        completed_paths = {
            record["container_path"] for record in result["completed_generation_records"]
        }
        self.assertIn("sessions/RL175", completed_paths)
        self.assertTrue(any(
            path.endswith("RL174_SESSION_STATE_AND_RL175_KICKOFF_2026-08-29.md")
            for record in result["completed_generation_records"]
            for path in record["session_state_handover_paths"]
        ))

    def test_duplicate_packaging_variants_remain_visible(self):
        result = rl_catalog.query_sessions(ROOT, 162)
        containers = {
            record["container_path"] for record in result["completed_generation_records"]
        }
        self.assertTrue({"sessions/RL162", "sessions/RL163"}.issubset(containers))

    def test_embedded_legacy_rl_has_locator_without_inferred_role(self):
        result = rl_catalog.query_sessions(ROOT, 3)
        self.assertTrue(result["embedded_locator_records"])
        self.assertTrue(all(
            record["completed_rl"] is None and record["incoming_rl"] is None
            for record in result["embedded_locator_records"]
        ))

    def test_named_current_result_has_verbatim_classification_and_source(self):
        result = rl_catalog.query_results(ROOT, "RL175.4", 5)
        self.assertEqual(result["match_count"], 1)
        record = result["matches"][0]
        self.assertEqual(record["source_scope"], "authoritative")
        self.assertEqual(record["recorded_classification"], "New proved analytic mathematics")
        self.assertTrue(record["source_path"].endswith("RL175_CERTIFIED_FACTS_AND_PROOF_LEDGER.md"))

    def test_explicit_correction_is_returned_without_adjudication(self):
        result = rl_catalog.query_results(ROOT, "physical-functional identification", 10)
        self.assertTrue(result["correction_or_demotion_matches"])
        self.assertIn("never adjudicated", result["status_policy"])

    def test_table_pipe_does_not_shift_verbatim_classification(self):
        result = rl_catalog.query_results(ROOT, "F4", 5)
        self.assertEqual(result["matches"][0]["recorded_classification"], "analytic")
        self.assertFalse(result["matches"][0]["is_correction_or_demotion_record"])

    def test_result_query_rejects_empty_normalised_input_and_limit(self):
        with self.assertRaises(rl_catalog.CatalogError):
            rl_catalog.query_results(ROOT, "---", 5)
        with self.assertRaises(rl_catalog.CatalogError):
            rl_catalog.query_results(ROOT, "F4", 0)

    def test_main_report_is_not_misclassified_as_correction_ledger(self):
        result = rl_catalog.query_sessions(ROOT, 174)
        records = result["completed_generation_records"]
        paths = [path for record in records for path in record["correction_demotion_ledger_paths"]]
        self.assertTrue(paths)
        self.assertTrue(all("LEDGER" in Path(path).name.upper() for path in paths))

    def test_root_start_here_is_timeless(self):
        text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\bRL\d+\b", text))

    def test_startup_reads_no_historical_surface(self):
        startup = rl_conveyor.startup_state()
        self.assertTrue(startup["target"].startswith("authoritative/"))
        self.assertFalse(any(
            path.startswith(("sessions/", "Archive/")) for path in startup["minimal_read_order"]
        ))
        for command in startup["required_commands"][2:]:
            script = command.split()[1]
            self.assertTrue((ROOT / script).is_file(), command)

    def test_checkpoint_initialization_refuses_dirty_repository(self):
        dirty_state = {"current_rl": 176, "working_tree_clean": False}
        with patch.object(rl_conveyor, "state", return_value=dirty_state):
            with self.assertRaises(rl_conveyor.Failure):
                rl_conveyor.cmd_checkpoint(SimpleNamespace(rl=None, target=None))

    def test_generated_indexes_are_current(self):
        validation = rl_catalog.validate_indexes(ROOT)
        self.assertTrue(validation["current"], json.dumps(validation["mismatches"], indent=2))


if __name__ == "__main__":
    unittest.main()
