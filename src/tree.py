def template_params(params):
    if len(params) > 0:
        return 'template <{}>\n'.format(', '.join(['class ' + v for v in params]))
    else:
        return ''

class Var:
    def __init__(self, name):
        self.name = name
    
    def gen(self, ctx, allocator, writer):
        return self.name

class Abstraction:
    def __init__(self, var_name, body):
        self.var_name = var_name
        self.body = body
    
    def gen(self, ctx, allocator, writer):
        body = self.body.gen(ctx + [self.var_name], allocator, writer)
        cur_abs = allocator.new_abs()
        writer.write(template_params(ctx))
        writer.write('struct {} : _AbsBase'.format(cur_abs))
        writer.write(' {\n')
        writer.write('    template <class {}>\n'.format(self.var_name))
        writer.write('    using apply = ' + body + ';\n')
        writer.write('};\n\n')
        return cur_abs + '<' + ', '.join(ctx) + '>' if len(ctx) > 0 else cur_abs

class Application:
    def __init__(self, rator, rand):
        self.rator = rator
        self.rand = rand
    
    def gen(self, ctx, allocator, writer):
        rator = self.rator.gen(ctx,allocator, writer)
        rand = self.rand.gen(ctx, allocator, writer)
        if isinstance(self.rator, Var):
            rator = 'typename ' + rator
        return '{}::apply<{}>'.format(rator, rand)

class PatternMatching:

    class MatchCase:
        def __init__(self, data_ctor_name, var_names, expr):
            self.data_ctor_name = data_ctor_name
            self.var_names = var_names
            self.expr = expr

    def __init__(self, arg, cases):
        self.arg = arg
        self.cases = cases

    def gen(self, ctx, allocator, writer):
        arg = self.arg.gen(ctx, allocator, writer)
        case_bodies = [c.expr.gen(ctx + c.var_names, allocator, writer) for c in self.cases]
        writer.write(template_params(ctx + ['_param']))
        cur_match = allocator.new_match()
        writer.write('struct ' + cur_match + ' : _MatchBase {};\n\n')
        for c, body in zip(self.cases, case_bodies):
            writer.write('template <')
            writer.write(', '.join(['class ' + v for v in ctx + c.var_names]))
            writer.write('>\n')
            cur_arg = c.data_ctor_name
            if len(c.var_names) > 0:
                cur_arg = cur_arg + '<' + ', '.join(c.var_names) + '>'
            writer.write('struct {}<{}> : _MatchBase'.format(cur_match, ', '.join(ctx + [cur_arg])))
            writer.write(' {\n')
            writer.write('    using result = ' + body + ';\n')
            writer.write('};\n\n')
        return 'typename {}<{}>::result'.format(cur_match, ', '.join(ctx + [arg]))
    
class BinaryOperation:
    def __init__(self, op, lhs, rhs):
        assert op in {'+', '-', '*', '/'}
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
    
    def gen(self, ctx, allocator, writer):
        lhs = self.lhs.gen(ctx, allocator, writer)
        rhs = self.rhs.gen(ctx, allocator, writer)
        if self.op == '+':
            helper = '_IntAdd'
        elif self.op == '-':
            helper = '_IntMinus'
        elif self.op == '*':
            helper = '_IntMul'
        else:
            helper = '_IntDiv'
        return 'typename {}<{}, {}>::result'.format(helper, lhs, rhs)

class IntLiteral:
    def __init__(self, num):
        self.num = num
    
    def gen(self, ctx, allocator, writer):
        return '_Int<{}>'.format(self.num)

class DataConstructorDecl:
    def __init__(self, name, param_n):
        self.name = name
        self.param_n = param_n

    def gen(self, ctx, allocator, writer):
        writer.write(template_params(['_param' + str(i) for i in range(self.param_n)]))
        writer.write('struct ' + self.name + ' {\n')
        writer.write('    static void display() {\n')
        writer.write('        std::cout << "A {}\\n";\n'.format(self.name))
        writer.write('    }\n')
        writer.write('};\n')
        for i in range(self.param_n - 1, -1, -1):
            writer.write(template_params(['_param' + str(j) for j in range(i)]))
            writer.write('struct _{}_Curry{} : _DataCtorCurryBase'.format(self.name, i))
            writer.write(' {\n')
            writer.write('    template <class _param{}>\n'.format(i))
            next_struct_name = '_{}_Curry{}'.format(self.name, i + 1) if i < self.param_n - 1 else self.name
            arg = ', '.join(['_param' + str(j) for j in range(i + 1)])
            writer.write('    using apply = {}<{}>;\n'.format(next_struct_name, arg))
            writer.write('};\n')
        writer.write('\n')


class DataConstructor:
    def __init__(self, name):
        self.name = name
    
    def gen(self, ctx, allocator, writer):
        return self.name