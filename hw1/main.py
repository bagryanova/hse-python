import ast
import inspect
import os
import networkx


class AstGraphVisitor:
    def __init__(self):
        self.graph = networkx.DiGraph()
        self.cnt = 0
        self.operations = ["Add", "Sub", "Mult"]

    def visit(self, node):
        method = '_visit_' + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node)

    def add_edges(self, root, nodes, edges_name=None):
        for node in nodes:
            if edges_name is not None:
                self.graph.add_edge(root, node, label=edges_name)
            else:
                self.graph.add_edge(root, node)

    def _visit_Module(self, node):
        self.graph.add_node(node, label='Module')
        self.add_edges(node, self.visit(node.body[0]))
        return [node]

    def _visit_arguments(self, node):
        self.graph.add_node(node, shape='box', label='arguments', style='filled', fillcolor='purple')
        for arg in node.args:
            self.graph.add_node(arg, shape='box', label=f'Argument {arg.arg}', style='filled', fillcolor='plum')
            self.add_edges(node, [arg])
        return [node]

    def _visit_Constant(self, node):
        self.graph.add_node(node, shape='box', label=f'Constant {node.value}', style='filled', fillcolor='lightyellow')
        return [node]

    def _visit_FunctionDef(self, node):
        self.graph.add_node(node, shape='box', label=f'Function {node.name}', style='filled', fillcolor='honeydew')
        self.add_edges(node, self.visit(node.args))
        for body in node.body:
            self.add_edges(node, self.visit(body))
        return [node]

    def _visit_BinOp(self, node):
        for op in self.operations:
            if op in str(node.op):
                node.op = op

        self.graph.add_node(node, shape='box', label=f'BinOp {node.op}', style='filled', fillcolor='salmon')
        self.add_edges(node, self.visit(node.left), 'left')
        self.add_edges(node, self.visit(node.right), 'right')
        return [node]

    def _visit_For(self, node):
        self.graph.add_node(node, shape='box', label='For', style='filled', fillcolor='springgreen')
        self.add_edges(node, self.visit(node.target))
        self.add_edges(node, self.visit(node.iter))
        for body in node.body:
            self.add_edges(node, self.visit(body))
        return [node]

    def _visit_Assign(self, node):
        self.graph.add_node(node, shape='box', label='Assign', style='filled', fillcolor='lightgray')
        for target in node.targets:
            self.add_edges(node, self.visit(target), 'target')
        self.add_edges(node, self.visit(node.value), 'value')
        return [node]

    def _visit_Return(self, node):
        self.graph.add_node(node, shape='box', label='Return', style='filled', fillcolor='red')
        self.add_edges(node, self.visit(node.value))
        return [node]

    def _visit_List(self, node):
        self.graph.add_node(node, shape='box', label='List', style='filled', fillcolor='hotpink')
        for elt in node.elts:
            self.add_edges(node, self.visit(elt))
        return [node]

    def _visit_Subscript(self, node):
        self.graph.add_node(node, shape='box', label='Subscript', style='filled', fillcolor='lightgreen')
        self.add_edges(node, self.visit(node.value), 'value')
        self.add_edges(node, self.visit(node.slice), 'slice')
        return [node]

    def _visit_Call(self, node):
        self.graph.add_node(node, shape='box', label='Call', style='filled', fillcolor='deepskyblue')
        self.add_edges(node, self.visit(node.func), 'func')
        for arg in node.args:
            self.add_edges(node, self.visit(arg), 'arg')
        return [node]

    def _visit_Name(self, node):
        self.graph.add_node(node, shape='box', label=f'Name {node.id}', style='filled', fillcolor='lavender')
        return [node]


def get_fib(n):
    res = [0] * n
    res[0] = res[1] = 1
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res


def get_ast():
    ast_object = ast.parse(inspect.getsource(get_fib))
    v = AstGraphVisitor()
    v.visit(ast_object)
    g = networkx.drawing.nx_pydot.to_pydot(v.graph)
    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")
    g.write_png('artifacts/ast_graph.png')


if __name__ == '__main__':
    get_ast()
