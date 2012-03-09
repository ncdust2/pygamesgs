from distutils.core import setup   
import py2exe  
  
includes = ["encodings", "encodings.*",'pygame']  
  
options = {"py2exe":   
            {   "compressed": 1,   
                "optimize": 2,   
                "includes": includes,   
                "bundle_files": 1,
                "packages": ['pygame'],  
            }   
          }   
setup(      
    version = "0.1.0",   
    description = "3th",   
    name = "For My Love",
    options = options,
    zipfile=None,   
    windows=[{"script": "sgs.py", "icon_resources": [(1, "roses.ico")] }],     
    ) 
