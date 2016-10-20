import codecs
from optparse import OptionParser
import os
import pprint
import requests
import sys

""" Parse command line arguments to determine input files to use or set to defaults if none are provided. """
parser = OptionParser()
parser.add_option("-d", "--source-dir", 
        dest="source_dir", 
        default=".", 
        help="Source directory", metavar="DIR")
parser.add_option("-e", "--endpoint", 
        dest="endpoint", 
        default="http://0.0.0.0:8080", 
        help="Apache Sling endpoint", metavar="URI")

(options, args) = parser.parse_args()

def get_file_list(dir=options.source_dir):
    """ Returns list of all html files in specified directory (recursive) """
    fileList = []

    for root, subFolders, files in os.walk(dir,onerror=walk_error):
        for file in files:
            filepath = os.path.join(root,file)
            if ".html" in filepath:
                fileList.append(filepath)
    return fileList

def walk_error(e):
    print e.strerror+': '+e.filename

def import_to_jcr(fileList):
    """ Import files to Day JCR using Apache SlingPostServlet """
    for idx, file in enumerate(fileList):
        try:
            with codecs.open(file,'r','utf-8') as f:
                print "index: %s - %s" % (str(idx), file)
                contents = f.read()
                if not contents:
                    contents = 'empty'

                payload = {
                            'sling:resourceType': 'plain',
                            'title': file,
                            'text': contents
                        }

                try:
                    r = requests.post(options.endpoint+'/content/'+file,data=payload,auth=('admin','admin'))
                except requests.exceptions.ConnectionError:
                    print "connection error"
                except Exception as ex:
                    print ex

        except UnicodeDecodeError as ex:
            print "Unicode decode error: "+str(ex)

# Program flow starts here
fileList = get_file_list()
import_to_jcr(fileList)
