# Python File Organizer
Organize your files easily using a simple JSON file

# Installation
TODO

# How to use
You will need to create a JSON file called `fs.directives.json` which must look like:
```json
{
    "categories" : {
        "images" : ["png", "jpeg", "jpg", "gif"],
        "code" : ["py", "h", "c"]
    },
    "folders" : ["myfolder/"]
}
```

When you run the project, the program with an 'apply' argument, it will inspect this JSON file and in the example above, will move all png, jpeg, gif files into a new subdirectory called 'images', and in the same likeness for 'code'. A fs.generated.json file will be created that maps the changes made.

When you run the program with an 'undo' argument, the program will move the moved files from images back to the original directory 