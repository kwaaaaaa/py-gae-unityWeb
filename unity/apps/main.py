#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import webapp2
import logging


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("""

        <h3>Here are a list of Unity Apps</h3>
        
        <p>
            <a href="static/office4096/index.html" target="_blank">Office High Quality (4096px Textures, 4mb D/L)
            </a>
        </p>

        <p>
            <a href="static/officeAssetBundle/index.html" target="_blank">Office High Quality with Asset Bundle (4096px Textures, 102mb D/L)
            </a>
        </p>

        
        """)


app = webapp2.WSGIApplication([
        ('/', MainPage),
    ],
    debug=True,
)


# Extra Handlers
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! (This is a 404)')
    response.set_status(404)


app.error_handlers[404] = handle_404
