"""
CI/CD pipeline orchestrator
"""

import enum
from enum import StrEnum
import os


class CICDPipelineOrchestrator(StrEnum):
    """
    CI/CD pipeline orchestrator
    """

    JENKINS = "jenkins"
    GITHUB_ACTIONS = "github_actions"

    @enum.property
    def info(self) -> dict:
        """
        CI/CD pipeline orchestrator information
        """
        match self:
            case CICDPipelineOrchestrator.JENKINS:
                return {
                    "description": "Jenkins",
                    "pipeline_code": {
                        "description": "declarative pipeline",
                        "file": "Jenkinsfile",
                        "directory": os.path.join("."),
                        "template": "Jenkinsfile.template",
                    },
                }
            case CICDPipelineOrchestrator.GITHUB_ACTIONS:
                return {
                    "description": "Github actions",
                    "pipeline_code": {
                        "description": "workflow configuration",
                        "file": "cicd-pipeline.yml",
                        "directory": os.path.join(".",".github","workflows"),
                        "template": "cicd-pipeline.yml.template",
                    },
                }
