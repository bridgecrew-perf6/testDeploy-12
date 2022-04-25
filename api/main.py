from flask_restx import Namespace, Resource
from http import HTTPStatus
from werkzeug.exceptions import Conflict


math_namespace=Namespace("Math", description="Calculates and provides results for Fibonacci,Ackermann and factorial")

@math_namespace.route("/feibonacci/<int:x>")
class Fibonacci(Resource):

    def get(self, x):
        """
        The n:th Fibonacci number F(n) with the value of n provided by the user        
        """
        try:
            m = 0
            n = 1

            if x < 0:
                print("Fibonacci can't be computed")
            elif x == 0:
                return m
            elif x == 1:
                return n
            else:
                return self.get(x-1) + self.get(x-2)
        except Exception as e:
            print(f'Fibonacci function: {e}')
            raise Conflict(f'Fibonacci function: {e}')
            


@math_namespace.route('/ackermann/<int:m>/<int:n>')
class Ackermann(Resource):

    def get(self, m, n):
        """
        The Ackermann function A(m,n) with values of m and n provided by the user
        """
        try:
            if m == 0:
                return n + 1
            elif m > 0 and n == 0:
                return self.get(m - 1, 1)
            elif m > 0 and n > 0:
                return self.get(m - 1, self.get(m, n - 1))
        except Exception as e:
            print(f'Ackermann function: Recursive depth exceeded {e}')
            raise Conflict(f'Ackermann function: Recursive depth exceeded {e}')


@math_namespace.route('/factorial/<int:n>')
class Factorial(Resource):

    def get(self, n):
        """
        The factorial n! of a non-negative integer n provided by the user.
        """
        try:
            if n == 0:
                return 1
            else:
                return n * self.get(n-1)
        except Exception as e:
            print(f'Factorial function: {e}')
            raise Conflict(f'Factorial function: {e}')