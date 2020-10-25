import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from bs4 import BeautifulSoup
import markdown
import codecs

class TocSidebar(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        soup = BeautifulSoup(output_content, 'html.parser')
        nav_extra = soup.find("div", {"id": "sidebar-extra"})
        if nav_extra:
            soup_target_sidebar = soup.find("div", {"class" : "sphinxsidebarwrapper"})
            
            if soup_target_sidebar:
                soup_target_sidebar.insert(5, nav_extra)
            else:
                print("WARNING: Table of Contents sidebar not found")
   
        souped_html = soup.prettify(soup.original_encoding)
        return souped_html 

