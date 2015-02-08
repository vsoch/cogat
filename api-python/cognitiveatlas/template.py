import os
import api

def get_package_dir():
   return os.path.abspath(os.path.join(os.path.dirname(api.__file__)))

def get_template(html_name):
  return read_template(html_name)
  
# Add code string to end of template
def add_javascript_function(function_code,template):
  template.append("<script>\n%s\n</script>" % (function_code))
  return template

def read_template(html_name):
  # Get package directory
  ppwd = get_package_dir()  
  html_name = html_name + ".html"
  template_file = os.path.join(ppwd,'html', html_name)
  return open(template_file,"r").readlines()

'''Add strings to a template  eg, {"TAG":"text"} will replace [TAG] with text in template!'''
def add_string(repl_dict,template):
  for tag,code in repl_dict.iteritems():
    template = [t.replace("[%s]" %(tag),code) for t in template]
  return template
