"""
This module exposes the chain using langserve fastapi server
"""

import logging
import os
from devops_cicd_pipeline_code_generator.chains import (
    CICDPipelineCodeGeneratorChainResource,
)

loglevel = os.getenv("DEVOPS_CICD_PIPELINE_CODE_GENERATOR_LOG_LEVEL", "WARNING")
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError(f"Invalid log level: {loglevel}")
logging.getLogger().setLevel(level=numeric_level)
logger = logging.getLogger(__name__)

app = CICDPipelineCodeGeneratorChainResource().create_fastapi_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
