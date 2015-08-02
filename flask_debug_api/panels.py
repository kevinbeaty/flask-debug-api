import jinja2

from flask import current_app, url_for
from flask_debugtoolbar.panels import DebugPanel

template_loader = jinja2.PrefixLoader({
    'debug-api': jinja2.PackageLoader(__name__, 'templates/debug-api')
})


def _prefix():
    return current_app.config.get('DEBUG_API_PREFIX', '')


class BrowseAPIPanel(DebugPanel):
    """
    Panel that displays the API browser
    """
    name = 'DebugAPI'
    has_content = True

    def __init__(self, jinja_env, context={}):
        DebugPanel.__init__(self, jinja_env, context=context)
        self.jinja_env.loader = jinja2.ChoiceLoader([
            self.jinja_env.loader, template_loader])

    def nav_title(self):
        return 'API Browse'

    def title(self):
        return 'API Browse'

    def url(self):
        return ''

    def nav_subtitle(self):
        count = len(self.routes)
        return '%s %s' % (count, 'route' if count == 1 else 'routes')

    def process_request(self, request):
        rs = current_app.url_map.iter_rules()
        self.routes = [r for r in rs if r.rule.startswith(_prefix())]

    def content(self):
        return self.render('debug-api/routes.html', {
            'routes': self.routes,
            'prefix': _prefix(),
            'url_for': url_for
        })
