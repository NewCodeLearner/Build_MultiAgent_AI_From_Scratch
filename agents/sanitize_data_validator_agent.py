from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent",max_retries=max_retries,verbose=verbose)

    def execute(self,original_data,sanitized_data):
        system_message = "You are an expert AI assistant that validates the sanitization of medical data\
        by checking the removal of PHI"
        user_content = f"Given the original and Sanitized data ,verify that all PHI has been remvoed.\n"
        "Provide the brief analysis and rate the sanitized process on a scale of 1 to 5 , where 5 indicates excellent quality\n\n"
        f"Original Data: {original_data}\n\n"
        f"Sanitized Data: \n {sanitized_data}\n\n"
        "Validation:"

        messages = [
            { "role": "system", "content" : system_message },
            { "role": "user",   "content" : user_content }
        ]

        validation = self.call_openai(messages,max_tokens =512)
        return validation