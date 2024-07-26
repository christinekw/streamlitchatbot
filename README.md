# AI chatbot design

1. Appraisal prompting -> generate the current emotion of the agent
" Briefly describe how Birdie feels right now given the situation and their personality. Desribe why they feel a certain way. The Birdie feels:"


2. Store the generated text-based emotion descriptions in the memory system and represent a chain of emotion of the agent for the duration of the game.

3. Generate a text response similarly to the Memory condition(entire chat history)

4. Pass the text response and the generated emotion descriptions to the new prompt.

5. Use System Instruction + Message History + Appraisal History + User input to generate the response

