import requests
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


class RebootLauncher(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, _, extention):
        url = extention.preferences['url']
        r = requests.get(url=url)
        r.close()
        return HideWindowAction()


if __name__ == '__main__':
    RebootLauncher().run()
