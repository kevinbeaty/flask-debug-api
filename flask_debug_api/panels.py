import jinja2

from flask import current_app, url_for, Markup
from flask_debugtoolbar.panels import DebugPanel
from werkzeug.routing import parse_rule

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
        self.variables = {}

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
        for r in self.routes:
            self.variables[r.rule] = self.url_builder(r)

    def content(self):
        return self.render('debug-api/routes.html', {
            'routes': self.routes,
            'prefix': _prefix(),
            'url_for': url_for,
            'variables': self.variables
        })

    def url_builder(self, route):
        parts = []
        for (converter, arguments, variable) in parse_rule(route.rule):
            parts.append({'variable': converter is not None, 'text': variable})

        content = self.render('debug-api/url-builder.html', {
            'route': route,
            'parts': parts,
            'url_for': url_for
        })
        return Markup(content)
