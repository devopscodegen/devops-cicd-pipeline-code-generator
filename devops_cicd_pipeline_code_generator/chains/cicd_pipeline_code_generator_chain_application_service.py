"""
PLACEHOLDER
"""

from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from .cicd_pipeline_code_generator_chain import CICDPipelineCodeGeneratorChain


class CICDPipelineCodeGeneratorChainApplicationService:
    """
    PLACEHOLDER
    """

    def __init__(
        self,
        llm: Runnable = ChatOpenAI(
            model="gpt-4o",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        ),
    ):
        self.set_llm(llm)

    def get_llm(self) -> Runnable:
        """Get llm"""
        return self.llm

    def set_llm(self, llm: Runnable = None):
        """Set llm"""
        self.llm = llm

    def create_chain(self):
        """
        PLACEHOLDER
        """
        llm = self.get_llm()
        return CICDPipelineCodeGeneratorChain(llm=llm).create_chain()

    def __str__(self):
        return self.get_llm()
