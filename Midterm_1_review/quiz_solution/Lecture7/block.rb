def test
   puts "You are in the method"
   yield
   puts "You are again back to the method"
   yield
end
test {puts "You are in the block"}


def one_yield
  yield
end

def multiple_yields
  yield
  yield
end

one_yield { puts "one yield" }
multiple_yields{ puts "two yield"}
