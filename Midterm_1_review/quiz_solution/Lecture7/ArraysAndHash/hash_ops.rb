

h1 = {'key1'=>'val1', 'key2'=>'val2', 'key3'=>'val3', 'key4'=>'val4'}
h2 = {'key1'=>'val1', 'KEY_TWO'=>'val2', 'key3'=>'VALUE_3', 'key4'=>'val4'}

p( h1.keys & h2.keys ) 	# intersection
p( h1.values & h2.values ) #intersection of values
p( h1.keys+h2.keys ) #concatination
p( h1.values-h2.values ) #intersection
p( (h1.keys << h2.keys)  ) #append
p( (h1.keys << h2.keys).flatten.reverse  ) # un-nesting or flattening


s = "Hello World"
t = s.scan(/\w{2}/)
puts t