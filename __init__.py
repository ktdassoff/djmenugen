# -*- coding: utf-8 -*-
def id_snip(id_attr=None):
	if id_attr:
		return u' id="%s"' % id_attr
	else:
		return u''

def class_snip(class_attr=None):
	if class_attr:
		return u' class="%s"' % class_attr
	else:
		return u''


def gen_node(title, url, tabprefix, current_url, li_class, a_class, cur_item_id):
	if url == current_url:
		return tabprefix + u'\t<li%s%s>%s</li>\n' % (class_snip(li_class), id_snip(cur_item_id), title)
	else:
		return tabprefix + u'\t<li%s><a%s href="%s">%s</a></li>\n' % (class_snip(li_class), class_snip(a_class), url, title)

def gen_level(node, tabprefix, current_url, ul_class, li_class, a_class, cur_item_id):
	val = tabprefix + u'<ul%s>\n' % class_snip(ul_class)

	for title, url in node:
		if not title: continue

		try: #assume node is a dictionary with child items
			if None in url:
				val += gen_node(title, url[None], tabprefix, current_url, li_class, a_class, cur_item_id)
			else:
				val += tabprefix + u'\t<li%s>%s</li>\n' % (class_snip(li_class), title)

			val += gen_level(url, tabprefix + u'\t', current_url, ul_class, li_class, a_class, cur_item_id)

		except (AttributeError, TypeError):
			val += gen_node(title, url, tabprefix, current_url, li_class, a_class, cur_item_id)

	val += tabprefix + u'</ul>\n'
	return val

class MenuGenerator(object):
	def __init__(self, entries, current_url=None, cur_item_id=u'thispage',
			ul_class=None, li_class=None, a_class=None):
		self.entries = entries
		self.current_url = current_url
		self.cur_item_id = cur_item_id
		self.ul_class = ul_class
		self.li_class = li_class
		self.a_class = a_class
	
	def generate(self):
		return gen_level(self.entries, u'', self.current_url, self.ul_class, self.li_class, self.a_class, self.cur_item_id)

import context_processors