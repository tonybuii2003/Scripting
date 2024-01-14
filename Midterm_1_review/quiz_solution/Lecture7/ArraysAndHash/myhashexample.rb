# Ruby program to illustrate
# use of sort method
 
a = { "x" => 34, "y" => 60, "z"=>33 }
 
# Using sort method
p a.sort
p a.sort {|x, y| x[1]<=>y[1]}