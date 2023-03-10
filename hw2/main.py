import os
from ast_builder.main import get_ast
import logging


def generate_latex_table(data):

    def check_data():
        return not list(filter(lambda line: len(line) != len(data[0]), data))

    if not check_data():
        logging.error("Incorrect input. All lines must contain the same amount of elements.")
        os.system(exit(1))

    size = max(map(len, data))
    first = '\\begin{tabular}'
    first += '{ ' + size * '|c' + '| }\n'
    hline = '\\hline\n'
    table = '\n'.join(map(lambda line: ' & '.join(str(el) for el in line) + '\\\\', data)) + '\n'
    last = '\\end{tabular}'
    return first + hline + table + hline + last


def generate_tex_document(content):
    begin = [
        '\\documentclass{article}',
        '\\usepackage{graphicx}',
        '\\begin{document}'
    ]
    end = ['\\end{document}']
    return '\n'.join(begin + content + end)

def generate_latex_picture(path):
    return f'\\includegraphics[width=\\textwidth]{{{path}}}'


def get_latex(data):
    table = generate_latex_table(data)
    get_ast()
    picture = generate_latex_picture('artifacts/ast_graph.png')
    document = generate_tex_document([table, picture])

    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")
    with open('artifacts/document.tex', 'w') as file:
        file.write(document)


if __name__ == '__main__':
    data = [
        ['cell1', 'cell2', 'cell3'],
        ['cell4', 'cell5', 'cell6'],
        ['cell7', 'cell8', 'cell9']
    ]

    wrong_data = [
        ['cell1', 'cell2', 'cell3'],
        ['cell4', 'cell5'],
        ['cell7', 'cell8', 'cell9']
    ]

    get_latex(data)
    os.system("pdflatex -halt-on-error -output-directory artifacts artifacts/document.tex")
    os.system("rm artifacts/document.aux artifacts/document.log artifacts/ast_graph.png")

