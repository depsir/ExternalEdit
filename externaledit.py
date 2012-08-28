import sublime, sublime_plugin
import re
from wiki import *
from api import *
from page import *
from category import *
from user import *
from wikifile import *


class ExternalEdit:
	site = None
	mypage = None
	wk_type = None
	wk_engine = None
	wk_script = None
	wk_server = None
	wk_path = None
	wk_url = None
	pagename = None

	def load(self, view):
		wk_type = view.find('Type=.*',0)
		wk_engine = view.find('Engine=.*',0)
		wk_script = view.find('Script=.*',0)
		wk_server = view.find('Server=.*',0)
		wk_path = view.find('Path=.*',0)
		wk_url = view.find('URL=.*',0)
		if view.find('[Process]',0) and \
			view.find('[File]',0) and \
			wk_type and \
			wk_engine and \
			wk_script and \
			wk_server and \
			wk_path and \
			wk_url:

			wk_type= view.substr(sublime.Region(wk_type.a + 5, wk_type.b))
			wk_engine = view.substr(sublime.Region(wk_engine.a + 7, wk_engine.b))
			wk_script = view.substr(sublime.Region(wk_script.a + 7, wk_script.b))
			wk_server = view.substr(sublime.Region(wk_server.a + 7, wk_server.b))
			wk_path = view.substr(sublime.Region(wk_path.a + 5, wk_path.b))
			wk_url = view.substr(sublime.Region(wk_url.a + 4, wk_url.b))
			self.site = wiki.Wiki(wk_server+wk_path+"/api.php") 
			pagename = re.search('title=([^&]*)', wk_url)
			pagename = pagename.group(1)
			view.set_name(pagename)
			self.mypage = page.Page(self.site, pagename)
			edit = view.begin_edit()
			reg = sublime.Region(0,view.size())
			view.erase(edit,reg)
			view.set_syntax_file('Packages/Mediawiki.tmbundle/Syntaxes/Mediawiki.tmLanguage')
			view.set_encoding('utf-8')
			view.insert(edit,0,self.mypage.getWikiText().decode('utf-8'))
			view.end_edit(edit)

ee = ExternalEdit()

class eeSendChanges(sublime_plugin.TextCommand):
	def run(self, edit):
		global ee
		s = self.view.settings()
		if s.has("externaledit_username") and s.has("externaledit_password"):
			ee.site.login(s.get("externaledit_username", ''), s.get("externaledit_password", ''))
			ee.mypage.edit(self.view.substr(sublime.Region(0,self.view.size())))
			print "saved"

class eeProcessControlFile(sublime_plugin.TextCommand):
	def run(self, edit):
		global ee
		ee.load(self.view)

class EEEventListener(sublime_plugin.EventListener):
	def on_load(self,view):
		global ee
		doc = view.file_name()
		if re.search(r'index( *\([0-9]*\))*.php$',doc):
			ee.load(view)