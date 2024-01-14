# Ruby program to illustrate the parameter
# passing to methods

#!/usr/bin/ruby

# mymethod is the method name
# var1 and var2 are the parameters
def mymethod (var1 = "CSE", var2 = "ISE")

	# statements to be executed
	puts "First parameter is #{var1}"
	puts "First parameter is #{var2}"
end

# calling method with parameters
mymethod "337", "Sudo"

puts ""

puts "Without Parameters"
puts ""

# calling method without passing parameters
mymethod
