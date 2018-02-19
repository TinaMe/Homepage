#!/usr/bin/env pyt

import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class Vstopna(BaseHandler):
    def get(self):
        return self.render_template("vstopna.html")

class OMeni(BaseHandler):
    def get(self):
        return self.render_template("jaz.html")


class MojiProjekti(BaseHandler):
    def get(self):
        return self.render_template("projekti.html")


class Blog(BaseHandler):
    def get(self):
        return self.render_template("blog.html")


class Kontakt(BaseHandler):
    def get(self):
        return self.render_template("kontakt.html")



app = webapp2.WSGIApplication([
    webapp2.Route('/', Vstopna),
    webapp2.Route('/jaz', OMeni),
    webapp2.Route('/projekti', MojiProjekti),
    webapp2.Route('/blog', Blog),
    webapp2.Route('/kontakt', Kontakt),
], debug=True)