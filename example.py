# -*- coding: utf-8 -*-
"""
	Will generate into the variable output:
	<ul class="navlist">
		<li class="navitem"><a class="navlink" href="/alpha/">Alpha</a></li>
		<li class="navitem"><a class="navlink" href="/beta/">Beta</a></li>
		<li class="navitem">News Articles</li>
		<ul class="navlist">
			<li class="navitem"><a class="navlink" href="/news/sports/">Sports</a></li>
			<li class="navitem" id="curpage">Arts</li>
			<li class="navitem"><a class="navlink" href="/news/local/">Local</a></li>
			<li class="navitem"><a class="navlink" href="/news/local/">National</a></li>
		</ul>
		<li class="navitem">Animals</li>
		<ul class="navlist">
			<li class="navitem"><a class="navlink" href="/giraffe/">Giraffe</a></li>
			<li class="navitem"><a class="navlink" href="/bumblebee/">Bumblebee</a></li>
		</ul>
	</ul>
"""

import djmenugen

menudata = [
	(u'Alpha', '/alpha/'),
	(u'Beta', '/beta/'),
	(u'News Articles', [
		(None, '/news/'),
		(u'Sports', '/news/sports/'),
		(u'Arts', '/news/arts/'),
		(u'Local', '/news/local/'),
		(u'National', '/news/local/')
	]),
	(u'Animals', [
		(u'Giraffe', '/giraffe/'),
		(u'Bumblebee', '/bumblebee/')
	])
]

#Usage
menu = djmenugen.MenuGenerator(menudata,
	current_url='/news/arts/',
	cur_item_id=u'curpage',
	ul_class=u'navlist',
	li_class=u'navitem',
	a_class=u'navlink')

output = menu.generate()