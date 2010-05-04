# -*- coding: utf-8 -*-
def current_url(request):
	'''
		Include this into Django\'s TEMPLATE_CONTEXT_PROCESSORS tuple to automatically include
		the path component from the HttpRequest in any RequestContext as current_url.
	'''
	return {'current_url': request.path}
