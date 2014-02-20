# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.conf.urls import patterns
from django.conf.urls import url

# Local application / specific library imports
from machina.apps.conversation import views
from machina.core.app import Application


class ConversationApp(Application):
    name = 'conversation'

    topic_view = views.TopicView

    def get_urls(self):
        urls = [
            url(r'^topic/(?P<pk>\d+)/$', self.topic_view.as_view(), name='topic'),
            url(r'^forum/(?P<forum_pk>\d+)/topic/(?P<pk>\d+)/$', self.topic_view.as_view(), name='topic'),
        ]
        return patterns('', *urls)


application = ConversationApp()