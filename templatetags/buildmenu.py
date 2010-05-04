# -*- coding: utf-8 -*-
from djmenugen import *

from django import template

register = template.Library()

class MenuNode(template.Node):
	def __init__(self, entries):
		self.entries = entries
	
	def render(self, context):
		return gen_level(
			self.entries, u'',
			context.get('current_url'),
			context.get('menugen_ul_class'),
			context.get('menugen_li_class'),
			context.get('menugen_a_class'),
			context.get('menugen_cur_item_id', u'thispage'))

@register.tag('buildmenu')
def do_buildmenu(parser, token):
	try:
		tag, mnusrc = token.split_contents()
		mnusrc = mnusrc[1:-1].rsplit(u'.', 1)
	except ValueError:
		raise template.TemplateSyntaxError, '%s tag requires one argument' % token.split_contents()[0]

	modpath = mnusrc[0]
	mnumod = __import__(modpath, fromlist=modpath.split(u'.')[0:-1])

	mnuvar = mnusrc[1]
	return MenuNode(mnumod.__dict__[mnuvar])
