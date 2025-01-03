from .agent_base import AgentBase

class WriteArticleValidatorAgent(AgentBase):
    def __init__(self,max_retries,verbose=True):
        super().__init__(name="WriteArticleValidatorAgent",max_retries=max_retries,verbose=verbose)

    def execute(self,topic,article):
        system_message = "You are an expert AI assistant that validates research articles"
        user_content = f"Given the topic and article ,assess whether the article comprehensivley covers the topic,
         follows a logical structure and maintains academci standards\n"
        "Provide the brief analysis and rate the article on a scale of 1 to 5 , where 5 indicates excellent quality\n\n"
        f"Topic: {topic}\n\n"
        f"Article: \n {article}\n\n"
        "Validation:"

        messages = [
            { "role": "system", "content" : system_message },
            { "role": "user",   "content" : user_content }
        ]

        validation = self.call_openai(messages,max_tokens =512)
        return validation