# -*- coding: utf-8 -*-
"""
	Given a simple data structure, generates an HTML link menu using unordered lists.
	The menu may have multiple levels.
	
	The data structure is a list of two-tuples. Each tuple represents one menu entry.
	The first element in each tuple is the text that will be displayed in the page.
	The second element in each tuple is the url that will be placed in the link's href attribute.
	
	Alternatively, the second element may be another list of two-tuples in order to create a sub-menu.
	In that case, the first element is still the text displayed. If you want the entry to have its own link url
	in addition to the sub-menu, in the inner list, include a two-tuple where the first element is None rather
	than a string.
	
	Associated properties available using MenuGenerator are:
		current_url:           if a menu item has the same url as this option, then it will be generated without
		                       the link element and optionally with an id attribute on its list item element
		cur_item_id:           the id to add to the entry that matches current_url (default is u"thispage")
		ul_class,
		li_class,
		a_class:               the class attribute to include on each ul, li, and a element, respectively
	
	See example.py for an example data structure and the generated HTML
"""

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
	'Returns a list item and hyperlink for the current title+url (or just a list item if it is the current url.'
	
	if url == current_url:
		return tabprefix + u'\t<li%s%s>%s</li>\n' % (class_snip(li_class), id_snip(cur_item_id), title)
	else:
		return tabprefix + u'\t<li%s><a%s href="%s">%s</a></li>\n' % (class_snip(li_class), class_snip(a_class), url, title)

def gen_level(node, tabprefix, current_url, ul_class, li_class, a_class, cur_item_id):
	'Returns an HTML unordered list from the node data structure.'
	
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
	"""
		Encapsulates a menu data structure and its associated properties.
		See module-level documentation for information on the data structure used
		and the available options.
	"""
	
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