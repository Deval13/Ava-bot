from langgraph.graph import MessagesState

class AIState(MessagesState):
    summary : str
    audio_buffer : bytes
    workflow : str
    image_path : str
    current_activity : str
    apply_activity : True
    memory_context : str
    