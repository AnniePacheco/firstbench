from .ResourcesManager import ResourcesManager
from .UsersManager import UsersManager
from .PersonasManager import PersonasManager
from .RagManager import RagManager
from .MessagesManager import MessagesManager
from .ConversationsManager import ConversationsManager
from .VoicesFacesManager import VoicesFacesManager
from .OcrIndexingManager import OcrIndexingManager

# List of manager classes
manager_classes = [    
    ResourcesManager,
    UsersManager,
    PersonasManager,
    RagManager,
    MessagesManager,
    ConversationsManager,
    VoicesFacesManager,
    OcrIndexingManager
]

# Initialize the managers dynamically
managers = {cls.__name__.lower(): cls() for cls in manager_classes}

# Expose the initialized managers for easy access as e.g. backend.managers.managers['abilitiesmanager']
__all__ = ['managers'] + list(managers.keys())
