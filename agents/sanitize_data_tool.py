from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="SanitizeDataTool",max_retries=max_retries,verbose=verbose)

    def execute(self,medical_data):
        messages =[
            {
                "role" : "system",
                "content":"You are an AI assistant that Sanitizes the medical data by removing protected health information(PHI)"
            },
            {
                "role": "user",
                "content" : (
                    "Rrmove all PHI from the following medical data:\n\n"
                    f"{medical_data}\n\nSanitized Data:"

                )
            }

        ]
        sanitized_data = self.call_openai(messages,max_tokens=300)
        return sanitized_data
