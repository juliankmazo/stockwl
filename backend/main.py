#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from core.controllers import BaseController
from core.controllers import UpdateStockController


# from core.helpers import QueryHelper

# def render_str(template, **params):
#     j = jinja_env.get_template(template)
#     return j.render(params)

#########################################################################
# Handler Principal
# class Handler(webapp2.RequestHandler):

    # def write(self, *a, **kw):
    #     self.response.out.write(*a, **kw)

    # def render_str(self, template, **params):
    #     params['user'] = self.user
    #     return render_str(template, **params)

    # def render(self, template, **kw):
    #     self.write(self.render_str(template, **kw))

    # def set_secure_cookie(self, name, val):
    #     cookie_val = fns.make_secure_val(val)

    #     if self.request.get("remember")=="yes":
    #         next_month = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    #         self.response.headers.add_header('Set-Cookie','%s=%s; Path=/; expires= %s' % (name, cookie_val, next_month))
    #     else:
    #         tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    #         self.response.headers.add_header('Set-Cookie','%s=%s; Path=/; expires= %s' % (name, cookie_val, tomorrow))

    # def read_secure_cookie(self, name):
    #     cookie_val = self.request.cookies.get(name)
    #     return cookie_val and fns.check_secure_val(cookie_val)

    # def login(self, user, teacher):
    #     self.set_secure_cookie('usi', str(user.key.urlsafe()))

    # def logout(self):
    #     self.response.headers.add_header("Set-Cookie", "usi=; Path=/")

    # def initialize(self, *a, **kw):
    #     webapp2.RequestHandler.initialize(self, *a, **kw)
    #     ukey = self.read_secure_cookie("usi")
    #     self.user = ukey and ndb.Key(urlsafe=ukey).get()


class MainHandler(BaseController):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/tasks/stocksupdate', UpdateStockController),
    ('/', MainHandler)
], debug=True)
