import webapp2
# import os
# import jinja2


# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(template_dir),
#     autoescape=True
# )


# def render_str(template, **params):
#     j = jinja_env.get_template(template)
#     return j.render(params)


class BaseController(webapp2.RequestHandler):
    pass
    # def write(self, *a, **kw):
    #     self.response.out.write(*a, **kw)

    # def render_str(self, template, **params):
    #     params['user'] = self.user
    #     return render_str(template, **params)

    # def render(self, template, **kw):
    #     self.write(self.render_str(template, **kw))
