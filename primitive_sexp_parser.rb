# Just a rough idea for a sexp parser
#p "(this is an sexpression)".parse_sexp
#p [:this, :is, :an, :sexpression].to_sexp

require 'rubygems'
require 'sexp'

def koala_puts(statement)
  eval("puts '#{statement}'")
end

def koala_add(operands)
  operands.reduce { |total, element| total += element }
end

def koala_subtract(operands)
  operands.reduce { |total, element| total -= element }
end

def koala_multiply(operands)
  operands.reduce { |total, element| total *= element }
end

def koala_divide(operands)
  operands.reduce { |total, element| total /= element }
end

@operators = {
  # The equivalent of puts, yes I'm lazy
  :p => lambda { |statement| koala_puts(statement) },
  
  # Mathematical operators
  :+ => lambda { |statement| koala_add(statement) },
  :- => lambda { |statement| koala_subtract(statement) },
  :* => lambda { |statement| koala_multiply(statement) },
  :/ => lambda { |statement| koala_divide(statement) }
}

code = <<BLOCK
  (p (/ (- (+ 5 2) (+ 1 0) (* 5 2)) 2))  
BLOCK

ast = code.parse_sexp

def evaluate(statement)
  operator = statement.shift
  
  if @operators.has_key?(operator)
    unless statement.empty?
      buffer = []

      statement.each do |operand|
        if operand.class == Array
          buffer << evaluate(operand)
        else
          buffer << operand
        end
      end

      return @operators[operator].call(buffer)
    end
  else
    raise Exception.new "Operator '#{operator}' does not exist"
  end
end
  
ast.each do |statement|
  evaluate(statement)
end
