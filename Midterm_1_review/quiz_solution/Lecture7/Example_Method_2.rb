# Ruby program to illustrate the method
# that takes variables number of arguments


# defining method mymethod that can
# take any number of arguments
def mymethod (*var)
	
# to display the total number of parameters
puts "Number of parameters is: #{var.length}"
	
# using for loop
for i in 0...var.length
	puts "Parameters are: #{var[i]}"
end
end

# calling method by passing
# variable number of arguments
mymethod "CSE", "ISE"
mymethod ("We are learning Ruby")
