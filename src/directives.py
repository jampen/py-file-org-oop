import json


class Directives:
    def load(self, filepath):
        return False

    def ext_to_category(self, extension):
        return ''


'''

fs.directives.json JSON

{
    "categories" : {
        "images" : ["png", "jpeg", "jpg", "gif"],
        "code" : ["py", "h", "c"]
    },
    "folders" : ["myfolder/"]
}


'''
