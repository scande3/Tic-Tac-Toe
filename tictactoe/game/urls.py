from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tictactoe.game.views',
        url(r'^$', 'playGame', name='playGame'),
    )