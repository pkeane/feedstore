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

import wsgiref.handlers
import atomlib
import httplib2

from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
      #url = 'https://twitter.com/statuses/friends_timeline.atom'
      url = 'http://www.laits.utexas.edu/dasebeta/collections.atom'
      user = 'pkeane'
      passwd = 'xxx123'
      feed = atomlib.Atom.retrieve(url,user,passwd)
      out = """
      <html><head><title>tweets</title>
      <style type="text/css">
      body {
      font-size: 10px;
      font-family: verdana, arial, sans;
      width: 40%;
      margin-left: 30px;
      }
      dd {
      font-weight:bold;
      margin-bottom: 12px;
      }
      dt {
      color: #666;
      font-weight: bold;
      }
      </style>
      </head><body><dl>
      """
      for entry in feed.entries:
          for auth in entry.authors:
              out += '<dt>'+auth['name']+'</dt>'
          out += '<dd>'+entry.title+'</dd>'
      out += '</dl></body></html>'
      self.response.out.write(out)


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
    main()
