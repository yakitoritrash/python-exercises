valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

def filter_by(doc):
    for d in doc:
        if d in valid_formats:
            return True;
        else:
            return False;

document = []
filter_by(document);

