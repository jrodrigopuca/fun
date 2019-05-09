class Perro
	def initialize(nombre)
		@name= nombre
	end

	def ladrar()
		puts "guau"
	end
end

perrito= Perro.new("Bobby")
#perrito.ladrar() #=> "guau"
#puts perrito.inspect #=> <Perro @name="Bobby">
