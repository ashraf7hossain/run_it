class CompilerStrategy:
    def js_code(source_code) -> str:
        pass
    def generate_url(extension) ->  str:
        pass
    
class Onecompiler(CompilerStrategy):
    url_map = {
        "cpp": "cpp",
        "c"  : "c",
        "py" : "python",
        "rs" : "rust",
        "java": "java",
        "cs" : "csharp",
    }

    def generate_url(self , extension):
        lang = self.url_map.get(extension, "cpp")
        return f"https://onecompiler.com/{lang}"

    def js_code(self, source_code) -> str:
        execute_code = f"let editor = ace.edit('oc_ace'); editor.setValue(`{source_code}`)"
        return execute_code


class Programize(CompilerStrategy):
    url_map = {
        "cpp": "cpp-programming",
        "c"  : "c-programming",
        "py" : "python-programming",
        "rs" : "rust",
        "java": "java",
        "cs" : "csharp",
    }

    def generate_url(self, extension):
        lang = self.url_map.get(extension, "cpp")
        return f"https://www.programiz.com/{lang}/online-compiler/"
    
    def js_code(self, source_code) -> str:
        execute_code = f"let editor = ace.edit('editor'); editor.setValue(`{source_code}`)"
        return execute_code


class Dartpad(CompilerStrategy):
    
    def generate_url(self, extension):
        return f"https://dartpad.dev"

    def js_code(self , source_code) -> str:
        execute_code = f"const codeMirror = document.querySelectorAll('.CodeMirror')[0]; codeMirror.CodeMirror.setValue(`{source_code}`)"
        return execute_code