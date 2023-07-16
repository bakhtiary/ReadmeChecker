import os
from glob import glob
result = [y for x in os.walk(".") for y in glob(os.path.join(x[0], '*.md'))]


import mistune
import ast

class DockerVisitor(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, list):
            for item in node:
                if item['type'] == 'block_code':
                    self.process_block_code(item)
                self.visit(item)

    def process_block_code(self, item):
        print(f"block code found{item}")


def checkFile(filename):
    ast_of_markdown = get_ast(filename)
    dv = DockerVisitor()
    dv.visit(ast_of_markdown)


def get_ast(filename):
    markdown = mistune.create_markdown(renderer=None)
    with open(filename) as the_file:
        ast_of_markdown = markdown(the_file.read())
    return ast_of_markdown


for readme in result:
    checkFile(readme)