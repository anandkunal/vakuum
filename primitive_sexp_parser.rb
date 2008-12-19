# Just a rough idea for a sexp parser

require 'rubygems'
require 'sexp'

#p "(this is an sexpression)".parse_sexp
#p [:this, :is, :an, :sexpression].to_sexp

operators = {
  :puts => lambda {|statement| "echo #{statement};"}
}

code = <<BLOCK
  (puts "hi there")
BLOCK

# Clear out all the line comments and strip line endings
code.gsub!(/^(\s*)(;;)(.*)$/, '')
code.strip!

ast = code.parse_sexp

ast.each do |node|
  operator = node.shift
  
  if operators.has_key?(operator)
    puts operators[operator].call(node)
  else
    raise Exception.new "Operator '#{operator}' does not exist"
  end
end