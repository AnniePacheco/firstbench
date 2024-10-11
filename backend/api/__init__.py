# import all the views to satisfy Connexion's MethodView resolver
# otherwise connexion will throw "TypeError: 'module' object is not callable"
from .ResourcesView import ResourcesView
from .UsersView import UsersView
from .PersonasView import PersonasView
from .RagIndexingView import RagIndexingView
from .MessagesView import MessagesView
from .ConversationsView import ConversationsView
from .VoicesFacesView import VoicesFacesView
from .OcrIndexingView import OcrIndexingView